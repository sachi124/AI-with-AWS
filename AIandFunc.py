# Displaying and returning Dataset Sizes
# You are developing a utility to handle large datasets for a machine learning project. 
# You need functions to both display and return the size of a dataset after adding a specified increment. 
# This is useful for logging and processing purposes.

# This function prints the dataset size after adding the increment, but does not return anything
def display_new_size(current_size, increment):
    new_size = current_size + increment
    print(f"New dataset size after adding {increment} GB: {new_size} GB")

# This function returns the dataset size after adding the increment
def get_new_size(current_size, increment):
    new_size = current_size + increment
    return new_size

# example usage
current_size = 50
increment = 10

print("Calling display new size")
return_value1 = display_new_size(current_size, increment)  # This will print the new size but return None
print("Done Calling")
print("This function returned {}".format(return_value1))  # This will print "This function returned None"

print("\nCalling get new size")
return_value2 = get_new_size(current_size, increment)  # This will return the new size
print("Done Calling")
print("This function returned {}".format(return_value2))  # This will print "This function returned 60"

