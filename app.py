import streamlit as st
import pandas as pd
import pickle

st.set_page_config(page_title="Telco Churn Prediction", layout="wide")
st.title("📊 Telco Customer Churn Prediction App")

# -------------------------
# Load model + scaler + encoding map
# -------------------------
with open("model.pkl", "rb") as f:
    model = pickle.load(f)

with open("scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

with open("encoding_map.pkl", "rb") as f:
    encoding_map = pickle.load(f)

# -------------------------
# Feature definitions
# -------------------------
features = [
    'gender', 'SeniorCitizen', 'Partner', 'Dependents', 'tenure',
    'PhoneService', 'MultipleLines', 'InternetService', 'OnlineSecurity',
    'OnlineBackup', 'DeviceProtection', 'TechSupport', 'StreamingTV',
    'StreamingMovies', 'Contract', 'PaperlessBilling', 'PaymentMethod',
    'MonthlyCharges', 'TotalCharges'
]

num_cols = ['tenure', 'MonthlyCharges', 'TotalCharges']

options_dict = {
    "gender": ['Female', 'Male'],
    "SeniorCitizen": ['No', 'Yes'],
    "Partner": ['Yes', 'No'],
    "Dependents": ['No', 'Yes'],
    "PhoneService": ['No', 'Yes'],
    "MultipleLines": ['No phone service', 'No', 'Yes'],
    "InternetService": ['DSL', 'Fiber optic', 'No'],
    "OnlineSecurity": ['No', 'Yes', 'No internet service'],
    "OnlineBackup": ['Yes', 'No', 'No internet service'],
    "DeviceProtection": ['No', 'Yes', 'No internet service'],
    "TechSupport": ['No', 'Yes', 'No internet service'],
    "StreamingTV": ['No', 'Yes', 'No internet service'],
    "StreamingMovies": ['No', 'Yes', 'No internet service'],
    "Contract": ['Month-to-month', 'One year', 'Two year'],
    "PaperlessBilling": ['Yes', 'No'],
    "PaymentMethod": [
        'Electronic check', 'Mailed check',
        'Bank transfer (automatic)', 'Credit card (automatic)'
    ]
}

# -------------------------
# UI INPUT SECTION
# -------------------------
st.header("Enter Customer Details")

col1, col2, col3 = st.columns(3)
inputs = {}

for idx, col in enumerate(features):
    with [col1, col2, col3][idx % 3]:
        if col in options_dict:
            inputs[col] = st.selectbox(col, options_dict[col])
        else:
            inputs[col] = st.number_input(col, value=0.0)

# -------------------------
# Prediction Section
# -------------------------
if st.button("Predict Churn"):

    # Create input DataFrame
    df = pd.DataFrame([inputs])

    # Apply manual encoding
    df = df.replace(encoding_map)

    # Scale numericals
    df[num_cols] = scaler.transform(df[num_cols])

    # Predict
    pred = model.predict(df)[0]
    prob = model.predict_proba(df)[0][1]*100

    st.subheader("Prediction Result")
    if pred == 1:
        st.error(f"⚠️ Customer is likely to **CHURN** (Probability: {prob:.2f})")
    else:
        st.success(f"✅ Customer is **NOT likely** to churn (Probability: {prob:.2f})")