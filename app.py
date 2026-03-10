import gradio as gr
import joblib

# load model
model = joblib.load("model.pkl")

def predict(endpoint, rpm, failed, payload, time):

    features = [[endpoint, rpm, failed, payload, time]]

    prediction = model.predict(features)

    if prediction[0] == 1:
        return " Attack Detected"
    else:
        return " Normal Traffic"

interface = gr.Interface(
    fn=predict,
    inputs=[
        gr.Number(label="Endpoint"),
        gr.Number(label="Requests per Minute"),
        gr.Number(label="Failed Logins"),
        gr.Number(label="Payload Size"),
        gr.Number(label="Unusual Time (0 or 1)")
    ],
    outputs="text",
    title="API Attack Detection System",
    description="Enter API traffic details to detect attacks."
)

interface.launch()