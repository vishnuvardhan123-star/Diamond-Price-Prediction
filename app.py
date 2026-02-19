import streamlit as st
import pandas as pd
import pickle

# ---------------- LOAD MODEL ----------------
with open("diamond_model.pkl", "rb") as file:
    model = pickle.load(file)

st.set_page_config(page_title="Diamond Price Prediction", layout="centered")
st.title("💎 Diamond Price Prediction App")

st.write("Enter diamond details to predict its price")

# ---------------- NUMERICAL INPUTS ----------------
carat = st.number_input("Carat", min_value=0.1, max_value=5.0, value=1.0, step=0.01)
depth = st.number_input("Depth (%)", min_value=40.0, max_value=80.0, value=61.5)
table = st.number_input("Table (%)", min_value=40.0, max_value=80.0, value=57.0)
x = st.number_input("Length (x) in mm", min_value=0.0, value=6.5)
y = st.number_input("Width (y) in mm", min_value=0.0, value=6.5)
z = st.number_input("Height (z) in mm", min_value=0.0, value=4.0)

# ---------------- CATEGORICAL INPUTS ----------------
cut = st.selectbox("Cut", ["Fair", "Good", "Very Good", "Premium", "Ideal"])
color = st.selectbox("Color", ["D", "E", "F", "G", "H", "I", "J"])
clarity = st.selectbox(
    "Clarity",
    ["I1", "SI2", "SI1", "VS2", "VS1", "VVS2", "VVS1", "IF"]
)

# ---------------- CREATE INPUT DATAFRAME ----------------
input_data = pd.DataFrame({
    "carat": [carat],
    "cut": [cut],
    "color": [color],
    "clarity": [clarity],
    "depth": [depth],
    "table": [table],
    "x": [x],
    "y": [y],
    "z": [z]
})

# ---------------- PREDICTION ----------------
if st.button("💰 Predict Diamond Price"):
    price = abs(model.predict(input_data)[0])

    st.success(f"💎 Estimated Diamond Price: **${price:,.2f}**")