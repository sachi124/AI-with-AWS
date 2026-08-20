# Model parameters
parameters = [0.5, 1.5, -0.5]
# Corresponding gradients
gradients = [0.1, -0.2, 0.05]
# Learning rate
learning_rate = 0.01

# For loop to update each parameter
for i in range(len(parameters)):
    parameters[i] -= learning_rate * gradients[i]
    print(f"Updated parameter {i + 1}: {parameters[i]:.5f}")

# Notebook grading
if parameters == [0.499, 1.502, -0.5005]:
    print("Nice work!")
else:
    print("Not quite. Check your parameter updates.")