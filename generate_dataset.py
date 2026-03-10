import pandas as pd
import random

data = []

for i in range(1000):

    endpoint = random.randint(0,4)
    requests_per_minute = random.randint(1,120)
    failed_logins = random.randint(0,20)
    payload_size = random.randint(200,5000)
    unusual_time = random.randint(0,1)

    # add realistic noise
    attack = 0

    if (
        requests_per_minute > random.randint(90,120)
        or failed_logins > random.randint(12,20)
        or (unusual_time == 1 and requests_per_minute > 70)
    ):
        attack = 1

    data.append([
        endpoint,
        requests_per_minute,
        failed_logins,
        payload_size,
        unusual_time,
        attack
    ])

df = pd.DataFrame(data, columns=[
    "endpoint",
    "requests_per_minute",
    "failed_logins",
    "payload_size",
    "unusual_time",
    "attack"
])

df.to_csv("api_traffic.csv", index=False)

print("Dataset Generated Successfully!")