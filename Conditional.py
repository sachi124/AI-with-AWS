# Evaluating Model performance
accuracy = 0.85

# if statement
if 0.0 <= accuracy <= 0.5:
    result = "Model Performance: Poor"
elif 0.51 <= accuracy <= 0.75:
    result = "MOdel Performance: Average"
elif 0.76 <= accuracy <= 0.90:
    result = "Model Performance: Good"
elif 0.91 <= accuracy <= 1.0:
    result = "Model Performance: Excellent"
else:
    result = "Invalid accuracy score."

print(result)
