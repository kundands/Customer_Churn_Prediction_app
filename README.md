# Customer_Churn_Prediction_app
A streamlined pipeline that moves from data collection to preprocessing, model training, and finally predicting churn for new customers.

<img width="720" height="600" alt="churn prediction workflow" src="https://github.com/user-attachments/assets/89864640-4596-4309-b566-874ca86613d1" />



## 📌 Overview

This project is a Customer Churn Prediction System built using Machine Learning and deployed with a user-friendly Streamlit web app.
The goal is to help telecom companies identify customers who are likely to churn (discontinue service) and take preventive action.

This end-to-end solution includes:


Data cleaning  
Feature encoding  
SMOTE for class imbalance   
Model training & hyperparameter tuning   
Model evaluation   
Streamlit web app for real-time prediction  

## 📂 Dataset

The dataset used is the popular Telco Customer Churn Dataset, containing customer service usage and subscription details.

Key fields include: 
Demographics: gender, SeniorCitizen, Partner, Dependents   
Services: InternetService, PhoneService, TechSupport, etc.   
Billing: Contract, PaymentMethod, MonthlyCharges, TotalCharges   
Target: Churn (Yes/No)   

## 🛠️ Tools & Technologies

Python 3.8+   
Pandas, NumPy – Data processing   
Scikit-learn – ML model training & preprocessing   
XGBoost – Final selected algorithm   
Imbalanced-learn (SMOTE) – Handle class imbalance   
Pickle – Save trained model and preprocessing objects   

## Streamlit – Web application
The app takes user inputs via dropdown menus for all categorical features and predicts whether the customer is likely to churn.

App Features:-   
Clean 3-column layout   
Automatic manual encoding   
Scaling of numeric features   
Probability-based prediction output   


## ▶️ How to Run This Project 

### **1. Clone the Repository**
```bash
git clone https://github.com/yourusername/customer-churn-app.git
cd customer-churn-app
```

### **2. Create Virtual Environment**
```bash
python -m venv venv
```

### **3. Activate the Virtual Environment (Windows)**
```bash

venv\Scripts\activate
```
### **4. Activate the Virtual Environment (Mac/Linux)**
```bash

source venv/bin/activate
```
### **5. Install Dependencies**
```bash
pip install -r requirements.txt
```

### **6. Run Streamlit App**
```bash
streamlit run app.py
```

# ⭐ Output Example

"Customer is likely to churn" (with probability)   
"Customer is not likely to churn" (with probability)   
