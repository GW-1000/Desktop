import json
import aiohttp
import asyncio


# function to listen in for the response
async def response_handler(ws):
    print("called response_handler")
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            response_data = json.loads(msg.data)
            if "action" in response_data and "marker" in response_data:
                if response_data["marker"] == "sport":
                    print(f"Received: {response_data}")
                    return response_data
        elif msg.type == aiohttp.WSMsgType.CLOSED:
            print("closed")
            return None
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f"Error: {msg.data}")
            return None


# function to send individual match request
async def send_match_request(semaphore, match_request):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.ws_connect('wss://wss2.betphoenix.info/ws/', timeout=61) as ws:
                    await ws.send_json({"token": "demo", "lang": "HT", "tree": "false", "hot": "false"})
                    await ws.send_json(match_request)

                    try:
                        msg = await asyncio.wait_for(response_handler(ws), timeout=120)
                    except asyncio.TimeoutError:
                        print(f"Timeout: No response received for the match request within {120} seconds")
                        await ws.close()
                        return None
                    if msg:
                        return msg
            except aiohttp.client_exceptions.ConnectionTimeoutError:
                return None


async def connect_to_websocket():
    async with aiohttp.ClientSession() as session:   # session manager closes the library i opened once the code is done with it
        async with session.ws_connect('wss://wss2.betphoenix.info/ws/') as ws:  # establish the connection to the websocket

            await ws.send_json({"token": "demo", "lang": "HT", "tree": "false", "hot": "false"})
            await asyncio.sleep(1)
            await ws.send_json({"action":"events","sport":1,"filter":{"antepost":False},"marker":"anteposts"})  # send the json which asks for event ids
            ids = []  # initialise a list to store tournament ids

            async for msg in ws:  # a loop that runs as long as the connection is up
                if msg.type == aiohttp.WSMsgType.TEXT:  # check if the response is the event ids
                    response_data = json.loads(msg.data)  # Convert string to dictionary

                    if "action" in response_data and "marker" in response_data:  # check if its the target message
                        if response_data["marker"] == "anteposts":  # check if its the target message

                            # extract the event ids and append to a list
                            cats = response_data["data"]["1"]
                            for _, level1 in cats.items():
                                for _, level2 in level1.items():
                                    for identity, level3 in level2.items():
                                        ids.append(identity)
                            break

            # create a semaphore to limit the number of requests
            semaphore = asyncio.Semaphore(300)  # 300 request will be made at once after each batch
            tasks = []
            for evt_id in ids:
                match_req = {"action": "events", "level": 3, "id": evt_id, "filter": {"notempty": True}, "marker": "sport"}
                tasks.append(send_match_request(semaphore, match_req))

            results = await asyncio.gather(*tasks)  # this runs all the requests at once and waits for all responses
            for index, item in enumerate(results):
                with open(f'{index}.json', 'w') as file:  # convert each match to json
                    json.dump(item, file, indent=4)


asyncio.run(connect_to_websocket())



