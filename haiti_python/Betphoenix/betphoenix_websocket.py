import json
import aiohttp
import asyncio
import time
from datetime import datetime, timedelta

def format_date(my_date):
    # Example ISO 8601 time format
    iso_time =  my_date

    # Convert to datetime object
    dt = datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%S%z")

    # Convert to Unix timestamp
    unix_timestamp = int(dt.timestamp())

    return unix_timestamp


def start_end_times():
    # Current Unix timestamp
    current_timestamp = int(time.time())

    # Unix timestamp for tomorrow midnight
    tomorrow = datetime.now().date() + timedelta(days=2)
    tomorrow_midnight = datetime.combine(tomorrow, datetime.min.time())
    tomorrow_midnight_timestamp = int(tomorrow_midnight.timestamp())

    return current_timestamp + 5400, tomorrow_midnight_timestamp


# function to listen in for the response
async def response_handler(ws):
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            response_data = json.loads(msg.data)
            if "action" in response_data and "marker" in response_data:
                if response_data["marker"] == "event":
                    print("Received: ")
                    return response_data
        elif msg.type == aiohttp.WSMsgType.CLOSED:
            print("closed")
            return None
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f"Error: {msg.data}")
            return None


# function to send 1 match request
async def send_match_request(semaphore, match_request, max_retries=3, timeout=150):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            attempt = 0
            while attempt < max_retries:
                try:
                    async with session.ws_connect('wss://wss2.betphoenix.info/ws/', timeout=timeout) as ws:
                        await ws.send_json({"token": "demo", "lang": "HT", "tree": "false", "hot": "false"})
                        await asyncio.sleep(1)
                        await ws.send_json(match_request)

                        try:
                            msg = await asyncio.wait_for(response_handler(ws), timeout=timeout)
                            return msg
                        except asyncio.TimeoutError:
                            print(f"Timeout attempt {attempt + 1}: No response received within {timeout} seconds")
                            if attempt < max_retries - 1:
                                attempt += 1  # Retry using the same connection
                                print(f"Retrying request... (Attempt {attempt + 1})")
                                continue
                            else:
                                await ws.close()
                                return None
                except aiohttp.ClientError as e:
                    print(f"Connection attempt {attempt + 1} failed with error: {e}")
                    if attempt < max_retries - 1:
                        attempt += 1  # Establish a new connection
                        print(f"Retrying connection... (Attempt {attempt + 1})")
                    else:
                        return None


async def connect_to_websocket():
    async with aiohttp.ClientSession() as session:   # session manager closes the library i opened once the code is done with it
        async with session.ws_connect('wss://wss2.betphoenix.info/ws/') as ws:  # establish the connection to the websocket

            await ws.send_json({"token": "demo", "lang": "HT", "tree": "false", "hot": "false"})
            await asyncio.sleep(1)
            await ws.send_json({"action":"events","sport":1,"filter":{"antepost":False},"marker":"anteposts"})  # send the json which asks for event ids
            ids = []  # initialise a list to store tournament ids

            async for msg in ws:  # a loop that runs as long as the connection is up
                if msg.type == aiohttp.WSMsgType.TEXT:  # check if the response is the tournaments ids
                    response_data = json.loads(msg.data)  # Convert string to dictionary

                    if "action" in response_data and "marker" in response_data:  # check if its the target message
                        if response_data["marker"] == "anteposts":  # check if its the target message

                            # extract the event ids and append to a list
                            S, E = start_end_times()
                            cats = response_data["data"]["1"]
                            for _, level1 in cats.items():
                                for _, level2 in level1.items():
                                    for identity, level3 in level2.items():
                                        if S <= format_date(level3["tm"]) <= E:
                                            ids.append(identity)
                            break

            print(len(ids))
            # create a semaphore to limit the number of requests
            semaphore = asyncio.Semaphore(50)  # 320 request will be made at once after each batch
            tasks = []
            for evt_id in ids:
                match_req = {"action": "events", "level": 2, "id": evt_id, "filter": {"notempty": True}, "marker": "event"}
                tasks.append(send_match_request(semaphore, match_req))

            results = await asyncio.gather(*tasks)  # this runs all the requests at once and waits for all responses

            return results






