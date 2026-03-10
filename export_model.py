import mlflow.sklearn
import joblib

# load model from MLflow
model = mlflow.sklearn.load_model("runs:/3fccb8d1afdd480b974f5bb4b527d8af/model")

# save model locally
joblib.dump(model, "model.pkl")

print(" Model exported successfully!")