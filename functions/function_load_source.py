import json


def load_source(dir_path=None, level=None, current_level=None):
    with open(f"{dir_path}/{level}.json", "r", encoding="utf-8") as jData:
        jdata = json.load(jData)
        if current_level:
            for key in jdata.keys():
                if key == str(current_level):
                    return jdata[key]
        else:
            return jdata
