import argparse
import json
import ast
parser = argparse.ArgumentParser()
parser.add_argument('filename', type=str,
                   help='optional filename')
args = parser.parse_args()
filename = args.filename
playerfile = "" 
with open(filename,"r") as f:
    next(f)
    playerfile = json.loads(f.read())
artifacts = []
containers = []
for index,item in enumerate(playerfile["worn"]["worn"]):
    
    for attr in item:
        if attr == "contents":
            containers.append(index)
for cont in containers:
    pack = playerfile["worn"]["worn"][cont]["contents"]
    for pocket in pack:
        for item in pack[pocket]:
            if item["contents"] != []:
                for pocketItem in item["contents"]:
                    if "relic_data" in pocketItem and pocketItem["relic_data"] != {}:
                        artifacts.append(pocketItem)
artifacts1 = []
for art in artifacts:
    #print(_,art,"\n")
    for data in art["relic_data"].values():
        if data == 0:
            continue
        artifacts1.append(art)
artifacts2 = [ast.literal_eval(el1) for el1 in set([str(el2) for el2 in artifacts1])]
#https://stackoverflow.com/questions/11741876/getting-unique-values-from-a-list-of-dict
for art in artifacts2:
    if "passive_effects" in art["relic_data"]:
        pEffects = art["relic_data"]["passive_effects"][0]["values"]
        print(art["typeid"])
        for effect in pEffects:
            if len(effect) != 1:
                print(effect)
