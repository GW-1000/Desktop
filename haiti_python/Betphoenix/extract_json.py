import pandas as pd
from haiti_python.markets import markets_list
import json
import os
from datetime import datetime

def format_date(my_date):
    # Example ISO 8601 time format
    iso_time =  my_date  #"2024-11-30T13:00:00Z"

    # Convert to datetime object
    dt = datetime.strptime(iso_time, "%Y-%m-%dT%H:%M:%S%z")

    # Convert to Unix timestamp
    unix_timestamp = int(dt.timestamp())

    return unix_timestamp

def logic_bpo(dict_file):
    ours = dict_file["data"]["1"]
    for f_key, f_id in ours.items():
        for s_key, s_id in f_id.items():
            for t_key, t_id in s_id.items():
                data = t_id

    odds = ["", "", "", "", [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        , [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        , [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        , [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []
        , [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [],
            [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], [], []]

    odds[0] = data["tr"]
    odds[1] = format_date(data["tm"])
    odds[2] = data["cms"][0]
    odds[3] = data["cms"][1]

    for m_id, m_data in data["mr"].items():
        for outcomes in m_data["ou"]:
            for outcome_key, outcome_data in outcomes.items():
                if m_data["nm"] == "Winner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "Win1":
                    odds[4] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "Winner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "Win2":
                    odds[6] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "Winner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "Draw":
                    odds[8] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "DoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "1X":
                    odds[7] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "DoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "X2":
                    odds[5] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "DoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "12":
                    odds[9] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersWinner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "Win1":
                    odds[10] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersWinner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "Win2":
                    odds[12] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersWinner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "Draw":
                    odds[14] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersDoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "1X":
                    odds[13] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersDoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "X2":
                    odds[11] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersDoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "12":
                    odds[15] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersTotal" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["nm"] == "Over" and m_data["vl"] == "2.5":
                        odds[16] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2.5":
                        odds[17] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3":
                        odds[18] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3":
                        odds[19] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3.5":
                        odds[20] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3.5":
                        odds[21] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4":
                        odds[22] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4":
                        odds[23] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4.5":
                        odds[24] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4.5":
                        odds[25] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5":
                        odds[26] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5":
                        odds[27] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5.5":
                        odds[28] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5.5":
                        odds[29] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6":
                        odds[30] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6":
                        odds[31] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6.5":
                        odds[32] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6.5":
                        odds[33] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7":
                        odds[34] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7":
                        odds[35] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7.5":
                        odds[36] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7.5":
                        odds[37] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8":
                        odds[38] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8":
                        odds[39] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8.5":
                        odds[40] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8.5":
                        odds[41] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9":
                        odds[42] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9":
                        odds[43] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9.5":
                        odds[44] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9.5":
                        odds[45] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "10":
                        odds[46] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "10":
                        odds[47] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "10.5":
                        odds[48] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "10.5":
                        odds[49] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "11":
                        odds[50] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "11":
                        odds[51] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "11.5":
                        odds[52] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "11.5":
                        odds[53] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "12":
                        odds[54] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "12":
                        odds[55] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "12.5":
                        odds[56] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "12.5":
                        odds[57] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "13":
                        odds[58] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "13":
                        odds[59] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "13.5":
                        odds[60] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "13.5":
                        odds[61] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "14":
                        odds[62] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "14":
                        odds[63] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "14.5":
                        odds[64] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "14.5":
                        odds[65] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersHandicap" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["vl"] == "+0.5" and outcome_data["nm"] == "Win1":
                        odds[66] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-0.5" and outcome_data["nm"] == "Win1":
                        odds[67] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1" and outcome_data["nm"] == "Win1":
                        odds[68] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1" and outcome_data["nm"] == "Win1":
                        odds[69] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1.5" and outcome_data["nm"] == "Win1":
                        odds[70] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1.5" and outcome_data["nm"] == "Win1":
                        odds[71] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2" and outcome_data["nm"] == "Win1":
                        odds[72] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2" and outcome_data["nm"] == "Win1":
                        odds[73] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2.5" and outcome_data["nm"] == "Win1":
                        odds[74] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2.5" and outcome_data["nm"] == "Win1":
                        odds[75] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3" and outcome_data["nm"] == "Win1":
                        odds[76] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3" and outcome_data["nm"] == "Win1":
                        odds[77] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3.5" and outcome_data["nm"] == "Win1":
                        odds[78] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3.5" and outcome_data["nm"] == "Win1":
                        odds[79] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4" and outcome_data["nm"] == "Win1":
                        odds[80] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4" and outcome_data["nm"] == "Win1":
                        odds[81] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4.5" and outcome_data["nm"] == "Win1":
                        odds[82] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4.5" and outcome_data["nm"] == "Win1":
                        odds[83] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5" and outcome_data["nm"] == "Win1":
                        odds[84] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5" and outcome_data["nm"] == "Win1":
                        odds[85] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5.5" and outcome_data["nm"] == "Win1":
                        odds[86] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5.5" and outcome_data["nm"] == "Win1":
                        odds[87] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+0.5" and outcome_data["nm"] == "Win2":
                        odds[88] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-0.5" and outcome_data["nm"] == "Win2":
                        odds[89] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1" and outcome_data["nm"] == "Win2":
                        odds[90] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1" and outcome_data["nm"] == "Win2":
                        odds[91] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1.5" and outcome_data["nm"] == "Win2":
                        odds[92] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1.5" and outcome_data["nm"] == "Win2":
                        odds[93] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2" and outcome_data["nm"] == "Win2":
                        odds[94] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2" and outcome_data["nm"] == "Win2":
                        odds[95] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2.5" and outcome_data["nm"] == "Win2":
                        odds[96] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2.5" and outcome_data["nm"] == "Win2":
                        odds[97] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3" and outcome_data["nm"] == "Win2":
                        odds[98] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3" and outcome_data["nm"] == "Win2":
                        odds[99] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3.5" and outcome_data["nm"] == "Win2":
                        odds[100] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3.5" and outcome_data["nm"] == "Win2":
                        odds[101] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4" and outcome_data["nm"] == "Win2":
                        odds[102] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4" and outcome_data["nm"] == "Win2":
                        odds[103] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4.5" and outcome_data["nm"] == "Win2":
                        odds[104] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4.5" and outcome_data["nm"] == "Win2":
                        odds[105] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5" and outcome_data["nm"] == "Win2":
                        odds[106] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5" and outcome_data["nm"] == "Win2":
                        odds[107] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5.5" and outcome_data["nm"] == "Win2":
                        odds[108] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5.5" and outcome_data["nm"] == "Win2":
                        odds[109] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersTeam1Total" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["nm"] == "Over" and m_data["vl"] == "0.5":
                        odds[110] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "0.5":
                        odds[111] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1":
                        odds[112] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1":
                        odds[113] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1.5":
                        odds[114] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1.5":
                        odds[115] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2":
                        odds[116] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2":
                        odds[117] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2.5":
                        odds[118] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2.5":
                        odds[119] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3":
                        odds[120] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3":
                        odds[121] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3.5":
                        odds[122] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3.5":
                        odds[123] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4":
                        odds[124] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4":
                        odds[125] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4.5":
                        odds[126] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4.5":
                        odds[127] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5":
                        odds[128] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5":
                        odds[129] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5.5":
                        odds[130] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5.5":
                        odds[131] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6":
                        odds[132] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6":
                        odds[133] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6.5":
                        odds[134] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6.5":
                        odds[135] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7":
                        odds[136] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7":
                        odds[137] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7.5":
                        odds[138] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7.5":
                        odds[139] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8":
                        odds[140] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8":
                        odds[141] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8.5":
                        odds[142] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8.5":
                        odds[143] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9":
                        odds[144] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9":
                        odds[145] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9.5":
                        odds[146] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9.5":
                        odds[147] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "10":
                        odds[148] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "10":
                        odds[149] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "10.5":
                        odds[150] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "10.5":
                        odds[151] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "CornersTeam2Total" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["nm"] == "Over" and m_data["vl"] == "0.5":
                        odds[152] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "0.5":
                        odds[153] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1":
                        odds[154] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1":
                        odds[155] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1.5":
                        odds[156] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1.5":
                        odds[157] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2":
                        odds[158] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2":
                        odds[159] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2.5":
                        odds[160] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2.5":
                        odds[161] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3":
                        odds[162] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3":
                        odds[163] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3.5":
                        odds[164] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3.5":
                        odds[165] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4":
                        odds[166] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4":
                        odds[167] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4.5":
                        odds[168] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4.5":
                        odds[169] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5":
                        odds[170] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5":
                        odds[171] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5.5":
                        odds[172] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5.5":
                        odds[173] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6":
                        odds[174] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6":
                        odds[175] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6.5":
                        odds[176] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6.5":
                        odds[177] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7":
                        odds[178] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7":
                        odds[179] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7.5":
                        odds[180] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7.5":
                        odds[181] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8":
                        odds[182] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8":
                        odds[183] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8.5":
                        odds[184] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8.5":
                        odds[185] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9":
                        odds[186] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9":
                        odds[187] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9.5":
                        odds[188] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9.5":
                        odds[189] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "10":
                        odds[190] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "10":
                        odds[191] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "10.5":
                        odds[192] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "10.5":
                        odds[193] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsWinner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data[
                    "nm"] == "Win1":
                    odds[194] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsWinner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data[
                    "nm"] == "Win2":
                    odds[196] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsWinner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data[
                    "nm"] == "Draw":
                    odds[198] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsDoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data[
                    "nm"] == "1X":
                    odds[197] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsDoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data[
                    "nm"] == "X2":
                    odds[195] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsDoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data[
                    "nm"] == "12":
                    odds[199] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsTotal" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["nm"] == "Over" and m_data["vl"] == "1":
                        odds[200] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1":
                        odds[201] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1.5":
                        odds[202] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1.5":
                        odds[203] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2":
                        odds[204] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2":
                        odds[205] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2.5":
                        odds[206] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2.5":
                        odds[207] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3":
                        odds[208] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3":
                        odds[209] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3.5":
                        odds[210] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3.5":
                        odds[211] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4":
                        odds[212] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4":
                        odds[213] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4.5":
                        odds[214] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4.5":
                        odds[215] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5":
                        odds[216] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5":
                        odds[217] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5.5":
                        odds[218] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5.5":
                        odds[219] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6":
                        odds[220] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6":
                        odds[221] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6.5":
                        odds[222] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6.5":
                        odds[223] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7":
                        odds[224] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7":
                        odds[225] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7.5":
                        odds[226] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7.5":
                        odds[227] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8":
                        odds[228] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8":
                        odds[229] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8.5":
                        odds[230] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8.5":
                        odds[231] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9":
                        odds[232] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9":
                        odds[233] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9.5":
                        odds[234] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9.5":
                        odds[235] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "10":
                        odds[236] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "10":
                        odds[237] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "10.5":
                        odds[238] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "10.5":
                        odds[239] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsHandicap" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["vl"] == "+0.5" and outcome_data["nm"] == "Win1":
                        odds[240] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-0.5" and outcome_data["nm"] == "Win1":
                        odds[241] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1" and outcome_data["nm"] == "Win1":
                        odds[242] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1" and outcome_data["nm"] == "Win1":
                        odds[243] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1.5" and outcome_data["nm"] == "Win1":
                        odds[244] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1.5" and outcome_data["nm"] == "Win1":
                        odds[245] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2" and outcome_data["nm"] == "Win1":
                        odds[246] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2" and outcome_data["nm"] == "Win1":
                        odds[247] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2.5" and outcome_data["nm"] == "Win1":
                        odds[248] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2.5" and outcome_data["nm"] == "Win1":
                        odds[249] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3" and outcome_data["nm"] == "Win1":
                        odds[250] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3" and outcome_data["nm"] == "Win1":
                        odds[251] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3.5" and outcome_data["nm"] == "Win1":
                        odds[252] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3.5" and outcome_data["nm"] == "Win1":
                        odds[253] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4" and outcome_data["nm"] == "Win1":
                        odds[254] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4" and outcome_data["nm"] == "Win1":
                        odds[255] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4.5" and outcome_data["nm"] == "Win1":
                        odds[256] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4.5" and outcome_data["nm"] == "Win1":
                        odds[257] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5" and outcome_data["nm"] == "Win1":
                        odds[258] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5" and outcome_data["nm"] == "Win1":
                        odds[259] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5.5" and outcome_data["nm"] == "Win1":
                        odds[260] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5.5" and outcome_data["nm"] == "Win1":
                        odds[261] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+0.5" and outcome_data["nm"] == "Win2":
                        odds[262] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-0.5" and outcome_data["nm"] == "Win2":
                        odds[263] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1" and outcome_data["nm"] == "Win2":
                        odds[264] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1" and outcome_data["nm"] == "Win2":
                        odds[265] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1.5" and outcome_data["nm"] == "Win2":
                        odds[266] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1.5" and outcome_data["nm"] == "Win2":
                        odds[267] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2" and outcome_data["nm"] == "Win2":
                        odds[268] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2" and outcome_data["nm"] == "Win2":
                        odds[269] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2.5" and outcome_data["nm"] == "Win2":
                        odds[270] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2.5" and outcome_data["nm"] == "Win2":
                        odds[271] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3" and outcome_data["nm"] == "Win2":
                        odds[272] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3" and outcome_data["nm"] == "Win2":
                        odds[273] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3.5" and outcome_data["nm"] == "Win2":
                        odds[274] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3.5" and outcome_data["nm"] == "Win2":
                        odds[275] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4" and outcome_data["nm"] == "Win2":
                        odds[276] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4" and outcome_data["nm"] == "Win2":
                        odds[277] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4.5" and outcome_data["nm"] == "Win2":
                        odds[278] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4.5" and outcome_data["nm"] == "Win2":
                        odds[279] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5" and outcome_data["nm"] == "Win2":
                        odds[280] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5" and outcome_data["nm"] == "Win2":
                        odds[281] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5.5" and outcome_data["nm"] == "Win2":
                        odds[282] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5.5" and outcome_data["nm"] == "Win2":
                        odds[283] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsTeam1Total" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["nm"] == "Over" and m_data["vl"] == "0.5":
                        odds[284] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "0.5":
                        odds[285] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1":
                        odds[286] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1":
                        odds[287] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1.5":
                        odds[288] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1.5":
                        odds[289] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2":
                        odds[290] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2":
                        odds[291] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2.5":
                        odds[292] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2.5":
                        odds[293] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3":
                        odds[294] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3":
                        odds[295] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3.5":
                        odds[296] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3.5":
                        odds[297] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4":
                        odds[298] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4":
                        odds[299] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4.5":
                        odds[300] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4.5":
                        odds[301] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5":
                        odds[302] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5":
                        odds[303] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5.5":
                        odds[304] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5.5":
                        odds[305] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6":
                        odds[306] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6":
                        odds[307] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6.5":
                        odds[308] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6.5":
                        odds[309] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "YellowCardsTeam2Total" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["nm"] == "Over" and m_data["vl"] == "0.5":
                        odds[310] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "0.5":
                        odds[311] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1":
                        odds[312] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1":
                        odds[313] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1.5":
                        odds[314] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1.5":
                        odds[315] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2":
                        odds[316] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2":
                        odds[317] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2.5":
                        odds[318] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2.5":
                        odds[319] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3":
                        odds[320] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3":
                        odds[321] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3.5":
                        odds[322] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3.5":
                        odds[323] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4":
                        odds[324] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4":
                        odds[325] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4.5":
                        odds[326] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4.5":
                        odds[327] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5":
                        odds[328] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5":
                        odds[329] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5.5":
                        odds[330] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5.5":
                        odds[331] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6":
                        odds[332] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6":
                        odds[333] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6.5":
                        odds[334] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6.5":
                        odds[335] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesWinner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "Win1":
                    odds[336] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesWinner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "Win2":
                    odds[338] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesWinner3Ways" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "Draw":
                    odds[340] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesDoubleChance" and m_data["op"] == True and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "1X":
                    odds[339] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesDoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "X2":
                    odds[337] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesDoubleChance" and m_data["op"] == True and m_data["pn"] == "MainTime" and outcome_data["nm"] == "12":
                    odds[341] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesTotal" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["nm"] == "Over" and m_data["vl"] == "0.5":
                        odds[342] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "0.5":
                        odds[343] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1":
                        odds[344] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1":
                        odds[345] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1.5":
                        odds[346] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1.5":
                        odds[347] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2":
                        odds[348] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2":
                        odds[349] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2.5":
                        odds[350] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2.5":
                        odds[351] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3":
                        odds[352] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3":
                        odds[353] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3.5":
                        odds[354] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3.5":
                        odds[355] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4":
                        odds[356] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4":
                        odds[357] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4.5":
                        odds[358] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4.5":
                        odds[359] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5":
                        odds[360] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5":
                        odds[361] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5.5":
                        odds[362] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5.5":
                        odds[363] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6":
                        odds[364] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6":
                        odds[365] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6.5":
                        odds[366] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6.5":
                        odds[367] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7":
                        odds[368] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7":
                        odds[369] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "7.5":
                        odds[370] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "7.5":
                        odds[371] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8":
                        odds[372] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8":
                        odds[373] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "8.5":
                        odds[374] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "8.5":
                        odds[375] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9":
                        odds[376] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9":
                        odds[377] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "9.5":
                        odds[378] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "9.5":
                        odds[379] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesHandicap" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["vl"] == "+0.5" and outcome_data["nm"] == "Win1":
                        odds[380] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-0.5" and outcome_data["nm"] == "Win1":
                        odds[381] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1" and outcome_data["nm"] == "Win1":
                        odds[382] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1" and outcome_data["nm"] == "Win1":
                        odds[383] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1.5" and outcome_data["nm"] == "Win1":
                        odds[384] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1.5" and outcome_data["nm"] == "Win1":
                        odds[385] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2" and outcome_data["nm"] == "Win1":
                        odds[386] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2" and outcome_data["nm"] == "Win1":
                        odds[387] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2.5" and outcome_data["nm"] == "Win1":
                        odds[388] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2.5" and outcome_data["nm"] == "Win1":
                        odds[389] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3" and outcome_data["nm"] == "Win1":
                        odds[390] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3" and outcome_data["nm"] == "Win1":
                        odds[391] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3.5" and outcome_data["nm"] == "Win1":
                        odds[392] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3.5" and outcome_data["nm"] == "Win1":
                        odds[393] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4" and outcome_data["nm"] == "Win1":
                        odds[394] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4" and outcome_data["nm"] == "Win1":
                        odds[395] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4.5" and outcome_data["nm"] == "Win1":
                        odds[396] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4.5" and outcome_data["nm"] == "Win1":
                        odds[397] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5" and outcome_data["nm"] == "Win1":
                        odds[398] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5" and outcome_data["nm"] == "Win1":
                        odds[399] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5.5" and outcome_data["nm"] == "Win1":
                        odds[400] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5.5" and outcome_data["nm"] == "Win1":
                        odds[401] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+0.5" and outcome_data["nm"] == "Win2":
                        odds[402] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-0.5" and outcome_data["nm"] == "Win2":
                        odds[403] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1" and outcome_data["nm"] == "Win2":
                        odds[404] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1" and outcome_data["nm"] == "Win2":
                        odds[405] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+1.5" and outcome_data["nm"] == "Win2":
                        odds[406] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-1.5" and outcome_data["nm"] == "Win2":
                        odds[407] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2" and outcome_data["nm"] == "Win2":
                        odds[408] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2" and outcome_data["nm"] == "Win2":
                        odds[409] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+2.5" and outcome_data["nm"] == "Win2":
                        odds[410] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-2.5" and outcome_data["nm"] == "Win2":
                        odds[411] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3" and outcome_data["nm"] == "Win2":
                        odds[412] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3" and outcome_data["nm"] == "Win2":
                        odds[413] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+3.5" and outcome_data["nm"] == "Win2":
                        odds[414] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-3.5" and outcome_data["nm"] == "Win2":
                        odds[415] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4" and outcome_data["nm"] == "Win2":
                        odds[416] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4" and outcome_data["nm"] == "Win2":
                        odds[417] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+4.5" and outcome_data["nm"] == "Win2":
                        odds[418] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-4.5" and outcome_data["nm"] == "Win2":
                        odds[419] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5" and outcome_data["nm"] == "Win2":
                        odds[420] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5" and outcome_data["nm"] == "Win2":
                        odds[421] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "+5.5" and outcome_data["nm"] == "Win2":
                        odds[422] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["vl"] == "-5.5" and outcome_data["nm"] == "Win2":
                        odds[423] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesTeam1Total" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["nm"] == "Over" and m_data["vl"] == "0.5":
                        odds[424] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "0.5":
                        odds[425] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1":
                        odds[426] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1":
                        odds[427] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1.5":
                        odds[428] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1.5":
                        odds[429] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2":
                        odds[430] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2":
                        odds[431] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2.5":
                        odds[432] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2.5":
                        odds[433] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3":
                        odds[434] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3":
                        odds[435] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3.5":
                        odds[436] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3.5":
                        odds[437] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4":
                        odds[438] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4":
                        odds[439] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4.5":
                        odds[440] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4.5":
                        odds[441] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5":
                        odds[442] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5":
                        odds[443] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5.5":
                        odds[444] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5.5":
                        odds[445] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6":
                        odds[446] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6":
                        odds[447] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6.5":
                        odds[448] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6.5":
                        odds[449] = ["BPO", outcome_data["kf"]]
                elif m_data["nm"] == "OffsidesTeam2Total" and m_data["op"] == True and m_data["pn"] == "MainTime":
                    if outcome_data["nm"] == "Over" and m_data["vl"] == "0.5":
                        odds[450] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "0.5":
                        odds[451] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1":
                        odds[452] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1":
                        odds[453] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "1.5":
                        odds[454] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "1.5":
                        odds[455] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2":
                        odds[456] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2":
                        odds[457] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "2.5":
                        odds[458] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "2.5":
                        odds[459] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3":
                        odds[460] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3":
                        odds[461] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "3.5":
                        odds[462] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "3.5":
                        odds[463] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4":
                        odds[464] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4":
                        odds[465] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "4.5":
                        odds[466] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "4.5":
                        odds[467] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5":
                        odds[468] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5":
                        odds[469] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "5.5":
                        odds[470] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "5.5":
                        odds[471] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6":
                        odds[472] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6":
                        odds[473] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Over" and m_data["vl"] == "6.5":
                        odds[474] = ["BPO", outcome_data["kf"]]
                    elif outcome_data["nm"] == "Under" and m_data["vl"] == "6.5":
                        odds[475] = ["BPO", outcome_data["kf"]]
    return odds

# # Path to your folder containing JSON files
# folder_path = 'C:/Users/daniel/PycharmProjects/placerbot/testingground/eventresults'
#
# # List all files in the folder
# files = os.listdir(folder_path)
#
# df = pd.DataFrame({"market": markets_list})
#
# for file_name in files:
#     file_path = os.path.join(folder_path, file_name)
#     try:
#         with open(file_path, 'r') as json_file:
#             data = json.load(json_file)
#             event = logic_bpo(data)
#             df[df.shape[1]] = event
#     except json.JSONDecodeError as e:
#         print(f"Error decoding JSON in file {file_name}: {e}")
#     except Exception as e:
#         print(f"Error processing file {file_name}: {e}")
#
# df.to_csv("events_dataframe", index=False)
# df.to_pickle("events.pkl")



