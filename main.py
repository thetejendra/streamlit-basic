import streamlit as st
import pandas as pd

st.title("Hey! Join Our Community")
st.header("Enter your details")

name = st.text_input("Enter your name: ")
fname = st.text_input("Enter your father's name: ")
mname = st.text_input("Enter your mother's name: ")
add = st.text_area("Enter your address :")

button = st.button("Submit")

# to show input
# if button:
#     st.markdown(f"""
#     Name : {name}
#     Father Name :{fname}
#     Mother Name :{mname}
#     Address : {add}
# """)


