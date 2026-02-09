import streamlit as st

if 'length' not in st.session_state:
    st.session_state.length = 0.0
if 'width' not in st.session_state:
    st.session_state.width = 0.0

# Initialize
st.title("Area and Perimeter")
length = st.number_input("Enter the length", value=st.session_state.length) # defaults come from the session state
width = st.number_input("Enter the width",value=st.session_state.width)
btn_clicked =st.button("Calculate")
btn_clear = st.button("Clear")

#checks when clicked
if btn_clicked:
    area = length * width
    perimeter = 2*(length + width)
    st.write(f"Area:{area}")
    st.write(f"Perimeter:{perimeter}")

# reset by clearing
if btn_clear:
    st.session_state.length = None
    st.session_state.width = None
    st.rerun()  











