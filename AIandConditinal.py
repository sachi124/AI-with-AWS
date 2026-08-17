actual_accuracy = 0.80
predicted_accuracy = 0.82
if predicted_accuracy < actual_accuracy:
    result = "Your predictin is too low!"
elif predicted_accuracy > actual_accuracy:
    result = "Your prediction is too high"
else:
    result = "Nice! Your prediction match with actual value"

def get_solution(actual_accuracy, prediction_accuracy):
    if predicted_accuracy > actual_accuracy:
        return "Your predictin is too high!"
    elif predicted_accuracy < actual_accuracy:
        return "Your prediction is too low"
    else:
        return "Nice! Your prediction match with actual value"

if result == get_solution(actual_accuracy, predicted_accuracy):
    print("Great")
else:
    print("Please try again")