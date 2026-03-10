
# API Attack Detection using Machine Learning and MLflow

This project demonstrates how machine learning can be used to detect suspicious API traffic.  
It covers the complete ML lifecycle including training, experiment tracking with MLflow, and deployment using Gradio.

---

## Project Overview

Modern applications rely on APIs for communication between services.  
These APIs can be targeted by attackers using techniques such as:

- Request flooding
- Brute-force login attempts
- Abnormal payload submissions

This project builds a machine learning model to classify API traffic as:

• Normal Traffic  
• Attack Detected

---

## Features

- API traffic simulation
- Machine learning based attack detection
- MLflow experiment tracking
- Gradio web interface
- Deployment on Hugging Face Spaces

---

## Input Features

The model uses the following features:

- endpoint
- requests_per_minute
- failed_logins
- payload_size
- unusual_time

---

## Output

The model predicts:

- **Normal Traffic**
- **Attack Detected**

---

## Technologies Used

- Python
- Pandas
- Scikit-learn
- XGBoost
- MLflow
- Gradio
- Hugging Face Spaces

---

## Project Structure

api-attack-detection-mlflow

│

├── app.py

├── detect_attack.py

├── mlflow_demo.py

├── load_the_model.py

├── model.pkl

├── requirements.txt

└── README.md

---


### Gradio Prediction Interface
![Gradio Interface](screenshots/gradio_interface.png)

### Attack Detection Output
![Terminal Output](screenshots/attack_output.png)

## Live Demo

Deployed on Hugging Face Spaces

https://huggingface.co/spaces/ka4920/api-attack-detection

## Author

Kiranmayee Avula  
SRM University

