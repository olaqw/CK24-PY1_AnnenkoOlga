import json


def task() -> float:
    json_file = 'input.json'

    with open(json_file, 'r') as file:
        data = json.load(file)

    res = sum(item['score'] * item['weight'] for item in data if 'score' in item and 'weight' in item)

    return round(res, 3)


print(task())
