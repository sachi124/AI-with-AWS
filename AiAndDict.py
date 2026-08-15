# Define Dictionary
model_accuracies = {'ResNet': 0.91,
                    'AlexNet': 0.85,
                    'VGG': 0.88,
                    'Inception': 0.92
                    }

# Calculate the average accuracy
average_accuracy = sum(model_accuracies.values()) / len(model_accuracies)

# find the best model
best_model = max(model_accuracies, key=model_accuracies.get)

# Add a new Model
new_model = 'Mobilenet'
new_accuracy = 0.89
model_accuracies[new_model] = new_accuracy

# Check the results
model_accuracies_solution = {'ResNet': 0.91,
                            'AlexNet': 0.85,
                            'VGG': 0.88,
                            'Inception': 0.92,
                            'Mobilenet': 0.89
                            }

if model_accuracies == model_accuracies_solution:
    print("The model accuracies are correct!")
else:
    print("The model accuracies are incorrect!")

print(f"The average accuracy of the models is: {average_accuracy:.2f}.") 