import pandas as pd
import joblib

print("Loading trained model...")
model = joblib.load("artifacts/model.joblib")

print("Reading input data...")
X_new = pd.read_csv("sample_input.csv")

print(f"Number of samples to predict: {len(X_new)}")

probs = model.predict_proba(X_new)[:, 1]
preds = (probs >= 0.5).astype(int)

# Clean output (only results)
results = pd.DataFrame({
    "patient_id": range(1, len(X_new) + 1),
    "malignant_probability": probs,
    "prediction_label": ["Malignant" if p == 1 else "Benign" for p in preds]
})

results.to_csv("predictions.csv", index=False)

print("✅ Predictions saved to predictions.csv")
print(results)

