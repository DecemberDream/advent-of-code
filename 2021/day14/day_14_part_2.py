import collections
import numpy as np
from collections import defaultdict


template, insertions = open("../../input/day_14_data.txt").read().split("\n\n")
insertions = insertions.split("\n")
rules = {}
rules_idx = {}

for i, insertion in enumerate(insertions):
    split_insertion = insertion.rstrip().split(" -> ")
    rules[split_insertion[0]] = split_insertion[1]
    rules_idx[split_insertion[0]] = i

n = len(rules)
x = np.zeros(n)
A = np.zeros((n, n))

bigrams = [template[i:i+2] for i in range(len(template) - 1)]

for bigram in bigrams:
    x[rules_idx[bigram]] += 1

for rule in rules_idx:
    r = list(rule)
    r.insert(1, rules[rule])
    
    trigram = "".join(c for c in r)
    
    b1 = trigram[:2]
    b2 = trigram[1:]
    
    col_1 = rules_idx[b1]
    col_2 = rules_idx[b2]
    A[rules_idx[rule], col_1] = 1
    A[rules_idx[rule], col_2] = 1
    
b = np.dot(x, np.linalg.matrix_power(A, 40))

keys = list(rules_idx.keys())

char_dict = defaultdict(int)

for i, bigram in enumerate(keys):
    char_dict[bigram[0]] += int(b[i])

char_dict[template[-1]] += 1

char_count = collections.Counter(char_dict).most_common()
most_common = char_count[0]
least_common = char_count[-1]

print(most_common)
print(least_common)
print("difference", (most_common[1] - least_common[1]))