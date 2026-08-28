import pandas as pd
import numpy as np

# Reproducible
np.random.seed(42)

# Number of customer
n = 10000

# 1. generate the customer data
customer_id = [
    f"CUST{str(i).zfill(5)}"
    for i in range(1, n + 1)
]

age = np.random.randint(18, 71, n)

gender = np.random.choice(
    ["Male", "Female"],
    size=n
)

plan = np.random.choice(
    ["Basic", "Standard", "Premium"],
    size=n,
    p=[0.35, 0.45, 0.20]
)

monthly_bill = np.where(
    plan == "Basic",
    np.random.normal(30, 7, n),
    np.where(
        plan =="Standard",
        np.random.normal(50, 10, n),
        np.random.normal(75, 12, n)
    )
)

monthly_bill = np.clip(
    monthly_bill,
    15,
    120
)

tenure = np.random.randint(
    1,
    73,
    n
)

support_calls = np.random.poisson(3, n)

support_calls = np.clip(support_calls, 0, 15)

data_usage = np.random.gamma(shape=3, scale=8, size=n)

data_usage = np.clip(data_usage, 1, 100)

payment_method = np.random.choice(
    [
        "Card",
        "Bank Transfer",
        "Cash",
        "Mobile Wallet"
    ],
    size=n,
    p=[0.35, 0.25, 0.15, 0.25]
)

# Create churn probability, we intentionally create relationships between customer behaviour and churn

logit = (
    -2.4
    +0.035 * (monthly_bill - 45)
    -0.035 * (tenure - 24)
    +0.22 * support_calls
    -0.008 * (data_usage - 25)
    +0.35 * (plan == "Basic")
    +0.15 * (payment_method == "Cash")
    +0.10 * (age < 25)
)

# convert logit into probability
churn_probability = (
    1 / (1 + np.exp(-logit))
)

# Generate Yes/No churn
churn = np.where(
    np.random.random(n) < churn_probability,
    "Yes", "No"
)

# Create DataFrame
df = pd.DataFrame({
    "customer_id": customer_id,
    "age": age,
    "gender": gender,
    "plan": plan,
    "monthly_bill": np.round(monthly_bill, 2),
    "tenure": tenure,
    "support_calls": support_calls,
    "data_usage": np.round(data_usage, 2),
    "payment_method": payment_method,
    "churn": churn
})

# Add missing values, intentional

for column in [
    "monthly_bill",
    "data_usage",
    "payment_method"
]:
    random_indices = np.random.choice(
        df.index,
        size=100,
        replace=False
    )

    df.loc[
        random_indices,
        column
    ] = np.nan

# Add duplicate record
duplicates = df.sample(20, random_state=42)

df = pd.concat(
    [df, duplicates],
    ignore_index=True
)

df.to_csv(
    "customer_churn_1000.csv", index=False
)
print("Dataset created successfully!")