# Day-2 of learning AI with Python

# the initial learning rate of model
learning_rate = 0.01
# the initial loss of the training mmodel
training_loss = 0.8

# use the multiplication assignment opertaor to decrease the learning rate vaiaable by 10%
learning_rate *= 0.9

# Notebook grading
if learning_rate == 0.001*0.9:
    print("The learning rate is decreased by 10%")
elif learning_rate == 0.01 * 1.1:
    print("The learning rate is increased by 10%")
else:
    print("The learning rate in unchanged")

# Use the addition assignment operator to add a small value (0.02) due to noisy data
training_loss += 0.02

# Notebook grading
if training_loss== 0.8+0.02:
    print("The training loss is increaded by 0.02 due to noisy data")
elif training_loss ==0.8-0.02:
    print("The training loss is decreased by 0.02 due to noisy data")
else:
    print("The training loss is unchanged")

# use the multiplication assignment operator to decrease the training_loss by 5% to account for regularization
training_loss *= 0.95

if training_loss == (0.8+0.02)*1.05*0.95:
    print("The training loss is decreased by 5% due to regularization")
elif training_loss == (0.8+0.02)*1.05:
    print("The training loss is increased by 5% due to regularization")
else:
    print("The training loss is unchanged due to regularization")

# Use the subtraction assignment operator to decrease the training_loss by 0.05
training_loss -= 0.05

if training_loss == (0.8+0.02)*1.05*0.95-0.05:
    print("the training loss is decreased by 0.05")
else:
    print("The training loss is unchanged")


# Initial learninig rate
learning_rate = 1e-3 

# Update it by decreasing it by 10%
learning_rate *=0.9
print(f"Updated learning rate: {learning_rate}")