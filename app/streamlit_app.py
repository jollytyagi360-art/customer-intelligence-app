import streamlit as st
import pickle
import pandas as pd

# ---------------------------
# Load model (FIXED PATH)
# ---------------------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------------------
# Page Config
# ---------------------------
st.set_page_config(
    page_title="Customer Intelligence App",
    layout="centered"
)

# ---------------------------
# Title
# ---------------------------
st.title("📊 Customer Churn Prediction System")
st.markdown("Enter customer details to predict churn probability")

# ---------------------------
# Input Layout
# ---------------------------
col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input("Recency (days)", min_value=0)

with col2:
    frequency = st.number_input("Frequency", min_value=0)

with col3:
    monetary = st.number_input("Monetary Value", min_value=0.0)

# ---------------------------
# Predict Button
# ---------------------------
if st.button("Predict"):

    input_data = pd.DataFrame(
        [[recency, frequency, monetary]],
        columns=['Recency', 'Frequency', 'Monetary']
    )

    prediction = model.predict(input_data)

    # ---------------------------
    # Output
    # ---------------------------
    if prediction[0] == 1:
        st.error("⚠️ High Risk: Customer likely to churn")
    else:
        st.success("✅ Customer is active")
