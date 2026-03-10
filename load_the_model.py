   #3fccb8d1afdd480b974f5bb4b527d8af////# This code is for loading a pre-trained model and using it for inference.
import mlflow
import mlflow.sklearn

# replace with your run id
model = mlflow.sklearn.load_model("runs:/3fccb8d1afdd480b974f5bb4b527d8af/model")

sample = [[1, 50, 3, 1000, 0]]

prediction = model.predict(sample)

print("Prediction:", prediction)