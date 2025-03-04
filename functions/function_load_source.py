import json
from importlib import import_module



def load_json_source(dir_path=None, level=None, current_level=None):
    with open(f"{dir_path}/{level}.json", "r", encoding="utf-8") as jData:
        jdata = json.load(jData)
        if current_level:
            for key in jdata.keys():
                if key == str(current_level):
                    return jdata[key]
        else:
            return jdata


def load_python_file_source(
    dir_path=None,
    module_name=None,
    level=None,
    name_source=None
):
    return import_module(f'.{module_name}', package=f'{dir_path}.{str(level)}').__dict__[name_source]