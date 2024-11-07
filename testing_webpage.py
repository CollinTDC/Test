# Importing necessary libraries
import streamlit as st

# Title of the webpage
st.title("Basic Streamlit Webpage")

# Adding a header
st.header("Welcome to My Streamlit Webpage")

# Adding a subheader
st.subheader("This is a simple Streamlit example")

# Adding text
st.text("Streamlit is an open-source app framework for Machine Learning and Data Science projects.")

# Adding user input
name = st.text_input("Enter your name:", "")

# Displaying user input
if name:
    st.write(f"Hello, {name}! Welcome to this Streamlit app!")

# Adding a button
if st.button("Click me"):
    st.write("You clicked the button!")

# Adding a selectbox
option = st.selectbox(
    "Select a number:",
    [1, 2, 3, 4, 5]
)

st.write(f"You selected: {option}")

# Adding a slider
slider_value = st.slider("Select a value:", 0, 100, 50)
st.write(f"Slider value: {slider_value}")

# Adding an image (from URL)
st.image("https://www.streamlit.io/images/brand/streamlit-logo-secondary-colormark-darktext.png", caption="Streamlit Logo")

# Run this script with: `streamlit run app.py`
