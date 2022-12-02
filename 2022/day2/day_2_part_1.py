from enum import Enum


class RPS(Enum):
    A = "X"
    B = "Y"
    C = "Z"


class RPS_Pts(Enum):
    X = 1
    Y = 2
    Z = 3


def calculate_points(opp: str, me: str):
    if RPS[opp].value == me:
        return RPS_Pts[me].value + 3
    elif me == "X":
        return RPS_Pts[me].value + 6 if opp == "C" else RPS_Pts[me].value
    elif me == "Y":
        return RPS_Pts[me].value + 6 if opp == "A" else RPS_Pts[me].value
    elif me == "Z":
        return RPS_Pts[me].value + 6 if opp == "B" else RPS_Pts[me].value


filename = "./../../2022_input/day_2_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = file.readlines()
    
total = 0

for step in data:
    line = step.strip().split(" ")
    total += calculate_points(line[0], line[1])

print(total)