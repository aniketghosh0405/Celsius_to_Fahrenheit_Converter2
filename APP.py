import streamlit as st

# App title
st.title("🌡️ Celsius to Fahrenheit Converter")

# User input
celsius = st.number_input(
    "Please put the current temperature in Celsius:",
    value=0.0,
    step=0.1
)

# Convert Celsius to Fahrenheit
fahrenheit = (celsius * 9 / 5) + 32

# Display the result
st.success(f"Your converted temperature in Fahrenheit is: {fahrenheit:.2f} °F")