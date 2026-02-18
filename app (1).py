import streamlit as st
import pandas as pd
import joblib

# Load trained pipeline model
model = joblib.load("churn_top4_model.pkl")

st.set_page_config(page_title="Netflix Churn Predictor", layout="centered")

st.title("🎬 Netflix Churn Prediction App")
st.write("Enter customer behavioral details below:")

# ---------------- INPUTS ---------------- #

avg_watch_time = st.slider(
    "Avg Watch Time Per Day (hours)",
    min_value=0.0,
    max_value=12.0,
    value=3.0,
    step=0.1
)

last_login_days = st.slider(
    "Days Since Last Login",
    min_value=0,
    max_value=60,
    value=5
)

num_profiles = st.slider(
    "Number of Profiles",
    min_value=1,
    max_value=5,
    value=2
)

monthly_fee = st.selectbox(
    "Monthly Fee ($)",
    [8.99, 13.99, 17.99]
)

# ---------------- PREDICTION ---------------- #

if st.button("Predict Churn Risk"):

    input_data = pd.DataFrame([{
        "Avg_watch_time_per_day": avg_watch_time,
        "Last_login_days": last_login_days,
        "Number_of_Profile": num_profiles,
        "Monthly Fee ($)": monthly_fee
    }])

    probability = model.predict_proba(input_data)[0][1]

    st.subheader("Prediction Result")

    st.write("Churn Probability:", round(probability * 100, 2), "%")

    # Risk Categories
    if probability > 0.7:
        st.error("🔴 High Risk Customer")
    elif probability > 0.4:
        st.warning("🟡 Medium Risk Customer")
    else:
        st.success("🟢 Low Risk Customer")

