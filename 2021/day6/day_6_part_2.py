# old solution, too slow and takes too much memory
# =============================================================================
# import numpy as np
# 
# 
# data = open("../../input/day_6_example.txt")
# lines = data.read()
# 
# split_line = lines.split(",")
# status = np.array([int(c) for c in split_line], dtype=np.uint8)
# 
# data.close()
# 
# newest_index = len(status) - 1
# 
# for day in range(80):
#     
#     time_0 = np.where(status == 0)
#     
#     status[:newest_index + 1] -= 1
#     
#     if time_0[0].any():
#         if newest_index == len(status) - 1:
#             status = np.append(status, -np.ones(len(time_0[0]), dtype=np.uint8))
#         
#         for i in range(len(time_0[0])):
#             status[newest_index + 1] = 8
#             newest_index += 1
#             
#             if newest_index == len(status) - 1:
#                 status = np.append(status, -np.ones(len(time_0[0]), dtype=np.uint8))
#             
#         status[time_0[0]] = 6
#     
#     print(day)
# 
# print(len(status[:newest_index + 1]))
# =============================================================================


data = [open("../../input/day_6_data.txt").read().count(str(i)) for i in range(0, 9)]

for day in range(256):
    data[(day + 7) % 9] += data[day % 9]

print(sum(data))
