# Student Grade Predictor

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-red)
![License](https://img.shields.io/badge/License-MIT-green)

## Project Overview
The **Student Grade Predictor** is a Machine Learning application designed to predict a student's potential exam score based on their study hours.
It features automated data pipelines, model versioning (archiving), performance visualization, and a user-friendly web interface.

## Key Features
* **Linear Regression Model:** Trained on student study data to find correlation trends.
* **Automated Visualization:** Generates regression lines and residual plots automatically after every training run.
* **Model Versioning:** Implements an "Archive + Latest" strategy:
    * Saves a unique timestamped model (e.g., `model_2025-12-29_14-30.pkl`) for history.
    * Updates a `latest_model.pkl` alias for immediate use by the app.
* **Interactive Web App:** A Streamlit-based dashboard for real-time inference.
* **Logic Guardrails:** Includes post-processing logic to ensure predictions never exceed 100% or drop below 0%.

---

## Project Structure
```text
student_grade_predictor/
│
├── data/                                              # Contains dataset (student_scores.csv)
├── images/                                            # Stores generated plots, organized by run timestamp
│   └── run_2025.../                                   # Specific folder for each training run
├── models/                                            # Stores trained models
│   ├── model_2025...pkl                               # Archived version
│   └── latest_model.pkl                               # Active version used by the App
├── notebook/              
│   ├── Assignment_Student_Grade_Predictor.ipynb       # Complete notebook (simplicity)
|   └── Assignment_Student_Grade_Predictor.html
│
├── src/                                               # Source code modules
│   ├── __init__.py
│   ├── data_loader.py                                 # Data ingestion & dummy data generation
│   ├── trainer.py                                     # Model training, evaluation & versioning
│   ├── inference.py                                   # Prediction logic with DataFrame formatting
│   └── visualization.py                               # Plotting & saving graphs
│
├── app.py                                             # Streamlit Web Application entry point
├── main.py                                            # CLI Orchestrator for training & testing
├── requirements.txt                                   # Project dependencies
└── README.md                                          # Documentation (this file)
```
---
## Model Evaluation
The model is evaluated using standard regression metrics to ensure accuracy and generalization:

- **MAE (Mean Absolute Error):** Average prediction error in score units  
- **RMSE (Root Mean Squared Error):** Penalizes larger prediction errors  
- **R² Score:** Measures goodness of fit (variance explained)

**Sample Performance**
- **MAE:**  2.22
- **RMSE:** 2.49
- **R2:**   0.98  

---

## Visualization
Regression plots are automatically generated and saved after execution.


![Regression Plot](images/regression_line.png)
