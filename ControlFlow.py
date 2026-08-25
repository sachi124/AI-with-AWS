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

# Count of Models Meeting Performance Thresholds
peformance_count_dict = {}
threshold = 0.9

# iterate via model performance dict
for experiment, models in model_performance.items():
    for model, performance in models.items():
        if performance >= threshold:
            if model in peformance_count_dict:
                peformance_count_dict[model] += 1
            else:
                peformance_count_dict[model] = 1
print(peformance_count_dict)