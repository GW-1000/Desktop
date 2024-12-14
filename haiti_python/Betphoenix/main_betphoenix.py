import asyncio
import json
import pandas as pd
from haiti_python.markets import markets_list
from betphoenix_websocket import connect_to_websocket
from extract_json import logic_bpo

async def main():
    df = pd.DataFrame({"market": markets_list})
    matches = await connect_to_websocket()
    for match in matches:
        if not match == None:
            df[df.shape[1]] = logic_bpo(match)
    df.to_csv("C:/Users/daniel/PycharmProjects/placerbot/haiti/csvfiles/betphoenix.csv", index=False)
    df.to_pickle("C:/Users/daniel/PycharmProjects/placerbot/haiti/webresults/betphoenix.pkl")


asyncio.run(main())