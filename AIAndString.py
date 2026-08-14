ford_quote = "Whether you think you can, or you think you can't--you're right."

username = "Sachin"
timestamp = "06:60"
predicted_label = "Men"

message = f"User {username} received a prediction of {predicted_label} at {timestamp}."

# Notebook grading
def space_error(message):
    feedback = ""
    error = False
    """
    Check for spacing errors in the message string.
    """
    if message =="":
        error = True
        feedback = 'Looks like you are not printing anything!'
        return error, feedback
    if message[0]=='"' or message[-1]=='"':
        feedback = 'The line does not need to start or end with quotes'
        error = True
    if "Sachinreceived" in message:
        feedback = 'There should be space between the userbane abd the word'
        error =True
    if "predictionof" in message:
        feedback = 'There should be space between the prediction and feedback'
        error = True
    if message == ' ':
        feedback = 'looks like you are printing a space!'
        error = True
    return error, feedback

error, feedback = space_error(message)
if message == "User Sachin received a prediction of Men at 06:60.":
    print("The message is correct!")
elif error:
    print(feedback)
else:
    print("The message is incorrect.")