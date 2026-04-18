import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt
import os

# ---------------------------
# Load model (works local + cloud)
# ---------------------------
model_path = os.path.join(os.path.dirname(__file__), "model.pkl")
model = pickle.load(open(model_path, "rb"))

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="Customer Intelligence App", layout="centered")

# ---------------------------
# Title
# ---------------------------
st.markdown(
    "<h1 style='text-align: center; color: #00C897;'>Customer Intelligence Dashboard 🚀</h1>",
    unsafe_allow_html=True
)
st.markdown("Enter customer details to predict churn probability")

# ---------------------------
# Input layout (with default values)
# ---------------------------
col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input("Recency (days)", min_value=0, value=30)

with col2:
    frequency = st.number_input("Frequency", min_value=0, value=10)

with col3:
    monetary = st.number_input("Monetary Value", min_value=0.0, value=500.0)

# ---------------------------
# Predict button
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

    # ---------------------------
    # Probability
    # ---------------------------
    try:
        prob = model.predict_proba(input_data)[0][1]
        st.info(f"Churn Probability: {round(prob * 100, 2)}%")
    except:
        st.warning("Probability not available")

    # ---------------------------
    # Visualization
    # ---------------------------
    fig, ax = plt.subplots()
    ax.bar(['Recency', 'Frequency', 'Monetary'], [recency, frequency, monetary])
    ax.set_title("Customer Input Overview")
    st.pyplot(fig)

# ---------------------------
# Footer
# ---------------------------
st.markdown("---")
st.caption("Built by Nishant Tyagi | Data Science Project")