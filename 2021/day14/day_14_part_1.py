import collections


template, insertions = open("../../input/day_14_data.txt").read().split("\n\n")
template = list(template)
insertions = insertions.split("\n")
rules = {}

for i, insertion in enumerate(insertions):
    split_insertion = insertion.rstrip().split(" -> ")
    rules[split_insertion[0]] = split_insertion[1]

for step in range(10):
    i = 0
    
    while i < len(template) - 1:
        current = template[i] + template[i + 1]
        
        if current in rules:
            template.insert(i + 1, rules[current])
            i += 1
            
        i += 1
    
char_count = collections.Counter(template).most_common()

most_common = char_count[0]
least_common = char_count[-1]

print(most_common)
print(least_common)
print("difference", most_common[1] - least_common[1])