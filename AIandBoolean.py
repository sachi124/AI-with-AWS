"""
Problem Statement
Given an accuracy value, assign a performance level based on the following criteria:

0% - 50%: Poor performance
51% - 75%: Average performance
76% - 90%: Good performance
91% - 100%: Excellent performance
Assign the corresponding result message based on the performance level.

Example Input:

accuracy = 0.88  # use this as input for your submission
Instructions:

Establish the default performance level to None.
Use the accuracy value to assign performance levels to the correct performance names.
Use the truth value of performance level to assign result to the correct message.
"""

accuracy = 0.88  # use this as input for your submission

# Establish the default performance level to None
performance = None

# Use the accuracy value to assign performance levels to the correct performance names
# TODO
if 0.0 <= accuracy <= 0.50:
    performance = "Poor performance"
elif 0.51 <= accuracy <= 0.75:
    performance = "Average performance"
elif 0.76 <= accuracy <= 0.90:
    performance = "Good performance"
elif 0.91 <= accuracy <= 1:
    performance = "Excellent performance"
else:
    performance = None

# Use the truth value of performance to assign result to the correct phrase
if performance:
    result = "The model has achieved {}.".format(performance)
else:
    result = "Performance level not defined."

# Notebook grading
if result == "The model has achieved Good performance.":
    print("Good work!")
else:
    print("Not quite! Are your result string formatted correctly?")