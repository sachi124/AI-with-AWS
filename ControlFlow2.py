model_performance = {
    'Experiment 1': {
        'Model A': 0.85, 'Model B': 0.9, 'Model C': 0.88, 'Model D': 0.92, 'Model E': 0.87
    },
    'Experiment 2': {
        'Model A': 0.91, 'Model B': 0.89, 'Model C': 0.93, 'Model D': 0.94, 'Model E': 0.86
    },
    'Experiment 3': {
        'Model A': 0.87, 'Model B': 0.9, 'Model C': 0.86, 'Model D': 0.95, 'Model E': 0.84
    },
    'Experiment 4': {
        'Model A': 0.88, 'Model B': 0.85, 'Model C': 0.89, 'Model D': 0.93, 'Model E': 0.87
    },
    'Experiment 5': {
        'Model A': 0.89, 'Model B': 0.88, 'Model C': 0.91, 'Model D': 0.92, 'Model E': 0.85
    },
    'Experiment 6': {
        'Model A': 0.9, 'Model B': 0.87, 'Model C': 0.92, 'Model D': 0.91, 'Model E': 0.88
    },
    'Experiment 7': {
        'Model A': 0.86, 'Model B': 0.89, 'Model C': 0.85, 'Model D': 0.94, 'Model E': 0.89
    },
    'Experiment 8': {
        'Model A': 0.91, 'Model B': 0.92, 'Model C': 0.88, 'Model D': 0.93, 'Model E': 0.86
    },
    'Experiment 9': {
        'Model A': 0.92, 'Model B': 0.87, 'Model C': 0.89, 'Model D': 0.95, 'Model E': 0.87
    },
    'Experiment 10': {
        'Model A': 0.89, 'Model B': 0.9, 'Model C': 0.87, 'Model D': 0.94, 'Model E': 0.88
    }
}

# Assuming model_performance dictionary is already created from the previous exercise
# Create a dictionary to store the total performance and count of evaluations for each model
total_performance = {}
count_evaluation = {}

# Iterate through the model performance dictionary
for experiment, models in model_performance.items():
    for model,  performance in models.items():
        if model in total_performance:
            total_performance[model] += performance
            count_evaluation[model] += 1
        else:
            total_performance[model] = performance
            count_evaluation[model] = 1

# Calculate the average performance for each model
average_perform = {model: total_performance[model] / count_evaluation[model] for model in total_performance}

# Find the maximum average performance
max_average_perform = max(average_perform.values())
# Create a list of models with the maximum average performance
best_perform_model = [model for model, performance in average_perform.items() if performance == max_average_perform]

print(best_perform_model)

