import streamlit as st
st.write("Hello World")
st.title("Welcome")
a=st.text_input("Enter a Value:")
b=st.number_input("Enter a Number:",min_value=0,max_value=100)
st.success("Success")
st.warning("Warning")
st.info("Information")
st.balloons()