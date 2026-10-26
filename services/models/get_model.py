"""
Скрипт для выгрузки обученной модели из MLflow и сохранения её в model.pkl.
"""
import mlflow
import pickle

mlflow.set_tracking_uri("http://127.0.0.1:5000")
mlflow.set_registry_uri("http://127.0.0.1:5000")

model_uri = "models:/car_price_prediction_model/latest"
model = mlflow.sklearn.load_model(model_uri)

output_path = "/home/mainuser/ISS/Pr_1/services/models/model.pkl"

with open(output_path, "wb") as f:
    pickle.dump(model, f)

print(f"Модель сохранена в {output_path}")