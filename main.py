from src.data_loader import load_data, create_dummy_data
from src.trainer import train_model
from src.inference import predict_score
from src.visualization import visualize_performance
import os
from datetime import datetime # Import datetime

# --- 1. Generate Timestamp ---
# Format: YYYY-MM-DD_HH-MM-SS 
timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

# --- 2. Define Paths with Timestamps ---
# Data: We keep one main data file, but you could timestamp this too if data changes
DATA_FILE = 'data/student_scores.csv' 

# Model: We save a unique file every time we run this
MODEL_FILE = f'models/model_{timestamp}.pkl'

# Images: We create a specific folder for this run's images
IMAGE_FOLDER = f'images/run_{timestamp}/'

def main():
    print(f"--- Starting Run: {timestamp} ---")

    # 1. Setup Data
    if not os.path.exists(DATA_FILE):
        create_dummy_data(DATA_FILE)

    # 2. Load Data
    df = load_data(DATA_FILE)

    # 3. Train Model
    # This will save 'model_TIMESTAMP.pkl' AND 'latest_model.pkl'
    train_model(df, MODEL_FILE)

    # 4. Visualization
    # Passes the timestamped model path and specific image folder
    print("\nGenerating visualizations...")
    visualize_performance(DATA_FILE, MODEL_FILE, IMAGE_FOLDER)

    # 5. Inference
    # We test using the specific model we just trained
    print("\n--- Testing Current Model ---")
    try:
        user_input = float(input("Enter hours studied: "))
        prediction = predict_score(user_input, MODEL_FILE)
        print(f"Predicted Score: {prediction:.2f}")
    except ValueError:
        print("Invalid input.")

if __name__ == "__main__":
    main()