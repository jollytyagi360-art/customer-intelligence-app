import streamlit as st
import pickle
import pandas as pd
import matplotlib.pyplot as plt

# ---------------------------
# Load model
# ---------------------------
model = pickle.load(open("model.pkl", "rb"))

# ---------------------------
# Page config
# ---------------------------
st.set_page_config(page_title="Customer Intelligence App", layout="centered")

# ---------------------------
# Title
# ---------------------------
st.markdown(
    "<h1 style='text-align: center; color: #4CAF50;'>Customer Intelligence Dashboard</h1>",
    unsafe_allow_html=True
)
st.markdown("Enter customer details to predict churn probability")

# ---------------------------
# Input layout
# ---------------------------
col1, col2, col3 = st.columns(3)

with col1:
    recency = st.number_input("Recency (days)", min_value=0)

with col2:
    frequency = st.number_input("Frequency", min_value=0)

with col3:
    monetary = st.number_input("Monetary Value", min_value=0.0)

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
        st.write(f"Churn Probability: {round(prob * 100, 2)}%")
    except:
        st.write("Probability not available for this model")

    # ---------------------------
    # Visualization
    # ---------------------------
    fig, ax = plt.subplots()
    ax.bar(['Recency', 'Frequency', 'Monetary'], [recency, frequency, monetary])
    ax.set_title("Customer Input Overview")
    st.pyplot(fig)