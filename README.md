🎬 Netflix Churn Prediction App
📌 Problem Statement

Customer churn is a major challenge for subscription-based platforms like Netflix.
Losing customers directly impacts recurring revenue and business growth.

This project predicts whether a customer is likely to cancel their subscription based on behavioral engagement metrics.

🎯 Objective: Identify high-risk customers early and enable proactive retention strategies.

📊 Dataset Overview

The model uses key behavioral features:

Avg_watch_time_per_day – Average daily watch time in hours

Last_login_days – Days since last platform login

Number_of_Profile – Number of profiles in the account

Monthly Fee ($) – Subscription plan amount

Target Variable: Churned (0 = No, 1 = Yes)

Input values are restricted within training data distribution to ensure reliable predictions.

🤖 Model Approach

Feature selection based on importance

GradientBoostingClassifier

StandardScaler using ColumnTransformer

80–20 Train-Test Split

Risk segmentation using probability thresholds

📈 Model Performance
Metric	Score
Accuracy	92%
F1 Score	92%
ROC-AUC	98.4%

The model maintains high predictive power even after reducing to top behavioral features.

🚀 Live Demo

Click below to try the deployed application:

👉 Netflix Churn Prediction App

https://netflix-churn-prediction-ukekkixfwkxupftabj3p3z.streamlit.app/

🛠 Tech Stack

Python

Scikit-learn

Gradient Boosting

ColumnTransformer

Streamlit

GitHub

Streamlit Cloud Deployment
