import matplotlib.pyplot as plt
import pandas as pd
import joblib
import os
import numpy as np

def save_plot(filename: str, output_folder: str):
    """
    Helper function to save the current plot to a folder.
    """
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)
        
    path = os.path.join(output_folder, filename)
    plt.savefig(path)
    plt.close() # Close plot to free memory
    print(f"Saved plot to: {path}")

def visualize_performance(data_path: str, model_path: str, output_folder: str):
    """
    Loads data and model, creates visualizations, and saves them.
    """
    # 1. Load Data and Model
    if not os.path.exists(data_path) or not os.path.exists(model_path):
        print("Data or Model missing. Skipping visualization.")
        return

    df = pd.read_csv(data_path)
    model = joblib.load(model_path)

    X = df[['Hours_Studied']]
    y = df['Exam_Score']
    
    # Make predictions for the whole dataset to visualize the trend
    y_pred = model.predict(X)

    # --- PLOT 1: Regression Line (The "Best Fit") ---
    plt.figure(figsize=(10, 6))
    
    # Scatter plot of actual data
    plt.scatter(X, y, color='blue', label='Actual Scores')
    
    # Line plot of predictions
    plt.plot(X, y_pred, color='red', linewidth=2, label='Regression Line (AI Prediction)')
    
    plt.title('Study Hours vs. Exam Score (Linear Regression)')
    plt.xlabel('Hours Studied')
    plt.ylabel('Exam Score')
    plt.legend()
    plt.grid(True)
    
    save_plot('regression_line.png', output_folder)

    # --- PLOT 2: Residuals (Errors) ---
    # Shows how far off each prediction was
    residuals = y - y_pred.flatten()
    
    plt.figure(figsize=(10, 6))
    plt.scatter(X, residuals, color='purple')
    plt.axhline(y=0, color='black', linestyle='--') # Zero error line
    plt.title('Residual Plot (Prediction Errors)')
    plt.xlabel('Hours Studied')
    plt.ylabel('Error (Actual - Predicted)')
    plt.grid(True)
    
    save_plot('residuals.png', output_folder)