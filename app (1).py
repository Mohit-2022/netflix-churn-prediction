import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("churn_top4_model.pkl")

st.title("Netflix Churn Prediction App 🎬")

st.write("Enter customer details below:")

# Inputs
avg_watch_time = st.number_input("Avg Watch Time Per Day (hours)", min_value=0.0)
last_login_days = st.number_input("Days Since Last Login", min_value=0)
num_profiles = st.number_input("Number of Profiles", min_value=1)
monthly_fee = st.number_input("Monthly Fee ($)", min_value=0.0)

if st.button("Predict Churn"):
    
    input_data = pd.DataFrame([{
        "Avg_watch_time_per_day": avg_watch_time,
        "Last_login_days": last_login_days,
        "Number_of_Profile": num_profiles,
        "Monthly Fee ($)": monthly_fee
    }])
    
    prediction = model.predict(input_data)[0]
    probability = model.predict_proba(input_data)[0][1]
    
    st.write("Churn Probability:", round(probability * 100, 2), "%")
    
    if prediction == 1:
        st.error("⚠ High Risk Customer")
    else:
        st.success("✅ Low Risk Customer")
