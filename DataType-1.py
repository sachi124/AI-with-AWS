# Acci=uracy score for the last three month
accuracy_score = [87.4, 89.6, 90.6]

# calculate the average accuracy score
average_accuracy = sum(accuracy_score)/len(accuracy_score)

# print the avrage accuracy score
print(f"The acerage accuracy of the model is: {average_accuracy:.2f}%")

# Task - 2
# Managing Data Storage for Machine Learning Models
dataset1_size = 3000
dataset2_size = 4000

# size of each image in KB
image_size_kb = 256

# calculate the total storage needed 
total_storage_kb = (dataset1_size + dataset2_size) * image_size_kb

# Convert total storage needed in MB
total_storage_mb = total_storage_kb / 1024
print(f"Total Storage Needed: {total_storage_mb:.2f} MB")

# Storage device capacity
device_capacity_mb = 2048

# calclate leftover storage
leftover_storage_mb = device_capacity_mb - total_storage_mb
print(f"leftover storage in the device: {leftover_storage_mb:.2f} MB")