from enum import Enum


class RPS(Enum):
    A = "X"
    B = "Y"
    C = "Z"


class RPS_Pts(Enum):
    X = 1
    Y = 2
    Z = 3


class Defeats(Enum):
    A = "Z"
    C = "Y"
    B = "X"


class Wins(Enum):
    C = "X"
    B = "Z"
    A = "Y"


def calculate_points(opp: str, me: str):
    if me == "X": # lose
        return RPS_Pts[Defeats[opp].value].value
    elif me == "Y": # draw
        return RPS_Pts[RPS[opp].value].value + 3
    elif me == "Z": # win
        return RPS_Pts[Wins[opp].value].value + 6


filename = "./../../2022_input/day_2_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = file.readlines()
    
total = 0

for step in data:
    line = step.strip().split(" ")
    total += calculate_points(line[0], line[1])

print(total)