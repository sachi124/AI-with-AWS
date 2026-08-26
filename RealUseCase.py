customers = [
    {
        "name": "ABC Construction",
        "province": "Bagmati",
        "machine": "Excavator",
        "sales": 5000000,
        "last_contact": 10,
        "status": "Interested"
    },
    {
        "name": "XYZ Builders",
        "province": "Gandaki",
        "machine": "Wheel Loader",
        "sales": 1500000,
        "last_contact": 45,
        "status": "No Response"
    },
    {
        "name": "Nepal Infra",
        "province": "Bagmati",
        "machine": "Excavator",
        "sales": 7500000,
        "last_contact": 5,
        "status": "Interested"
    },
    {
        "name": "Himalayan Road",
        "province": "Koshi",
        "machine": "Motor Grader",
        "sales": 800000,
        "last_contact": 60,
        "status": "No Response"
    },
    {
        "name": "Everest Projects",
        "province": "Lumbini",
        "machine": "Compactor",
        "sales": 3000000,
        "last_contact": 20,
        "status": "Quotation"
    }
]

# Calculate the total sales
totol_sales = sum(customer["sales"] for customer in customers)

total_sales = sum(customer["sales"] for customer in customers)

# find the highest value of customer
highest_customer = max(
    customers,
    key=lambda customer: customer["sales"]
)

print("Highest Customer:", highest_customer["name"])
print("Sales:", highest_customer["sales"])

# Find the customer that need follow up
follow_up_customers = [
    customer
    for customer in customers
    if customer["last_contact"] > 30
]

for customer in follow_up_customers:
    print(customer["name"])

# Customer segmentation
for customer in customers:

    sales = customer["sales"]

    if sales >= 5000000:
        category = "High value"
    elif sales >= 1000000:
        category = "Meduim Value"
    else:
        category = "Low Value"

    print(customer["name"], "->", category)

# Segrigate province wise sales

province_sale = {}

for customer in customers:
    province = customer["province"]
    sales = customer["sales"]

    if province not in province_sale:
        province_sale["sales"] = 0
    province_sale["sales"] += sales

print(province_sale)

# find the most popular machine
machine_count = {}

for customer in customers:
    machine = customer["machine"]
    machine_count[machine] = machine_count.get(machine, 0) + 1

print(machine_count)

# find the most popular
most_popular = max(
    machine_count,
    key=machine_count.get
)

print("The most popular machine:", most_popular)

# creating outreach priority score

for customer in customers:

    score  = 0
    # sales value
    if customer["sales"] >= 5000000:
        score += 3
    elif customer["sales"] >= 1000000:
        score += 2
    else:
        score += 1

    # Days since last contacted
    if customer["last_contact"] > 30:
        score += 3
    elif customer["last_contact"] > 15:
        score +=2
    else:
        score += 1

    # customer status
    if customer["status"] == "Intrested":
        score += 3
    elif customer["status"] == "Quotation":
        score += 2
    else:
        score += 1

    print(customer["name"], "Score:", score)


if score >= 7:
    priority = "HIGH"
elif score >= 5:
    priority = "MEDIUM"
else:
    priority = "LOW"