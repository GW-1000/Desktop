import json
import aiohttp
import asyncio
import time
from datetime import datetime, timedelta


def unix_time():
    # Get the current time
    now = datetime.now()

    # Get the start of the current day
    start_of_today = datetime(now.year, now.month, now.day)

    # Get the start of tomorrow
    start_of_tomorrow = start_of_today + timedelta(days=2)

    # Convert to Unix timestamp
    start_of_today_unix = int(time.mktime(start_of_today.timetuple()))
    start_of_tomorrow_unix = int(time.mktime(start_of_tomorrow.timetuple()))

    return start_of_today_unix + 5400, start_of_tomorrow_unix


async def response_handler(ws):
    async for msg in ws:
        if msg.type == aiohttp.WSMsgType.TEXT:
            response_data = json.loads(msg.data)  # Convert string to JSON object with open('data.json', 'w') as file:
            if "rid" in response_data and "data" in response_data:
                if response_data["rid"] != "0" and "subid" in response_data["data"]:
                    print("Received:response_data")
                    return response_data
        elif msg.type == aiohttp.WSMsgType.CLOSED:
            print("closed")
            return None
        elif msg.type == aiohttp.WSMsgType.ERROR:
            print(f"Error: {msg.data}")
            return None

async def send_match_request(semaphore, match_request):
    async with semaphore:
        async with aiohttp.ClientSession() as session:
            try:
                async with session.ws_connect("wss://eu-swarm-newm.betconstruct.com/", timeout=61) as ws:
                    await ws.send_json({"command":"request_session","params":{"language":"fra","site_id":1345,"source":42,"local_ip":"137.196.0.6","release_date":"11/19/2024-10:33","afec":"BWUyFURkHuSwj4U2vXXSs-qWoS0OmZ_OS9sZ"},"rid":"5b2023e88dc25a3ffbcf924ef32e15d8eff56002"})
                    await ws.send_json(match_request)
                    try:
                        msg = await asyncio.wait_for(response_handler(ws), timeout=120)
                    except asyncio.TimeoutError:
                        print(f"Timeout: No response received for the match request within {120} seconds")
                        await ws.close()
                        return None
                    return msg
            except aiohttp.client_exceptions.ServerDisconnectedError:
                print("Server disconnected")
                return None
            except aiohttp.client_exceptions.ClientConnectorError:
                print("errored")
                return None
            except aiohttp.client_exceptions.ConnectionTimeoutError:
                return None


async def connect_to_websocket(login, ids_request):
    async with aiohttp.ClientSession() as session:
        async with session.ws_connect('wss://eu-swarm-newm.betconstruct.com/') as ws:
            await ws.send_json(login)
            ids = []
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    response_data = json.loads(msg.data)  # Convert string to dictionary
                    if 'code' in response_data and "rid" in response_data and "data" in response_data:
                        print(f"Received: {msg.data}")
                        await ws.send_json(ids_request)
                        break  # ensure we proceed to the next message only after handling match request
            async for msg in ws:
                if msg.type == aiohttp.WSMsgType.TEXT:
                    response_data = json.loads(msg.data)  # Convert string to JSON object with open('data.json', 'w') as file:
                    if "rid" in response_data:
                        if response_data["rid"] != "0":
                            data = response_data['data']['data']['sport']['1']['region']
                            for cat, cat_data in data.items():
                                for comp_id, comp_data in cat_data['competition'].items():
                                    for game_id, other in comp_data['game'].items():
                                        ids.append((cat_data['alias'], comp_id, game_id))
                            print(f"Received:")
                            break
                elif msg.type == aiohttp.WSMsgType.ERROR:
                    break

            # create a semaphore to limit the number of requests
            semaphore = asyncio.Semaphore(150)  # 320 request will be made at once after each batch
            tasks = []
            for evt_id in ids:
                match_req = {"command":"get","params":{"source":"betting","what":{"sport":["name"],"region":["name"],"competition":["name"],"game":["id","stats","info","is_neutral_venue","add_info_name","text_info","markets_count","type","start_ts","is_stat_available","team1_id","team1_name","team2_id","team2_name","last_event","live_events","match_length","sport_alias","sportcast_id","region_alias","is_blocked","show_type","game_number"],"market":["id","group_id","group_name","group_order","type","name_template","sequence","point_sequence","name","order","display_key","col_count","express_id","extra_info","cashout","is_new","has_early_payout"],"event":["id","type_1","price","name","base","home_value","away_value","display_column","order"]},"where":{"game":{"id":int(evt_id[2])},"sport":{"alias":"Soccer"},"region":{"alias":evt_id[0]},"competition":{"id":int(evt_id[1])}},"subscribe":"true"},"rid":"0f533c71d10b07e5eeee7860af88a3a3da0ef132"}
                tasks.append(send_match_request(semaphore, match_req))

            results = await asyncio.gather(*tasks)  # this runs all the requests at once and waits for all responses

            return results


async def main_websocket():
    S, E = unix_time()
    json_request_ids = {"command": "get", "params": {"source": "betting", "what": {"game": ["id"],
                                                                                   "market": ["type", "name",
                                                                                              "display_key", "base",
                                                                                              "id", "express_id"],
                                                                                   "event": ["id", "price", "type_1",
                                                                                             "name", "base", "order"],
                                                                                   "region": ["alias"],
                                                                                   "competition": ["id"],
                                                                                   "sport": ["alias"]},
                                                     "where": {"sport": {"id": {"@in": [1]}},
                                                               "game": {"type": 2, "start_ts": {"@gte": S, "@lt": E},
                                                                        "show_type": {"@ne": "OUTRIGHT"}},
                                                               "market": {"display_key": "WINNER",
                                                                          "display_sub_key": "MATCH"}},
                                                     "subscribe": "true"},
                        "rid": "20f921a4bb50041eed6f29ca16580bf58c86adb4"}
    json_login = {"command": "request_session",
                  "params": {"language": "fra", "site_id": 1345, "source": 42, "local_ip": "137.196.0.6",
                             "release_date": "11/19/2024-10:33", "afec": "BWUyFURkHuSwj4U2vXXSs-qWoS0OmZ_OS9sZ"},
                  "rid": "5b2023e88dc25a3ffbcf924ef32e15d8eff56002"}
    results = await connect_to_websocket(login=json_login, ids_request=json_request_ids)
    return results

