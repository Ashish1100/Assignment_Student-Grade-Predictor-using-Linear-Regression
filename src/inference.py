import joblib
import pandas as pd 
import os

def predict_score(hours: float, model_path: str) -> float:
    """
    Loads the saved model and predicts the score for given hours.
    """
    if not os.path.exists(model_path):
        raise FileNotFoundError("Model file not found! Train the model first.")

    # Load model
    model = joblib.load(model_path)


    # Instead of passing a raw list like [[hours]], we create a DataFrame
    # with the EXACT same column name used during training ('Hours_Studied').
    input_data = pd.DataFrame([[hours]], columns=['Hours_Studied'])
    
    # Predict using the DataFrame
    prediction = model.predict(input_data)
    
    # Logic to clamp the value between 0 and 100
    final_score = prediction[0]
    
    if final_score > 100:
        final_score = 100.0
    elif final_score < 0:
        final_score = 0.0
    
    return final_score