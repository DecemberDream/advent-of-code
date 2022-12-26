import numpy as np
from collections import deque


def a_star(start: tuple, goal: tuple, h: callable, heights: np.ndarray):
    # The set of discovered nodes that may need to be (re-)expanded.
    # Initially, only the start node is known.
    # This is usually implemented as a min-heap or priority queue rather than a hash-set.
    open_set = {start}

    # For node n, came_from[n] is the node immediately preceding it on the cheapest path from start
    # to n currently known.
    came_from = {}  # an empty map

    # For node n, g_score[n] is the cost of the cheapest path from start to n currently known.
    g_score = {start: 0}  # map with default value of Infinity

    # For node n, f_score[n] = g_score[n] + h(n). f_score[n] represents our current best guess as to
    # how cheap a path could be from start to finish if it goes through n.
    f_score = {start: h(start, goal)}  # map with default value of Infinity

    while open_set:  # is not empty:
        # This operation can occur in O(Log(N)) time if open_set is a min-heap or a priority queue
        # The node in open_set having the lowest f_score[] value
        sorted_f_scores = dict(sorted(f_score.items(), key=lambda item: item[1]))

        for k, v in sorted_f_scores.items():
            if k in open_set:
                current = k
                break

        if current == goal:
            return reconstruct_path(came_from, current)

        open_set.remove(current)

        for neighbor in get_neighbors(current):
            if not is_valid(heights[current], heights[neighbor]):
                continue

            # d(current,neighbor) is the weight of the edge from current to neighbor
            # tentative_g_score is the distance from start to the neighbor through current
            tentative_g_score = g_score[current] + 1  # d(current, neighbor)
            if neighbor not in g_score or tentative_g_score < g_score[neighbor]:
                # This path to neighbor is better than any previous one. Record it!
                came_from[neighbor] = current
                g_score[neighbor] = tentative_g_score
                f_score[neighbor] = tentative_g_score + h(neighbor, goal)

                if neighbor not in open_set:
                    open_set.add(neighbor)

    # Open set is empty but goal was never reached
    return None


def get_neighbors(current: tuple):
    x, y = current
    return [(x, y-1), (x+1, y), (x, y+1), (x-1, y)]


def is_valid(current_height: int, next_height: int) -> bool:
    return next_height <= current_height + 1


def reconstruct_path(came_from: dict, current: tuple):
    total_path = deque()

    while current in came_from.keys():
        current = came_from[current]
        total_path.appendleft(current)

    return total_path


filename = "./../../2022_input/day_12_data.txt"

with open(filename, "r", encoding="utf-8") as file:
    data = file.read().splitlines()

num_array = []

for line in data:
    num_array.append([ord(x)-ord("a") for x in list(line)])

grid = np.array(num_array)
grid = np.pad(grid, pad_width=1, mode="constant", constant_values=ord("A"))
S = list(zip(*np.where(grid == -14)))[0]
E = list(zip(*np.where(grid == -28)))[0]

grid[S] = 0
grid[E] = ord("z")-ord("a")

res = a_star(S, E, lambda x, y: abs(x[1] - x[0]) + abs(y[1] - y[0]), grid)
print(len(res))
