"""
Problem Statement
Depending on the cloud provider, you need to apply the appropriate cost rate to the computation cost. The providers and their rates are as follows: AWS (7.5%), Azure (9.5%), and GCP (8.9%). Use this information to calculate the total cost of running the training session based on the provider and the initial computation cost.

Example Input:

provider = "AWS"  # Either "AWS", "Azure", or "GCP"
computation_cost = 1000  # amount of computation cost
Instructions:

Use the provider to determine the cost rate.
Calculate the total cost based on the computation cost and the cost rate.
Inform the user of the total cost based on their provider.
"""

# provider and computational cost
provider = 'AWS'
computational_cost = 1000

if provider == 'AWS':
    cost_rate = .075
    total_cost = computational_cost * (1 + cost_rate)
    result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
elif provider == 'Azure':
    cost_rate = .095
    total_cost = computational_cost * (1 + cost_rate)
    result = "Since you are using {}, Your total cost is ${:.2f}.".format(provider, total_cost)
elif provider == 'GCP':
    cost_rate = .089
    total_cost = computational_cost * (1 + cost_rate)
    result = "Since, You are using {}, Your total cost is ${:.2f}.".format(provider, total_cost)
else:
    result = "Provider not recognized."

def get_solution(provider, computational_cost):
    if provider == 'AWS':
        cost_rate = .075
        total_cost = computational_cost * (1 + cost_rate)
        result = "Since you are using {}, your total cost is ${:.2f}.".format(provider, total_cost)
    elif provider == 'Azure':
        cost_rate = .095
        total_cost = computational_cost * (1 + cost_rate)
        result = "Since you are using {}, Your total cost is ${:.2f}.".format(provider, total_cost)
    elif provider == 'GCP':
        cost_rate = .089
        total_cost = computational_cost * (1 + cost_rate)
        result = "Since, You are using {}, Your total cost is ${:.2f}.".format(provider, total_cost)
    else:
        result = "Provider not recognized."
    return result

if result == get_solution(provider, computational_cost):
    print("Great")
else:
    print("Not Matched.")