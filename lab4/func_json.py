import json


def to_json(data):
    # json.dumps перетворює словник у рядок JSON
    return json.dumps(data, ensure_ascii=False)
