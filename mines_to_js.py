# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pandas as pd
import json

mines = pd.read_csv("/home/ttresslar/Downloads/mines.csv")
mines = mines.drop(['uuid', 'genetictyp','morphology','mineraage', 'sizegroup', 'size', 'levelknowl', 'geoknowl'], axis = 1)
mines_js = open("/home/ttresslar/Downloads/mines.js", "w+")
mines_js.write("var mine_pts =")
mines_out = []
for item in mines_dict:
    array = [item['X'],item['Y'],item]
    mines_out.append(array)
json.dump(mines_out, mines_js)
mines_js.close()
