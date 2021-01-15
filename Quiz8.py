import json

def avg_age():
    f = open("Quiz 8 ages.json")
    ages = json.load(f)
    sum = 0
    L = [ages["Alice"], ages["Bob"], ages["Carol"]]
    for age in L:
        sum = sum + age
    avg = sum / len(L)
    return int(avg)

print("Average age: ", avg_age())