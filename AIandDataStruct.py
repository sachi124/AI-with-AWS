# Count unique words in the AI model Descriptions

model_descriptions = "ResNet is a convolutional neural network that is 50 layers deep. MobileNet is a lightweight convolutional neural network designed for mobile and embedded vision applications. VGG is a convolutional neural network model proposed by Visual Geometry Group of Oxford University. Inception is a deep convolutional neural network architecture that has achieved state-of-the-art results."
print(model_descriptions, '\n')

# Split the model descriptions
model_list = model_descriptions.split()
print(model_list, '\n')

# convert list toa data structure that store unique element
model_set = set(model_list)
print(model_set, '\n')

# find the number of unique words
num_unique = len(model_set)
print(num_unique, '\n')



# Model Accuracy Dictionnary
model_accuracy_dict = {
    'ResNet': 0.91, 'MobileNet': 0.89, 'VGG': 0.88, 'Inception': 0.92, 
    'AlexNet': 0.85, 'EfficientNet': 0.93, 'SqueezeNet': 0.87
}

print(model_accuracy_dict, '\n')

# find the number of unique key in the dict
num_models = len(model_accuracy_dict)
print(num_models)

# find the 'SachinNet' in the dict key
contains_sachinnet = 'SachinNet' in model_accuracy_dict
print(contains_sachinnet)

# create and sort a list of the dict keys
sorted_keys = sorted(model_accuracy_dict)
print(sorted_keys)

# get the fist element from the sorted list
first_element = sorted_keys[0]
print(first_element)

# find the element with the higest value in the dict
highest_accuracy_model = max(model_accuracy_dict, key=model_accuracy_dict.get)
print(highest_accuracy_model)
