import streamlit as st

st.title("Factorial Calculator")

n = st.number_input("Enter an integer:", min_value=0, step=1, format="%d")

def compute_factorial(x):
    if x == 0 or x == 1:
        return 1
    result = 1
    for i in range(2, x+1):
        result *= i
    return result

if st.button("Calculate"):
    result = compute_factorial(n)
    st.write(f"The factorial of {int(n)} is {result}.")
