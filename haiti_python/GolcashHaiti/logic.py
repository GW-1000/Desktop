from haiti_python.markets import markets_list
import pandas as pd
import os
import json

# Path to your folder containing JSON files
folder_path = 'C:/Users/daniel/PycharmProjects/placerbot/group_project/events'

# List all files in the folder
files = os.listdir(folder_path)


def logic_gh(x):
    data = x['data']['data']['sport']['1']['region']
    for region_id, region_data in data.items():
        for comp_id, comp_data in region_data["competition"].items():
            for key, game_data in comp_data.items():
                if type(game_data) is dict:
                    for idkey, game_data in game_data.items():
                        game = game_data

    odds = ["", "", "", "", [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        , [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        , [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        , [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
            , [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    odds[0] = game["id"]
    odds[1] = game["start_ts"]
    odds[2] = game["team1_name"]
    odds[3] = game["team2_name"]

    for market_id, market_data in game["market"].items():
        if market_data["name_template"] == "Match Result":
            for _, events in market_data["event"].items():
                if events["type_1"] == "W1":
                    odds[4] = ["GH", events["price"]]
                elif events["type_1"] == "W2":
                    odds[6] = ["GH", events["price"]]
                elif events["type_1"] == "X":
                    odds[8] = ["GH", events["price"]]
        elif market_data["name_template"] == "Double Chance":
            for _, events in market_data["event"].items():
                if events["type_1"] == "1X":
                    odds[7] = ["GH", events["price"]]
                elif events["type_1"] == "X2":
                    odds[5] = ["GH", events["price"]]
                elif events["type_1"] == "12":
                    odds[9] = ["GH", events["price"]]
        elif market_data["name_template"] == "Corners: Result":
            for _, events in market_data["event"].items():
                if events["type_1"] == "W1":
                    odds[10] = ["GH", events["price"]]
                elif events["type_1"] == "W2":
                    odds[12] = ["GH", events["price"]]
                elif events["type_1"] == "X":
                    odds[14] = ["GH", events["price"]]
        elif market_data["name_template"] == "Corners: Double Chance":
            for _, events in market_data["event"].items():
                if events["type_1"] == "1X":
                    odds[13] = ["GH", events["price"]]
                elif events["type_1"] == "X2":
                    odds[11] = ["GH", events["price"]]
                elif events["type_1"] == "12":
                    odds[15] = ["GH", events["price"]]
        elif market_data["name_template"] == "Corners: Total":
            for _, events in market_data["event"].items():
                if events["base"] == 2.5 and events["type_1"] == "Over":
                    odds[16] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Under":
                    odds[17] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Over":
                    odds[18] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Under":
                    odds[19] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Over":
                    odds[20] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Under":
                    odds[21] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Over":
                    odds[22] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Under":
                    odds[23] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Over":
                    odds[24] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Under":
                    odds[25] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Over":
                    odds[26] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Under":
                    odds[27] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Over":
                    odds[28] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Under":
                    odds[29] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Over":
                    odds[30] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Under":
                    odds[31] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Over":
                    odds[32] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Under":
                    odds[33] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Over":
                    odds[34] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Under":
                    odds[35] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Over":
                    odds[36] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Under":
                    odds[37] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Over":
                    odds[38] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Under":
                    odds[39] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Over":
                    odds[40] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Under":
                    odds[41] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Over":
                    odds[42] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Under":
                    odds[43] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Over":
                    odds[44] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Under":
                    odds[45] = ["GH", events["price"]]
                elif events["base"] == 10 and events["type_1"] == "Over":
                    odds[46] = ["GH", events["price"]]
                elif events["base"] == 10 and events["type_1"] == "Under":
                    odds[47] = ["GH", events["price"]]
                elif events["base"] == 10.5 and events["type_1"] == "Over":
                    odds[48] = ["GH", events["price"]]
                elif events["base"] == 10.5 and events["type_1"] == "Under":
                    odds[49] = ["GH", events["price"]]
                elif events["base"] == 11 and events["type_1"] == "Over":
                    odds[50] = ["GH", events["price"]]
                elif events["base"] == 11 and events["type_1"] == "Under":
                    odds[51] = ["GH", events["price"]]
                elif events["base"] == 11.5 and events["type_1"] == "Over":
                    odds[52] = ["GH", events["price"]]
                elif events["base"] == 11.5 and events["type_1"] == "Under":
                    odds[53] = ["GH", events["price"]]
                elif events["base"] == 12 and events["type_1"] == "Over":
                    odds[54] = ["GH", events["price"]]
                elif events["base"] == 12 and events["type_1"] == "Under":
                    odds[55] = ["GH", events["price"]]
                elif events["base"] == 12.5 and events["type_1"] == "Over":
                    odds[56] = ["GH", events["price"]]
                elif events["base"] == 12.5 and events["type_1"] == "Under":
                    odds[57] = ["GH", events["price"]]
                elif events["base"] == 13 and events["type_1"] == "Over":
                    odds[58] = ["GH", events["price"]]
                elif events["base"] == 13 and events["type_1"] == "Under":
                    odds[59] = ["GH", events["price"]]
                elif events["base"] == 13.5 and events["type_1"] == "Over":
                    odds[60] = ["GH", events["price"]]
                elif events["base"] == 13.5 and events["type_1"] == "Under":
                    odds[61] = ["GH", events["price"]]
                elif events["base"] == 14 and events["type_1"] == "Over":
                    odds[62] = ["GH", events["price"]]
                elif events["base"] == 14 and events["type_1"] == "Under":
                    odds[63] = ["GH", events["price"]]
                elif events["base"] == 14.5 and events["type_1"] == "Over":
                    odds[64] = ["GH", events["price"]]
                elif events["base"] == 14.5 and events["type_1"] == "Under":
                    odds[65] = ["GH", events["price"]]
        elif market_data["name_template"] == "Corners: Handicap":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Home":
                    odds[66] = ["GH", events["price"]]
                elif events["base"] == -0.5 and events["type_1"] == "Home":
                    odds[67] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Home":
                    odds[68] = ["GH", events["price"]]
                elif events["base"] == -1 and events["type_1"] == "Home":
                    odds[69] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Home":
                    odds[70] = ["GH", events["price"]]
                elif events["base"] == -1.5 and events["type_1"] == "Home":
                    odds[71] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Home":
                    odds[72] = ["GH", events["price"]]
                elif events["base"] == -2 and events["type_1"] == "Home":
                    odds[73] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Home":
                    odds[74] = ["GH", events["price"]]
                elif events["base"] == -2.5 and events["type_1"] == "Home":
                    odds[75] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Home":
                    odds[76] = ["GH", events["price"]]
                elif events["base"] == -3 and events["type_1"] == "Home":
                    odds[77] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Home":
                    odds[78] = ["GH", events["price"]]
                elif events["base"] == -3.5 and events["type_1"] == "Home":
                    odds[79] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Home":
                    odds[80] = ["GH", events["price"]]
                elif events["base"] == -4 and events["type_1"] == "Home":
                    odds[81] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Home":
                    odds[82] = ["GH", events["price"]]
                elif events["base"] == -4.5 and events["type_1"] == "Home":
                    odds[83] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Home":
                    odds[84] = ["GH", events["price"]]
                elif events["base"] == -5 and events["type_1"] == "Home":
                    odds[85] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Home":
                    odds[86] = ["GH", events["price"]]
                elif events["base"] == -5.5 and events["type_1"] == "Home":
                    odds[87] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Away":
                    odds[88] = ["GH", events["price"]]
                elif events["base"] == -0.5 and events["type_1"] == "Away":
                    odds[89] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Away":
                    odds[90] = ["GH", events["price"]]
                elif events["base"] == -1 and events["type_1"] == "Away":
                    odds[91] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Away":
                    odds[92] = ["GH", events["price"]]
                elif events["base"] == -1.5 and events["type_1"] == "Away":
                    odds[93] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Away":
                    odds[94] = ["GH", events["price"]]
                elif events["base"] == -2 and events["type_1"] == "Away":
                    odds[95] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Away":
                    odds[96] = ["GH", events["price"]]
                elif events["base"] == -2.5 and events["type_1"] == "Away":
                    odds[97] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Away":
                    odds[98] = ["GH", events["price"]]
                elif events["base"] == -3 and events["type_1"] == "Away":
                    odds[99] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Away":
                    odds[100] = ["GH", events["price"]]
                elif events["base"] == -3.5 and events["type_1"] == "Away":
                    odds[101] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Away":
                    odds[102] = ["GH", events["price"]]
                elif events["base"] == -4 and events["type_1"] == "Away":
                    odds[103] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Away":
                    odds[104] = ["GH", events["price"]]
                elif events["base"] == -4.5 and events["type_1"] == "Away":
                    odds[105] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Away":
                    odds[106] = ["GH", events["price"]]
                elif events["base"] == -5 and events["type_1"] == "Away":
                    odds[107] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Away":
                    odds[108] = ["GH", events["price"]]
                elif events["base"] == -5.5 and events["type_1"] == "Away":
                    odds[109] = ["GH", events["price"]]
        elif market_data["name_template"] == "Corners: Team 1 Total":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Over":
                    odds[110] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Under":
                    odds[111] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Over":
                    odds[112] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Under":
                    odds[113] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Over":
                    odds[114] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Under":
                    odds[115] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Over":
                    odds[116] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Under":
                    odds[117] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Over":
                    odds[118] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Under":
                    odds[119] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Over":
                    odds[120] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Under":
                    odds[121] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Over":
                    odds[122] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Under":
                    odds[123] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Over":
                    odds[124] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Under":
                    odds[125] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Over":
                    odds[126] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Under":
                    odds[127] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Over":
                    odds[128] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Under":
                    odds[129] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Over":
                    odds[130] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Under":
                    odds[131] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Over":
                    odds[132] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Under":
                    odds[133] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Over":
                    odds[134] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Under":
                    odds[135] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Over":
                    odds[136] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Under":
                    odds[137] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Over":
                    odds[138] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Under":
                    odds[139] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Over":
                    odds[140] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Under":
                    odds[141] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Over":
                    odds[142] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Under":
                    odds[143] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Over":
                    odds[144] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Under":
                    odds[145] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Over":
                    odds[146] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Under":
                    odds[147] = ["GH", events["price"]]
                elif events["base"] == 10 and events["type_1"] == "Over":
                    odds[148] = ["GH", events["price"]]
                elif events["base"] == 10 and events["type_1"] == "Under":
                    odds[149] = ["GH", events["price"]]
                elif events["base"] == 10.5 and events["type_1"] == "Over":
                    odds[150] = ["GH", events["price"]]
                elif events["base"] == 10.5 and events["type_1"] == "Under":
                    odds[151] = ["GH", events["price"]]
        elif market_data["name_template"] == "Corners: Team 2 Total":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Over":
                    odds[152] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Under":
                    odds[153] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Over":
                    odds[154] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Under":
                    odds[155] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Over":
                    odds[156] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Under":
                    odds[157] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Over":
                    odds[158] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Under":
                    odds[159] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Over":
                    odds[160] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Under":
                    odds[161] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Over":
                    odds[162] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Under":
                    odds[163] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Over":
                    odds[164] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Under":
                    odds[165] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Over":
                    odds[166] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Under":
                    odds[167] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Over":
                    odds[168] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Under":
                    odds[169] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Over":
                    odds[170] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Under":
                    odds[171] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Over":
                    odds[172] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Under":
                    odds[173] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Over":
                    odds[174] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Under":
                    odds[175] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Over":
                    odds[176] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Under":
                    odds[177] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Over":
                    odds[178] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Under":
                    odds[179] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Over":
                    odds[180] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Under":
                    odds[181] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Over":
                    odds[182] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Under":
                    odds[183] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Over":
                    odds[184] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Under":
                    odds[185] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Over":
                    odds[186] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Under":
                    odds[187] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Over":
                    odds[188] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Under":
                    odds[189] = ["GH", events["price"]]
                elif events["base"] == 10 and events["type_1"] == "Over":
                    odds[190] = ["GH", events["price"]]
                elif events["base"] == 10 and events["type_1"] == "Under":
                    odds[191] = ["GH", events["price"]]
                elif events["base"] == 10.5 and events["type_1"] == "Over":
                    odds[192] = ["GH", events["price"]]
                elif events["base"] == 10.5 and events["type_1"] == "Under":
                    odds[193] = ["GH", events["price"]]
        elif market_data["name_template"] == "Yellow Cards: Result":
            for _, events in market_data["event"].items():
                if events["type_1"] == "W1":
                    odds[194] = ["GH", events["price"]]
                elif events["type_1"] == "W2":
                    odds[196] = ["GH", events["price"]]
                elif events["type_1"] == "X":
                    odds[198] = ["GH", events["price"]]
        elif market_data["name_template"] == "Yellow Cards: Double Chance":
            for _, events in market_data["event"].items():
                if events["type_1"] == "1X":
                    odds[197] = ["GH", events["price"]]
                elif events["type_1"] == "X2":
                    odds[195] = ["GH", events["price"]]
                elif events["type_1"] == "12":
                    odds[199] = ["GH", events["price"]]
        elif market_data["name_template"] == "Yellow Cards: Total":
            for _, events in market_data["event"].items():
                if events["base"] == 1 and events["type_1"] == "Over":
                    odds[200] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Under":
                    odds[201] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Over":
                    odds[202] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Under":
                    odds[203] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Over":
                    odds[204] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Under":
                    odds[205] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Over":
                    odds[206] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Under":
                    odds[207] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Over":
                    odds[208] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Under":
                    odds[209] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Over":
                    odds[210] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Under":
                    odds[211] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Over":
                    odds[212] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Under":
                    odds[213] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Over":
                    odds[214] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Under":
                    odds[215] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Over":
                    odds[216] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Under":
                    odds[217] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Over":
                    odds[218] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Under":
                    odds[219] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Over":
                    odds[220] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Under":
                    odds[221] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Over":
                    odds[222] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Under":
                    odds[223] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Over":
                    odds[224] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Under":
                    odds[225] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Over":
                    odds[226] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Under":
                    odds[227] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Over":
                    odds[228] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Under":
                    odds[229] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Over":
                    odds[230] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Under":
                    odds[231] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Over":
                    odds[232] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Under":
                    odds[233] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Over":
                    odds[234] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Under":
                    odds[235] = ["GH", events["price"]]
                elif events["base"] == 10 and events["type_1"] == "Over":
                    odds[236] = ["GH", events["price"]]
                elif events["base"] == 10 and events["type_1"] == "Under":
                    odds[237] = ["GH", events["price"]]
                elif events["base"] == 10.5 and events["type_1"] == "Over":
                    odds[238] = ["GH", events["price"]]
                elif events["base"] == 10.5 and events["type_1"] == "Under":
                    odds[239] = ["GH", events["price"]]
        elif market_data["name_template"] == "Yellow Cards: Handicap":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Home":
                    odds[240] = ["GH", events["price"]]
                elif events["base"] == -0.5 and events["type_1"] == "Home":
                    odds[241] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Home":
                    odds[242] = ["GH", events["price"]]
                elif events["base"] == -1 and events["type_1"] == "Home":
                    odds[243] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Home":
                    odds[244] = ["GH", events["price"]]
                elif events["base"] == -1.5 and events["type_1"] == "Home":
                    odds[245] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Home":
                    odds[246] = ["GH", events["price"]]
                elif events["base"] == -2 and events["type_1"] == "Home":
                    odds[247] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Home":
                    odds[248] = ["GH", events["price"]]
                elif events["base"] == -2.5 and events["type_1"] == "Home":
                    odds[249] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Home":
                    odds[250] = ["GH", events["price"]]
                elif events["base"] == -3 and events["type_1"] == "Home":
                    odds[251] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Home":
                    odds[252] = ["GH", events["price"]]
                elif events["base"] == -3.5 and events["type_1"] == "Home":
                    odds[253] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Home":
                    odds[254] = ["GH", events["price"]]
                elif events["base"] == -4 and events["type_1"] == "Home":
                    odds[255] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Home":
                    odds[256] = ["GH", events["price"]]
                elif events["base"] == -4.5 and events["type_1"] == "Home":
                    odds[257] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Home":
                    odds[258] = ["GH", events["price"]]
                elif events["base"] == -5 and events["type_1"] == "Home":
                    odds[259] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Home":
                    odds[260] = ["GH", events["price"]]
                elif events["base"] == -5.5 and events["type_1"] == "Home":
                    odds[261] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Away":
                    odds[262] = ["GH", events["price"]]
                elif events["base"] == -0.5 and events["type_1"] == "Away":
                    odds[263] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Away":
                    odds[264] = ["GH", events["price"]]
                elif events["base"] == -1 and events["type_1"] == "Away":
                    odds[265] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Away":
                    odds[266] = ["GH", events["price"]]
                elif events["base"] == -1.5 and events["type_1"] == "Away":
                    odds[267] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Away":
                    odds[268] = ["GH", events["price"]]
                elif events["base"] == -2 and events["type_1"] == "Away":
                    odds[269] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Away":
                    odds[270] = ["GH", events["price"]]
                elif events["base"] == -2.5 and events["type_1"] == "Away":
                    odds[271] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Away":
                    odds[272] = ["GH", events["price"]]
                elif events["base"] == -3 and events["type_1"] == "Away":
                    odds[273] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Away":
                    odds[274] = ["GH", events["price"]]
                elif events["base"] == -3.5 and events["type_1"] == "Away":
                    odds[275] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Away":
                    odds[276] = ["GH", events["price"]]
                elif events["base"] == -4 and events["type_1"] == "Away":
                    odds[277] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Away":
                    odds[278] = ["GH", events["price"]]
                elif events["base"] == -4.5 and events["type_1"] == "Away":
                    odds[279] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Away":
                    odds[280] = ["GH", events["price"]]
                elif events["base"] == -5 and events["type_1"] == "Away":
                    odds[281] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Away":
                    odds[282] = ["GH", events["price"]]
                elif events["base"] == -5.5 and events["type_1"] == "Away":
                    odds[283] = ["GH", events["price"]]
        elif market_data["name_template"] == "Yellow Cards: Team 1 Total":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Over":
                    odds[284] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Under":
                    odds[285] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Over":
                    odds[286] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Under":
                    odds[287] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Over":
                    odds[288] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Under":
                    odds[289] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Over":
                    odds[290] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Under":
                    odds[291] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Over":
                    odds[292] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Under":
                    odds[293] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Over":
                    odds[294] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Under":
                    odds[295] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Over":
                    odds[296] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Under":
                    odds[297] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Over":
                    odds[298] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Under":
                    odds[299] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Over":
                    odds[300] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Under":
                    odds[301] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Over":
                    odds[302] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Under":
                    odds[303] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Over":
                    odds[304] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Under":
                    odds[305] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Over":
                    odds[306] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Under":
                    odds[307] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Over":
                    odds[308] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Under":
                    odds[309] = ["GH", events["price"]]
        elif market_data["name_template"] == "Yellow Cards: Team 2 Total":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Over":
                    odds[310] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Under":
                    odds[311] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Over":
                    odds[312] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Under":
                    odds[313] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Over":
                    odds[314] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Under":
                    odds[315] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Over":
                    odds[316] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Under":
                    odds[317] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Over":
                    odds[318] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Under":
                    odds[319] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Over":
                    odds[320] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Under":
                    odds[321] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Over":
                    odds[322] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Under":
                    odds[323] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Over":
                    odds[324] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Under":
                    odds[325] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Over":
                    odds[326] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Under":
                    odds[327] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Over":
                    odds[328] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Under":
                    odds[329] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Over":
                    odds[330] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Under":
                    odds[331] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Over":
                    odds[332] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Under":
                    odds[333] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Over":
                    odds[334] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Under":
                    odds[335] = ["GH", events["price"]]
        elif market_data["name_template"] == "Offsides: Result":
            for _, events in market_data["event"].items():
                if events["type_1"] == "W1":
                    odds[336] = ["GH", events["price"]]
                elif events["type_1"] == "W2":
                    odds[338] = ["GH", events["price"]]
                elif events["type_1"] == "X":
                    odds[340] = ["GH", events["price"]]
        elif market_data["name_template"] == "Offsides: Double Chance":
            for _, events in market_data["event"].items():
                if events["type_1"] == "1X":
                    odds[339] = ["GH", events["price"]]
                elif events["type_1"] == "X2":
                    odds[337] = ["GH", events["price"]]
                elif events["type_1"] == "12":
                    odds[341] = ["GH", events["price"]]
        elif market_data["name_template"] == "Offsides: Total":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Over":
                    odds[342] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Under":
                    odds[343] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Over":
                    odds[344] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Under":
                    odds[345] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Over":
                    odds[346] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Under":
                    odds[347] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Over":
                    odds[348] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Under":
                    odds[349] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Over":
                    odds[350] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Under":
                    odds[351] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Over":
                    odds[352] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Under":
                    odds[353] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Over":
                    odds[354] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Under":
                    odds[355] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Over":
                    odds[356] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Under":
                    odds[357] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Over":
                    odds[358] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Under":
                    odds[359] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Over":
                    odds[360] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Under":
                    odds[361] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Over":
                    odds[362] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Under":
                    odds[363] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Over":
                    odds[364] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Under":
                    odds[365] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Over":
                    odds[366] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Under":
                    odds[367] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Over":
                    odds[368] = ["GH", events["price"]]
                elif events["base"] == 7 and events["type_1"] == "Under":
                    odds[369] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Over":
                    odds[370] = ["GH", events["price"]]
                elif events["base"] == 7.5 and events["type_1"] == "Under":
                    odds[371] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Over":
                    odds[372] = ["GH", events["price"]]
                elif events["base"] == 8 and events["type_1"] == "Under":
                    odds[373] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Over":
                    odds[374] = ["GH", events["price"]]
                elif events["base"] == 8.5 and events["type_1"] == "Under":
                    odds[375] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Over":
                    odds[376] = ["GH", events["price"]]
                elif events["base"] == 9 and events["type_1"] == "Under":
                    odds[377] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Over":
                    odds[378] = ["GH", events["price"]]
                elif events["base"] == 9.5 and events["type_1"] == "Under":
                    odds[379] = ["GH", events["price"]]
        elif market_data["name_template"] == "Offsides: Handicap":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Home":
                    odds[380] = ["GH", events["price"]]
                elif events["base"] == -0.5 and events["type_1"] == "Home":
                    odds[381] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Home":
                    odds[382] = ["GH", events["price"]]
                elif events["base"] == -1 and events["type_1"] == "Home":
                    odds[383] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Home":
                    odds[384] = ["GH", events["price"]]
                elif events["base"] == -1.5 and events["type_1"] == "Home":
                    odds[385] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Home":
                    odds[386] = ["GH", events["price"]]
                elif events["base"] == -2 and events["type_1"] == "Home":
                    odds[387] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Home":
                    odds[388] = ["GH", events["price"]]
                elif events["base"] == -2.5 and events["type_1"] == "Home":
                    odds[389] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Home":
                    odds[390] = ["GH", events["price"]]
                elif events["base"] == -3 and events["type_1"] == "Home":
                    odds[391] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Home":
                    odds[392] = ["GH", events["price"]]
                elif events["base"] == -3.5 and events["type_1"] == "Home":
                    odds[393] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Home":
                    odds[394] = ["GH", events["price"]]
                elif events["base"] == -4 and events["type_1"] == "Home":
                    odds[395] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Home":
                    odds[396] = ["GH", events["price"]]
                elif events["base"] == -4.5 and events["type_1"] == "Home":
                    odds[397] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Home":
                    odds[398] = ["GH", events["price"]]
                elif events["base"] == -5 and events["type_1"] == "Home":
                    odds[399] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Home":
                    odds[400] = ["GH", events["price"]]
                elif events["base"] == -5.5 and events["type_1"] == "Home":
                    odds[401] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Away":
                    odds[402] = ["GH", events["price"]]
                elif events["base"] == -0.5 and events["type_1"] == "Away":
                    odds[403] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Away":
                    odds[404] = ["GH", events["price"]]
                elif events["base"] == -1 and events["type_1"] == "Away":
                    odds[405] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Away":
                    odds[406] = ["GH", events["price"]]
                elif events["base"] == -1.5 and events["type_1"] == "Away":
                    odds[407] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Away":
                    odds[408] = ["GH", events["price"]]
                elif events["base"] == -2 and events["type_1"] == "Away":
                    odds[409] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Away":
                    odds[410] = ["GH", events["price"]]
                elif events["base"] == -2.5 and events["type_1"] == "Away":
                    odds[411] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Away":
                    odds[412] = ["GH", events["price"]]
                elif events["base"] == -3 and events["type_1"] == "Away":
                    odds[413] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Away":
                    odds[414] = ["GH", events["price"]]
                elif events["base"] == -3.5 and events["type_1"] == "Away":
                    odds[415] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Away":
                    odds[416] = ["GH", events["price"]]
                elif events["base"] == -4 and events["type_1"] == "Away":
                    odds[417] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Away":
                    odds[418] = ["GH", events["price"]]
                elif events["base"] == -4.5 and events["type_1"] == "Away":
                    odds[419] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Away":
                    odds[420] = ["GH", events["price"]]
                elif events["base"] == -5 and events["type_1"] == "Away":
                    odds[421] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Away":
                    odds[422] = ["GH", events["price"]]
                elif events["base"] == -5.5 and events["type_1"] == "Away":
                    odds[423] = ["GH", events["price"]]
        elif market_data["name_template"] == "Offsides: Team 1 Total":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Over":
                    odds[424] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Under":
                    odds[425] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Over":
                    odds[426] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Under":
                    odds[427] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Over":
                    odds[428] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Under":
                    odds[429] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Over":
                    odds[430] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Under":
                    odds[431] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Over":
                    odds[432] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Under":
                    odds[433] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Over":
                    odds[434] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Under":
                    odds[435] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Over":
                    odds[436] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Under":
                    odds[437] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Over":
                    odds[438] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Under":
                    odds[439] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Over":
                    odds[440] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Under":
                    odds[441] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Over":
                    odds[442] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Under":
                    odds[443] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Over":
                    odds[444] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Under":
                    odds[445] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Over":
                    odds[446] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Under":
                    odds[447] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Over":
                    odds[448] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Under":
                    odds[449] = ["GH", events["price"]]
        elif market_data["name_template"] == "Offsides: Team 2 Total":
            for _, events in market_data["event"].items():
                if events["base"] == 0.5 and events["type_1"] == "Over":
                    odds[450] = ["GH", events["price"]]
                elif events["base"] == 0.5 and events["type_1"] == "Under":
                    odds[451] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Over":
                    odds[452] = ["GH", events["price"]]
                elif events["base"] == 1 and events["type_1"] == "Under":
                    odds[453] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Over":
                    odds[454] = ["GH", events["price"]]
                elif events["base"] == 1.5 and events["type_1"] == "Under":
                    odds[455] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Over":
                    odds[456] = ["GH", events["price"]]
                elif events["base"] == 2 and events["type_1"] == "Under":
                    odds[457] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Over":
                    odds[458] = ["GH", events["price"]]
                elif events["base"] == 2.5 and events["type_1"] == "Under":
                    odds[459] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Over":
                    odds[460] = ["GH", events["price"]]
                elif events["base"] == 3 and events["type_1"] == "Under":
                    odds[461] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Over":
                    odds[462] = ["GH", events["price"]]
                elif events["base"] == 3.5 and events["type_1"] == "Under":
                    odds[463] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Over":
                    odds[464] = ["GH", events["price"]]
                elif events["base"] == 4 and events["type_1"] == "Under":
                    odds[465] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Over":
                    odds[466] = ["GH", events["price"]]
                elif events["base"] == 4.5 and events["type_1"] == "Under":
                    odds[467] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Over":
                    odds[468] = ["GH", events["price"]]
                elif events["base"] == 5 and events["type_1"] == "Under":
                    odds[469] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Over":
                    odds[470] = ["GH", events["price"]]
                elif events["base"] == 5.5 and events["type_1"] == "Under":
                    odds[471] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Over":
                    odds[472] = ["GH", events["price"]]
                elif events["base"] == 6 and events["type_1"] == "Under":
                    odds[473] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Over":
                    odds[474] = ["GH", events["price"]]
                elif events["base"] == 6.5 and events["type_1"] == "Under":
                    odds[475] = ["GH", events["price"]]
    return odds

# df = pd.DataFrame({"market": markets_list})
#
# # Iterate over each file
# for file_name in files:
#     file_path = os.path.join(folder_path, file_name)
#     try:
#         with open(file_path, 'r') as json_file:
#             data = json.load(json_file)
#             event = logic(data)
#             df[df.shape[1]] = event
#     except json.JSONDecodeError as e:
#         print(f"Error decoding JSON in file {file_name}: {e}")
#     except Exception as e:
#         print(f"Error processing file {file_name}: {e}")
#
# df.to_csv("events_dataframe", index=False)
# df.to_pickle("events.pkl")
