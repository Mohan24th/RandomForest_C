import streamlit as st
import pandas as pd
import joblib

# Load model
model = joblib.load("income_model.pkl")
model_columns = joblib.load("model_columns.pkl")

st.set_page_config(
    page_title="Income Prediction",
    page_icon="💰",
    layout="centered"
)

st.title("💰 Income Prediction System")
st.write("Predict whether a person earns more than $50K annually.")

st.divider()

# User Inputs
age = st.slider("Age", 18, 70, 30)

gender = st.selectbox(
    "Gender",
    ["Male", "Female"]
)

education = st.selectbox(
    "Education",
    [
        "Bachelors",
        "Masters",
        "HS-grad",
        "Some-college",
        "Doctorate"
    ]
)

occupation = st.selectbox(
    "Occupation",
    [
        "Exec-managerial",
        "Sales",
        "Tech-support",
        "Craft-repair",
        "Prof-specialty"
    ]
)

hours_per_week = st.slider(
    "Hours Worked Per Week",
    1,
    80,
    40
)

capital_gain = st.number_input(
    "Capital Gain",
    min_value=0,
    value=0
)

# Predict Button
if st.button("Predict Income"):

    input_data = {
        "age": age,
        "hours-per-week": hours_per_week,
        "capital-gain": capital_gain,
        "gender": 1 if gender == "Male" else 0
    }

    # Create dataframe
    input_df = pd.DataFrame([input_data])

    # Add missing columns
    for col in model_columns:
        if col not in input_df.columns:
            input_df[col] = 0

    # Reorder columns
    input_df = input_df[model_columns]

    # Prediction
    prediction = model.predict(input_df)[0]
    probability = model.predict_proba(input_df)[0]

    st.divider()

    if prediction == 1:
        st.success("✅ Likely earns more than $50K annually")
        st.metric(
            "Confidence",
            f"{round(max(probability)*100,2)}%"
        )
    else:
        st.error("❌ Likely earns less than or equal to $50K annually")
        st.metric(
            "Confidence",
            f"{round(max(probability)*100,2)}%"
        )

    st.subheader("Why this prediction?")
    
    reasons = []

    if education in ["Masters", "Doctorate", "Bachelors"]:
        reasons.append("Higher education level")

    if hours_per_week > 45:
        reasons.append("Works longer weekly hours")

    if occupation == "Exec-managerial":
        reasons.append("Management occupation")

    if age > 35:
        reasons.append("More work experience")

    if reasons:
        for r in reasons:
            st.write("•", r)