"""
Класс-обработчик запросов к API: загрузка модели и выдача предсказаний.
"""

from pathlib import Path
import pickle
import pandas as pd

class FastAPIHandler:
    def __init__(self):
        container_path = Path("/models/model.pkl")
        local_path = Path(__file__).resolve().parent.parent / "models" / "model.pkl"

        model_path = container_path if container_path.is_file() else local_path

        with open(model_path, "rb") as f:
            self.model = pickle.load(f)

    def predict(self, data):
        df = pd.DataFrame([data])
        prediction = self.model.predict(df)

        return prediction[0]