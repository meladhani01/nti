# Save this code as a Python file (e.g., app.py) and use it in your Streamlit application.


import streamlit as st
import pandas as pd
import joblib

# Load the saved model pipeline
try:
    rf_pipe = joblib.load('random_forest_pipeline.joblib')
except FileNotFoundError:
    st.error("Error: 'random_forest_pipeline.joblib' not found. Please ensure the model file is in the same directory.")
    st.stop()

def predict_deficit(data: pd.DataFrame)  > str:

    """


    Predicts the deficit flag (Yes/No) using the loaded Random Forest pipeline.

    Args:
      data: DataFrame containing new data with the same columns as
            the training data (excluding 'Cons_Total_MWh' and 'Deficit_Flag').

    Returns:
      A string indicating whether a deficit is predicted ('Yes' or 'No').
    """
    if rf_pipe is not None:
        prediction = rf_pipe.predict(data)
        return "Yes" if prediction[0] == 1 else "No"
    else:
        return "Model not loaded"

# --- Streamlit App ---

st.title("Energy Deficit Prediction App")

st.write("Enter the details below to predict if there will be an energy deficit.")

# Add input fields for the features (example for a few, add all relevant features)
city = st.text_input("City")
state = st.text_input("State")
year = st.number_input("Year", min_value=2018, max_value=2030, value=2023)
month = st.number_input("Month", min_value=1, max_value=12, value=1)
population = st.number_input("Population", min_value=0, value=100000)
households = st.number_input("Households", min_value=0, value=30000)
businesses = st.number_input("Businesses", min_value=0, value=500)
gen_gas = st.number_input("Gen_Gas_MWh", min_value=0.0, value=5000.0)


gen_coal = st.number_input("Gen_Coal_MWh", min_value=0.0, value=2000.0)



gen_renew = st.number_input("Gen_Renew_MWh", min_value=0.0, value=1500.0)




gen_total = st.number_input("Gen_Total_MWh", min_value=0.0, value=8500.0)




cons_household = st.number_input("Cons_Household_MWh", min_value=0.0, value=100000.0)






cons_commercial = st.number_input("Cons_Commercial_MWh", min_value=0.0, value=10000.0)








cons_industrial = st.number_input("Cons_Industrial_MWh", min_value=0.0, value=1000.0)










energy_wasted = st.number_input("Energy_Wasted_MWh", min_value=0.0, value=500.0)












renewable_share = st.number_input("Renewable_Share_pct", min_value=0.0, max_value=100.0, value=20.0)
avg_income = st.number_input("Avg_Income_USD", min_value=0.0, value=50000.0)
energy_per_capita = st.number_input("Energy_per_capita_kWh", min_value=0.0, value=400.0)

















# Create a dictionary from the input values
input_data = {
    'City': [city],
    'State': [state],
    'Year': [year],
    'Month': [month],
    'Population': [population],
    'Households': [households],

    'Businesses': [businesses],
    'Gen_Gas_MWh': [gen_gas],










    'Gen_Coal_MWh': [gen_coal],

    'Gen_Renew_MWh': [gen_renew],

    'Gen_Total_MWh': [gen_total],

    'Cons_Household_MWh': [cons_household],


    'Cons_Commercial_MWh': [cons_commercial],



    'Cons_Industrial_MWh': [cons_industrial],


    'Energy_Wasted_MWh': [energy_wasted],




    'Renewable_Share_pct': [renewable_share],
    'Avg_Income_USD': [avg_income],
    'Energy_per_capita_kWh': [energy_per_capita]


}

# Create a DataFrame

input_df = pd.DataFrame(input_data)


if st.button("Predict"):
    prediction_result = predict_deficit(input_df)
    st.success(f"Predicted Energy Deficit: {prediction_result}")



st.write("Note: This is a simplified example. You would typically deploy this model as a web service and consume it from your Streamlit app.")




















































































