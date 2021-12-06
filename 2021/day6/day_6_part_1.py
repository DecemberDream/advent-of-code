import numpy as np


# unoptimized version
# =============================================================================
# data = open("../../input/day_6_data.txt")
# lines = data.read()
# 
# split_line = lines.split(",")
# status = np.array([int(c) for c in split_line])
# 
# data.close()
# 
# for day in range(80):
#     time_0 = np.where(status == 0)
#     
#     status -= 1
#     
#     if time_0[0].any():
#         to_append = []
#         
#         for i in range(len(time_0[0])):
#             to_append.append([8])
#             
#         status = np.append(status, to_append)
#         status[time_0[0]] = 6
#         
# print(len(status))
# =============================================================================

# slightly optimized version
data = open("../../input/day_6_example.txt")
lines = data.read()

split_line = lines.split(",")
status = np.array([int(c) for c in split_line], dtype=np.uint8)

data.close()

newest_index = len(status) - 1

for day in range(80):
    
    time_0 = np.where(status == 0)
    
    status[:newest_index + 1] -= 1
    
    if time_0[0].any():
        if newest_index == len(status) - 1:
            status = np.append(status, -np.ones(len(time_0[0]), dtype=np.uint8))
        
        for i in range(len(time_0[0])):
            status[newest_index + 1] = 8
            newest_index += 1
            
            if newest_index == len(status) - 1:
                status = np.append(status, -np.ones(len(time_0[0]), dtype=np.uint8))
            
        status[time_0[0]] = 6

print(len(status[:newest_index + 1]))
