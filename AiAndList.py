# To find the Acronyn of the Models
models = ["Logistic Regression", "Deceision Tree", "Random Forest", "Support Vectr machine", "Naive nayas"]
model_acronyms = ["".join(word[0] for word in model.split()) for model in models]

print(model_acronyms)

# Created own acronyms using list comprehensions
Name = ["Sushil Kumar Bista", "Sachin Bista", "Puran bista", "Aayush Bista", "Jhankar Bdr Bista", "Radhika Bista", "Koyali Bista"]
acronyms = ["".join(word[0] for word in name.split()) for name in Name]
print(acronyms)

# Learning Rate Decay
initial_lr = 0.1
decay_factor = 0.1
learning_rates = [initial_lr * (decay_factor ** i) for i in range(6)]
learning_rates = [format(lr, '.6f') for lr in learning_rates]
print(learning_rates)

# Filter Models by performance
model_performance = {
    "logistic Regression": 90,
    "Decision Tree": 75,
    "Random Forest": 92,
    "Support Vector machine": 80,
    "Naive Bayes": 88
}

passed_model = [model for model, score in model_performance.items() if score > 85]

print(passed_model)

# Created own example
Student_marks = {
    "Sachin Bista": 100,
    "Sachin ": 90,
    "Sachin B": 99,
    "Sachin BISTA": 95,
    "Sachin bista": 94
}
Passed_std = [name for name, score in Student_marks.items() if score > 95]
print(Passed_std)

# Compounding Price Discount (Exponential Decay)
initial_price = 100.0
decay_rate = 0.8 

# calculate the prive over 5 weeks
prices = [initial_price * (decay_rate ** week) for week in range(6)]
formatted_price = [f"${price:.2f}" for price in prices]
print(formatted_price)

# Step based learning rate decay
base_le = 0.05
decay_factor = 0.5

lrs = [base_le * (decay_factor ** (epoch // 2)) for epoch in range(8)]
formatted_le = [f"{le:.4f}" for le in lrs]
print(formatted_le)

# Question 1
initial_lr = 0.05
decay_factor = 0.5

learning_rates = [initial_lr * (decay_factor ** init) for init in range(5)]
learning_rates = [f"{learn:.4f}" for learn in learning_rates]
print(learning_rates)
