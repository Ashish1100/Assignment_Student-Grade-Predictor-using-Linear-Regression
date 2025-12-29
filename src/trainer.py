import pandas as pd
import joblib
import numpy as np
import os
import shutil # for copying files
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score, mean_absolute_error, mean_squared_error

def train_model(df: pd.DataFrame, timestamped_path: str):
    """
    Trains model and saves two versions:
    1. The timestamped version (for tracking history).
    2. A 'latest_model.pkl' version (for the App to use).
    """
    X = df[['Hours_Studied']]
    y = df['Exam_Score']

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    print("Training model...")
    model = LinearRegression()
    model.fit(X_train, y_train)

    # Evaluation
    predictions = model.predict(X_test)
    mae = mean_absolute_error(y_test, predictions)
    rmse = np.sqrt(mean_squared_error(y_test, predictions))
    r2 = r2_score(y_test, predictions)

    print(f"\n--- Model Performance ---")
    print(f"MAE:  {mae:.2f}")
    print(f"RMSE: {rmse:.2f}")
    print(f"R2:   {r2:.2f}")

    # --- SAVE 1: Timestamped Version (The Archive) ---
    joblib.dump(model, timestamped_path)
    print(f"Saved tracked model to: {timestamped_path}")

    # --- SAVE 2: The 'Latest' Version (For the App) ---
    # We strip the folder from the path to get just the directory
    folder = os.path.dirname(timestamped_path)
    latest_path = os.path.join(folder, 'latest_model.pkl')
    
    # Copy the file we just saved
    shutil.copyfile(timestamped_path, latest_path)
    print(f"Updated latest model alias at: {latest_path}")