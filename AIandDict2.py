# Adding prperties to the nested dictionaries

models = {'ResNet': {'layers': 50, 'accuracy': 0.91, 'type': 'CNN'},
          'MobileNet': {'layers':28, 'accuracy': 0.89, 'type': 'CNN'}
}

# Add is_lightweight property to each model
models['ResNet']['is_lightweight'] = False
models['MobileNet']['is_lightweight'] = True

# Grading
print(models)