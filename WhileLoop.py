# Exercise 1: Learning Rate Schedule using While Loops

initial_learning = 0.1
deacy_factor = 0.9
epochs = 5

# Initialize the current learninig rate
current_lr = initial_learning
# Initialize current epoch
current_epoch = 0

# While loop to apply learning rate
while current_epoch < epochs:
    print(f"Epoch {current_epoch + 1}: learning rate = {current_lr:.6f}")
    # Apply decay to the current learning rat
    current_lr *= deacy_factor
    # Incrementthe current epoch
    current_epoch += 1

if abs(current_lr - 0.059049) < 1e-6:
    print("You go the answer")