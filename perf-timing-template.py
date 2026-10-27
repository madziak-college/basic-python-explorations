import time

start_time = time.time()
# do task here using approach 1
approach1_time = time.time() - start_time

start_time = time.time()
# do task here using approach 2
approach2_time = time.time() - start_time

# and then compare and/or output the timing of the two approaches..
print(f"Approach 1 time: {approach1_time:.6f} seconds")
