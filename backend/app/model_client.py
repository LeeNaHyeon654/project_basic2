import os
import requests

MODEL_API_URL = https://interplacental-liana-puddly.ngrok-free.dev

def predict_customer(customer_data: dict) -> dict:
    response = requests.post(f"{MODEL_API_URL}/predict", json=customer_data)
    response.raise_for_status()
    return response.json()

print("MODEL_API_URL =", MODEL_API_URL)
