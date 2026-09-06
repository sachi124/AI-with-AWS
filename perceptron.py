def logical_perceptron_or(x1, x2):
    """
    preceptron acting as a logical gate
    """ 
    inputs = [x1, x2]
    # lowering the bias threshold lets a single active input to a 1
    weight = [1.0, 1.0]
    bias = -0.5

    weighted_sum = sum(i * w for i, w in zip(inputs, weight)) + bias
    weighted_sum = sum(i * w for i, w in zip(inputs, weight)) + bias
    return 1 if weighted_sum >= 0 else 0

def logical_perceptron_not(x):
    inputs = [x]
    weights = [-1.0]
    bias = 0.5

    weighted_sum = sum(i * w for i, w in zip(inputs, weights)) + bias
    return 1 if weighted_sum >= 0 else 0

def logical_perceptron_and(x1, x2):
    inputs = [x1, x2]
    weights = [1.0, 1.0]
    bias = -1.5

    weighted_sum = sum(i * w for i, w in zip(inputs, weights)) + bias
    return 1 if weighted_sum >= 0 else 0

# Test the logical and gate
print("Truth table for and gate perceptron:")
print("x1 | x2 | Output")
print("-----------------")
for x1, x2 in [(0,0), (0,1), (1,0), (1,1)]:
    output = logical_perceptron_and(x1, x2)
    print(f"{x1} | {x2} | {output}")

# Test the logical or gate
print("Truth table for and gate perceptron:")
print("x1 | x2 | Output")
print("-----------------")
for x1, x2 in [(0,0), (0,1), (1,0), (1,1)]:
    output = logical_perceptron_or(x1, x2)
    print(f"{x1} | {x2} | {output}")

# Test the logical not gate
print("Truth table for and gate perceptron:")
print("x1 | x2 | Output")
print("-----------------")
for x in [0, 1]:
    output = logical_perceptron_not(x)
    print(f"{x} | {output}")