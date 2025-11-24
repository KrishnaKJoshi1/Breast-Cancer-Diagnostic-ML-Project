# Breast Cancer Disease Detection ML Project

![Project Banner](assets/github_banner_colored.png)

## Project Summary

This project predicts whether a breast tumor is malignant or benign using the Wisconsin Breast Cancer Diagnostic Dataset (Kaggle). It demonstrates a complete beginner–intermediate machine learning workflow including exploratory data analysis (EDA), preprocessing, model training, and evaluating multiple classifiers.

---

## Project Workflow
Data → EDA → Preprocessing → Model Training → Evaluation → Future Improvements

---

## Folder Structure

```text
Breast-Cancer-Diagnostic-ML-Project/
│
├── dataset/
│   └── data.csv
│
├── notebook/
│   └── Breast_Cancer_diagnosis_project.ipynb
│
├── reports/
│   └── Breast_Cancer_Diagnostic_Machine_Learning_Report.pdf
│
└── assets/
    └── github_banner_colored.png
```

---

## How to Open This Project

1. Download or clone this repository.  
2. Open the `notebook/` folder.  
3. Launch Jupyter Notebook.  
4. Open `Breast_Cancer_diagnosis_project.ipynb`.  
5. For the detailed write-up, open the PDF in the `reports/` folder:
   `Breast_Cancer_Diagnostic_Machine_Learning_Report.pdf`.

---

## 1. Dataset Summary

- Rows: 569  
- Columns: 32  
- Target: `diagnosis` (M = malignant, B = benign)  
- Missing values: None  
- Removed column: `id`  
- Dataset source: Wisconsin Breast Cancer Diagnostic Dataset (Kaggle)

---

## 2. Exploratory Data Analysis (EDA)

The EDA focused on understanding feature behavior and their relationship with diagnosis.

- Distribution plots (univariate) to view the shape, skewness, and spread of features.  
- Boxplots (bivariate) to compare feature values between malignant and benign classes.  
- Correlation heatmap to identify relationships between numeric features and highlight strongly correlated pairs.

---

## 3. Preprocessing Steps

- Label encoding: M → 1, B → 0  
- Separated features (X) and target (y)  
- Applied StandardScaler to numeric features  
- Train-test split: 80% training, 20% testing

---

## 4. Machine Learning Models

Three supervised classification models were used:

- Logistic Regression  
- Random Forest Classifier  
- XGBoost Classifier  

---

## 5. Model Evaluation

Models were evaluated using accuracy, precision, recall, and F1-score.

### Test Set Results

| Model               | Accuracy | Precision | Recall  | F1-score |
|---------------------|----------|-----------|---------|----------|
| Logistic Regression | 0.9737   | 0.9756    | 0.9524  | 0.9639   |
| Random Forest       | 0.9649   | 1.0000    | 0.9048  | 0.9500   |
| XGBoost             | 0.9737   | 1.0000    | 0.9286  | 0.9630   |

---

## 6. Future Improvements

- Perform hyperparameter tuning (GridSearchCV)  
- Try additional models such as SVC and KNN  
- Add cross-validation for more robust evaluation  
- Explore feature importance in more detail

---

## 7. What This Project Demonstrates

- End-to-end ML workflow on a real healthcare dataset  
- Understanding of EDA, preprocessing, model training, and evaluation  
- Ability to compare multiple classification algorithms  
- Awareness of medically meaningful metrics  
- Clear explanation of steps for both technical and non-technical audiences  
