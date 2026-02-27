
# Breast Cancer Diagnosis — Machine Learning Project

![Banner](assets/github_banner_colored.png)


# Breast Cancer Diagnosis — Machine Learning Project

## Overview
This project builds a machine learning classifier to predict whether a breast tumor is **malignant or benign** using diagnostic imaging features.

The primary objective is to **maximize Recall (Sensitivity)** to reduce missed malignant cases, which is critical in cancer screening.

---

## Dataset
Wisconsin Breast Cancer Diagnostic Dataset.

Features are numeric measurements computed from digitized breast mass cell nuclei images (e.g., radius, texture, smoothness, compactness, concavity).

---

## Models Compared
- Logistic Regression
- Random Forest
- XGBoost

Model selection prioritized **Recall** to minimize false negatives.

---

## Final Model
**Random Forest**

Key performance (test set):

| Metric | Score |
|------|------|
| Recall | 0.9286 |
| ROC-AUC | 0.9934 |
| Precision | 0.975 |
| Accuracy | 0.9649 |

---
## Quick Start (Inference Demo)

This repo includes a small inference script that loads the trained model and predicts diagnosis for new samples.

### Run locally
```bash
pip install -r requirements.txt
python src/predict.py

---
## Repository Structure


Breast-Cancer-Diagnosis-ML/
│
├── artifacts/
│ └── model.joblib
├── data/
│ └── breast_cancer.csv
├── notebook/
│ └── Breast_Cancer_diagnosis_project.ipynb
├── src/
│ └── predict.py
├── sample_input.csv
├── README.md
├── requirements.txt
└── .gitignore
----
## Skills Demonstrated
- Supervised Machine Learning
- Model Evaluation (Recall, ROC-AUC)
- Feature Importance
- Cross-Validation
- Model Serialization (joblib)
- Basic ML Inference Pipeline

---

## Author
Krishna Joshi  

Machine Learning — Healthcare Analytics
