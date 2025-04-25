import json
# TODO решите задачу
def task() -> float:
    sum_ = 0
    with open('input.json', 'r') as f:
        data = json.load(f)
    for i in data:
        sum_ += i['score']*i['weight']
    return round(sum_, 3)

print(task())
