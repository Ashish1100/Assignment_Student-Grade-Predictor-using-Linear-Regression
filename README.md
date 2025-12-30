<div align="center"> 

# **Student Grade Predictor using Simple Linear Regression**

![Python](https://img.shields.io/badge/Python-3.8%2B-blue)
![Machine Learning](https://img.shields.io/badge/Machine%20Learning-Scikit--Learn-orange)
![Frontend](https://img.shields.io/badge/Frontend-Streamlit-red)
[![Status: Completed](https://img.shields.io/badge/Status-Completed-green.svg)](https://github.com/Ashish1100Assignment_Student-Grade-Predictor-using-Linear-Regression/blob/main/license.md)

</div>

---

## Assignment Overview
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

## Live Demos
Try the application instantly on your preferred platform:

| Platform | Status | Link |
| :--- | :--- | :--- |
| **Streamlit** | Active | [**Launch App**](https://assignment-student-grade-predictor-using-linear-regression.streamlit.app/) |
| **Render** | Active | [**Launch App**](https://assignment-student-grade-predictor-using.onrender.com) |


---

## Repository Structure
```text
student_grade_predictor/
│
├── data/                                              # Contains dataset
|   └── student_scores.csv
├── images/                                            # Stores generated plots, organized by run timestamp
│   └── run_2025.../                                   # Specific folder for each training run
├── models/                                            # Stores trained models
│   ├── model_2025...pkl                               # Archived version
│   └── latest_model.pkl                               # Active version used by the App
├── notebook/              
│   ├── Assignment_Student_Grade_Predictor.ipynb       # Complete notebook (simplicity)
|   ├── Assignment_Student_Grade_Predictor.py
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
├── requirements.txt                                   # Assignment dependencies
├── license.md                                         # Usage licence
├── info.pdf                                           # Some important instructions
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


![Regression Plot](https://github.com/Ashish1100/Assignment_Student-Grade-Predictor-using-Linear-Regression/blob/main/images/run_2025-12-29_19-27-05/regression_line.png)

---

## Installation & Setup

### 1. Clone the Repository
```text
git clone https://github.com/Ashish1100/Assignment_Student-Grade-Predictor-using-Linear-Regression.git

cd student_grade_predictor
```

### 2. Set Up a Virtual Environment
It is recommended to use an isolated environment for dependency management.

**Windows**
```text
python -m venv venv
.\venv\Scripts\activate
```
**macOS / Linux**
```text
python3 -m venv venv
source venv/bin/activate
```

### 3. Install Dependencies
```text
pip install -r requirements.txt
```
---
## How to Run

### Full Pipeline (Train & Evaluate)
Runs the complete pipeline including data generation, model training, evaluation, and visualization.
```text
python main.py
```
**Output**
- Creates a timestamped folder under images/
- Saves the trained model to models/latest_model.pkl


### Launch the Web App
Starts the Streamlit dashboard for real-time predictions using the latest trained model.
```text
streamlit run app.py
```

---

## **License**

```
© 2025 Ashish Saha

This assignment is a personal initiative intended for educational use only.

Permission is granted to use, copy, and modify this software for learning and research purposes.
Commercial use, sale, or monetization of this software or its derivatives is strictly prohibited.

The software is provided “as is”, without warranty of any kind.

```

---


## **Author**

<div align="center">

### **Ashish Saha**
**AI Engineering** | **ML Research** | **Data Science**

*Specializing in building intelligent ML systems and transforming data into actionable insights.*

**Tech Stack:** Python • TensorFlow/Keras • PyTorch • XGBoost • Scikit-learn 

<a href="https://github.com/Ashish1100" target="_blank">
  <img src="https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white" alt="GitHub">
</a>
<a href="https://www.linkedin.com/in/ashishsaha21/" target="_blank">
  <img src="https://img.shields.io/badge/LinkedIn-0077B5?style=flat-square&logo=linkedin&logoColor=white" alt="LinkedIn">
</a>
<a href="mailto:ashishsaha.software@gmail.com">
  <img src="https://img.shields.io/badge/Email-D14836?style=flat-square&logo=gmail&logoColor=white" alt="Email">
</a>

</div>



---

</div>

<div align="center">

### **Star ⭐ this repo if you found this assignment helpful!**


---

*Made with ❤️ by Ashish Saha*

</div>
