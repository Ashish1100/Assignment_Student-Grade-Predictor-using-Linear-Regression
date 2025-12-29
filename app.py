import streamlit as st
import joblib
import pandas as pd
import os

# 1. Setup Title
st.title("Student Exam Score Predictor")
st.write("Enter study hours to predict the score")

# 2. Load Model
model_path = 'models/latest_model.pkl'

if os.path.exists(model_path):
    model = joblib.load(model_path)
    
    # 3. Slider Input
    hours = st.slider("Hours Studied", min_value=0.0, max_value=15.0, step=0.5)

    if st.button("Predict Score"):
        # Prepare input with correct column name
        input_data = pd.DataFrame([[hours]], columns=['Hours_Studied'])
        
        # Make Prediction
        raw_prediction = model.predict(input_data)[0]

        # ---CLAMPING THE VALUE ---
        # 1. If prediction > 100, make it 100.
        # 2. If prediction < 0, make it 0.
        if raw_prediction > 100:
            final_score = 100.0
        elif raw_prediction < 0:
            final_score = 0.0
        else:
            final_score = raw_prediction
        
        # --- Display Result ---
        st.success(f"If you study for **{hours} hours**, you might score: **{final_score:.2f}%**")

        # Fun logic
        if final_score >= 90:
            st.balloons()
            
else:
    st.error("Model file not found. Please run 'python main.py' first.")