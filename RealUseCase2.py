import pandas as pd
import random
from datetime import datetime, timedelta

random.seed(42)

users = [
    "ram", "sita", "hari", "sachin",
    "admin", "manager", "sales01",
    "hr01", "finance01"
]

normal_ips = [
    "192.168.1.10",
    "192.168.1.11",
    "192.168.1.12"
]

suspicious_ips = [
    "103.45.22.10",
    "45.22.91.12"
]

devices = [
    "Windows",
    "Linux",
    "Android",
    "iPhone"
]

locations = [
    "Kathmandu",
    "Lalitpur",
    "Bhaktapur",
    "Pokhara",
    "India"
]

data = []

start_time = datetime(2026, 8, 1, 9, 0)

for i in range(10000):

    timestamp = start_time + timedelta(
        minutes=random.randint(0, 30 * 24 * 60)
    )

    username = random.choice(users)

    # Mostly normal IPs, sometimes suspicious
    if random.random() < 0.10:
        ip = random.choice(suspicious_ips)
    else:
        ip = random.choice(normal_ips)

    device = random.choice(devices)
    location = random.choice(locations)

    # Normal login behavior
    status = random.choices(
        ["success", "failed"],
        weights=[90, 10]
    )[0]

    data.append({
        "timestamp": timestamp,
        "username": username,
        "ip_address": ip,
        "status": status,
        "device": device,
        "location": location
    })

df = pd.DataFrame(data)

df.to_csv(
    "login_logs.csv",
    index=False
)

print("Created", len(df), "records")