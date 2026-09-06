import time

# Sample data
numbers = list(range(1, 10000000))
threshold = 500000

# Conventional for-loop for map equivalent (square of each number)
start_time = time.time()
squares_conventional = []
for num in numbers:
    squares_conventional.append(num ** 2)
end_time = time.time()
conventional_map_time = end_time - start_time

# Using Map
start_time = time.time()
squares_map = list(map(lambda x: x ** 2, numbers))
end_time = time.time()
map_time = end_time - start_time

# Conventional for-loop for filter equivalent (numbers greater than threshold)
start_time = time.time()
filtered_conventional = []
for num in numbers:
    if num > threshold:
        filtered_conventional.append(num)
end_time = time.time()
conventional_filter_time = end_time - start_time

# Using filter
start_time = time.time()
fintered_filter = list(filter(lambda x: x > threshold, numbers))
end_time = time.time()
filter_time = end_time - start_time

# Printing the results
print(f"Conventional for-loop (map equivalent) took: {conventional_map_time:.6f} seconds")
print(f"Map function took: {map_time:.6f} seconds")
print(f"Conventional for-loop (filter equivalent) took: {conventional_filter_time:.6f} seconds")
print(f"Filter function took: {filter_time:.6f} seconds")