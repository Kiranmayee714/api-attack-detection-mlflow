import pandas as pd
import mlflow.sklearn
import random

# Load model from MLflow
model = mlflow.sklearn.load_model("runs:/996e429b84c047c4b24e64da764a362b/model")

# Possible API endpoints
endpoints = ["/login", "/products", "/cart", "/payment", "/profile"]

# Simulate a new API request
request = {
    "endpoint": random.randint(0, 4),
    "requests_per_minute": random.randint(1, 120),
    "failed_logins": random.randint(0, 20),
    "payload_size": random.randint(200, 5000),
    "unusual_time": random.randint(0, 1)
}

# Convert to DataFrame
df = pd.DataFrame([request])

# Predict
prediction = model.predict(df)

if prediction[0] == 1:
    print(" Attack Detected!")
else:
    print(" Normal Traffic")

print("Request Data:", request)