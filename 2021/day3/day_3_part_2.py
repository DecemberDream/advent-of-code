import numpy as np


data = open("../../input/day_3_data.txt")
lines = data.readlines()

data_array = []

for line in lines:
    data_array.append(np.array([int(c) for c in line.rstrip("\n")]))

data_array = np.array(data_array)
filtered_oxygen = np.copy(data_array)
filtered_co2 = np.copy(data_array)

rows = len(data_array)

for i in range(len(data_array[0])):
    ones_oxygen = np.sum(filtered_oxygen[:, i])
    ones_co2 = np.sum(filtered_co2[:, i])

    bit_criteria_oxygen = 1 if ones_oxygen / len(filtered_oxygen) >= 0.5 else 0
    bit_criteria_co2 = 0 if ones_co2 / len(filtered_co2) >= 0.5 else 1
    
    if len(filtered_oxygen) > 1:
        filtered_oxygen = filtered_oxygen[filtered_oxygen[:, i] == bit_criteria_oxygen, :]
    if len(filtered_co2) > 1:
        filtered_co2 = filtered_co2[filtered_co2[:, i] == bit_criteria_co2, :]
    
filtered_oxygen = filtered_oxygen[0]
filtered_co2 = filtered_co2[0]

oxygen = filtered_oxygen.dot(1 << np.arange(filtered_oxygen.shape[-1] - 1, -1, -1))
co2 = filtered_co2.dot(1 << np.arange(filtered_co2.shape[-1] - 1, -1, -1))

print(oxygen * co2)

