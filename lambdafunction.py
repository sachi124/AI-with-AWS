# Raw dataset: list of dictionaries
dataset = [
    {"age": 25, "income": 50000, "city": "NYC"},
    {"age": 40, "income": 90000, "city": "SF"},
    {"age": 35, "income": 65000, "city": "NYC"}
]

# Mapping category strings to numbers manually
city_map = {"NYC": 0, "SF": 1}

# Convert each record to a numerical vector: [age, income, city_code]
vectorize = lambda row: [row["age"], row["income"], city_map[row["city"]]]

feature_matrix = list(map(vectorize, dataset))

print(feature_matrix)
# Output: [[25, 50000, 0], [40, 90000, 1], [35, 65000, 0]]

incomes = [50000, 90000, 65000]

min_val = min(incomes)
max_val = max(incomes)

# Normalize each value to range [0, 1] using lambda
normalize = lambda x: (x - min_val) / (max_val - min_val)

scaled_incomes = list(map(normalize, incomes))

print(scaled_incomes)
# Output: [0.0, 1.0, 0.375]

from functools import reduce

features = [0.5, 0.8, 0.2]  # Inputs (X)
weights  = [0.4, -0.1, 0.9] # Weights (W)
bias = 0.1

# 1. Multiply elements pairwise using zip and map with lambda
products = map(lambda pair: pair[0] * pair[1], zip(features, weights))

# 2. Sum products up and add bias using reduce
dot_product = reduce(lambda a, b: a + b, products) + bias

print(dot_product)
# Output: 0.3 (Calculated: (0.5*0.4) + (0.8*-0.1) + (0.2*0.9) + 0.1)

import math

# ReLU (Rectified Linear Unit): returns max(0, x)
relu = lambda x: max(0.0, x)

# Sigmoid: maps any value to a probability between 0 and 1
sigmoid = lambda x: 1 / (1 + math.exp(-x))

raw_outputs = [-2.5, 0.0, 1.8]

print("ReLU Outputs:   ", list(map(relu, raw_outputs)))
# Output: [0.0, 0.0, 1.8]

print("Sigmoid Outputs:", list(map(lambda x: round(sigmoid(x), 3), raw_outputs)))
# Output: [0.076, 0.5, 0.858]