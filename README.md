![Project Banner](assets/github_banner_colored.png)

# Breast Cancer Diagnosis — Machine Learning Project

## Project Overview

In this project, I built a machine learning classification model to predict whether a breast tumor is **Malignant** or **Benign** using structured diagnostic data.

The primary objective is to prioritize **Recall (Sensitivity)** to minimize missed malignant cases — a critical consideration in cancer screening.

This project demonstrates a complete end-to-end machine learning workflow — from raw data to trained model to reusable inference script.

---

## Dataset

Wisconsin Breast Cancer Diagnostic Dataset  
Public dataset containing structured numeric diagnostic features derived from digitized tumor images.

---

## Machine Learning Workflow

1. Data preprocessing and cleaning  
2. Exploratory Data Analysis (EDA)  
3. Correlation analysis and feature reduction  
4. Train–test split  
5. Model training and comparison:
   - Logistic Regression  
   - Random Forest  
   - XGBoost  
6. Recall-priority model selection  
7. Evaluation using:
   - Confusion Matrix  
   - ROC Curve  
   - Precision–Recall Curve  
8. Feature Importance analysis  
9. 5-fold cross-validation  
10. Final model packaging for inference  

---

## Model Performance (Test Set)

| Model | Recall | ROC-AUC | Precision | F1 Score | Accuracy |
|--------|--------|----------|-----------|----------|----------|
| Random Forest | 0.9286 | 0.9934 | 0.9750 | 0.9512 | 0.9649 |
| Logistic Regression | 0.9048 | 0.9957 | 1.0000 | 0.9500 | 0.9649 |
| XGBoost | 0.8810 | 0.9897 | 0.9487 | 0.9136 | 0.9386 |

Based on Recall and overall balance, **Random Forest** was selected as the final model.

---

## Inference Demo (How to Use This Project)

After training and evaluation, the final model was saved and packaged with a simple prediction script.

Trained model location:
artifacts/model.joblib

Sample input file:
sample_input.csv

### Run Inference Locally

From the project root folder, run:

pip install -r requirements.txt  
python src/predict.py  

This will generate:

predictions.csv  

The output file includes:
- Malignant probability  
- Final predicted label (Malignant / Benign)

This demonstrates reproducible model usage beyond notebook experimentation.

---

## Repository Structure

Breast-Cancer-Diagnosis-ML/
│
├── artifacts/
│   └── model.joblib  
├── data/  
├── notebook/  
│   └── Breast_Cancer_diagnosis_project.ipynb  
├── src/  
│   └── predict.py  
├── sample_input.csv  
├── README.md  
├── requirements.txt  
└── .gitignore  

---

## What This Project Demonstrates

- End-to-end ML workflow on healthcare data  
- Clinical metric prioritization (Recall-first modeling)  
- Comparison of multiple classification models  
- Cross-validation for reliability  
- Basic model interpretability  
- Packaging a trained model for real-world usage  

---

## Future Improvements

- Threshold tuning for specific clinical sensitivity targets  
- SHAP-based interpretability  
- Streamlit-based interactive prediction app  
- API deployment  
- Cloud deployment  

---

## Author

Krishna Joshi  
Machine Learning — Healthcare Analytics
