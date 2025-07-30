import streamlit as st

st.title("Factorial Calculator")

def factorial():
    n = int(st.number_input("Enter an integer:"))
    initial=n
    result=n
    for i in range(n-2):
        result=result*(n-1)
        n-=1
        st.write(result)
    st.write(f"\nThe factorial of {initial} is {result}.")

factorial()

import streamlit as st
import numpy as np

st.title("Trigonometric Ratio Calculator")
st.write("Calculate sine, cosine, and tangent for any angle in degrees.")

# Input: Angle in degrees
angle_deg = st.number_input("Enter angle in degrees:", value=0.0, step=0.1, format="%.2f")

# Convert degrees to radians
angle_rad = np.deg2rad(angle_deg)

# Calculate sine, cosine, tangent
sine = np.sin(angle_rad)
cosine = np.cos(angle_rad)
try:
    tangent = np.tan(angle_rad)
except Exception:
    tangent = float('nan')

st.markdown(f"### Results for {angle_deg}°:")
st.write(f"**Sine (sin):** {sine:.6f}")
st.write(f"**Cosine (cos):** {cosine:.6f}")

# Handle undefined tangent (e.g., 90°, 270°, etc.)
if np.isclose(cosine, 0.0):
    st.write("**Tangent (tan):** undefined")
else:
    st.write(f"**Tangent (tan):** {tangent:.6f}")

st.caption("Powered by Streamlit and NumPy.")
