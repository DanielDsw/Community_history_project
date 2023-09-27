import streamlit as st

def h(header,write):  
  st.header(header)
  st.write(write)

def sh(s_header,write):
  st.subheader(s_header)
  st.write(write)