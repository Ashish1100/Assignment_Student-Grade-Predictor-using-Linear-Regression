import pandas as pd
import os

def load_data(filepath: str) -> pd.DataFrame:
    """
    Loads data from a CSV file.
    """
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"File not found at: {filepath}")
    
    print(f"Loading data from {filepath}...")
    return pd.read_csv(filepath)

def create_dummy_data(filepath: str):
    """
    Creates a dummy CSV file if one doesn't exist.
    """
    data = {
        'Hours_Studied': [2.5, 5.1, 3.2, 8.5, 3.5, 1.5, 9.2, 5.5, 8.3, 2.7],
        'Exam_Score':    [21, 47, 27, 75, 30, 20, 88, 60, 81, 25]
    }
    df = pd.DataFrame(data)
    df.to_csv(filepath, index=False)
    print(f"Dummy data created at {filepath}")