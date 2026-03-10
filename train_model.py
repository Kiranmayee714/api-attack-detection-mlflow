import pandas as pd
import mlflow
import mlflow.sklearn
from sklearn.metrics import precision_score, recall_score, f1_score

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score

# Load dataset
df = pd.read_csv("api_traffic.csv")

# Convert endpoint to numeric
df["endpoint"] = df["endpoint"].astype("category").cat.codes

# Features and target
X = df.drop(["ip", "attack"], axis=1)
y = df["attack"]

# Train test split
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Start MLflow experiment
mlflow.set_experiment("API_Attack_Detection")

with mlflow.start_run():

    model = RandomForestClassifier()
    model.fit(X_train, y_train)

    y_pred = model.predict(X_test)

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    mlflow.log_metric("accuracy", accuracy)
    mlflow.log_metric("precision", precision)
    mlflow.log_metric("recall", recall)
    mlflow.log_metric("f1_score", f1)

    mlflow.sklearn.log_model(model, "model")

    print("Model trained successfully!")
    print("Accuracy:", accuracy)