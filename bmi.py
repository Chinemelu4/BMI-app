import streamlit as st
from PIL import Image

st.title("BMI Calculator")
st.subheader("Calculate your BMI")

def bmi_calc(weight, height):
    bmi = weight / (height ** 2)
    return round(bmi,2)

def bmi_reading(bmi):
    if bmi >= 30:
        return "You are at risk of being obese"
    elif 25 <= bmi < 30:
        return "You are at risk of being overweight"
    elif 18.5 <= bmi < 25:
        return "You are healthy"
    else:
        return "You are at risk of being underweight"
    
img = Image.open("bmi.jpeg")
st.sidebar.image(img)

st.image("heart.gif")
st.sidebar.write("BMI is a measure of body mass index. It evaluattes the body's weight relative to its height.")
    
weight = st.number_input("Enter your weight in kg", step=1)
height = st.number_input("Enter your height in m")

if st.button("Calculate"):
    bmi = bmi_calc(weight, height)
    reading = bmi_reading(bmi)
    st.write(f"Your BMI is {bmi} and {reading}")