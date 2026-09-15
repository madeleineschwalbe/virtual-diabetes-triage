import joblib
from sklearn.datasets import load_diabetes
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
import json
import numpy as np


def train_model():
    # Load example data
    data = load_diabetes(as_frame=True)
    X = data.frame.drop(columns=["target"])
    y = data.frame["target"]

    # Split dataset into training and testing
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42)

    # Create a pipeline with scaling + linear regression
    pipeline = Pipeline([
        ("scaler", StandardScaler()),
        ("model", LinearRegression()),
    ])

    # Train the model
    pipeline.fit(X_train, y_train)

    # Evaluate performance
    preds = pipeline.predict(X_test)
    rmse = np.sqrt(mean_squared_error(y_test, preds))

    # Save model and metrics
    joblib.dump(pipeline, "app/model.pkl")
    json.dump({"rmse": rmse}, open("app/metrics.json", "w"))

    print(f"✅ Model trained! RMSE: {rmse:.3f}")
    return rmse


if __name__ == "__main__":
    train_model()
