import pickle

from logic import logic_gh
from golcashaiti_websocket import main_websocket
from haiti_python.markets import markets_list
import asyncio
import pandas as pd

async def main():
    df = pd.DataFrame({"market": markets_list})
    matches = await main_websocket()
    for match in matches:
        if not match == None:
            df[df.shape[1]] = logic_gh(match)
    df.to_csv("C:/Users/daniel/PycharmProjects/placerbot/haiti/csvfiles/golcashhaiti.csv", index=False)
    # Pickling the list
    df.to_pickle("C:/Users/daniel/PycharmProjects/placerbot/haiti/webresults/golcashhaiti.pkl")

asyncio.run(main())