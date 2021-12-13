from collections import defaultdict


def dfs(current_node, visited):
    if current_node in visited:
        return 0
    if current_node == "end":
        return 1
    if current_node in small_caves:
        visited.add(current_node)
    
    num_of_paths = 0
    
    for node in adjacency_list[current_node]:
        num_of_paths += dfs(node, visited)
        
    visited.discard(current_node)
    
    return num_of_paths

edges = [line.rstrip().split("-") for line in open("../../input/day_12_data.txt").readlines()]
adjacency_list = defaultdict(list)
small_caves = set()

for edge in edges:
    a, b = edge
    
    adjacency_list[a].append(b)
    adjacency_list[b].append(a)
    
    if a.lower() == a:
        small_caves.add(a)
    if b.lower() == b:
        small_caves.add(b)

print(dfs("start", set()))