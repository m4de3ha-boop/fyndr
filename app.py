import streamlit as st
import staff_panel
import student_panel

st.set_page_config(page_title="FYNDR", layout="wide")

st.title("🔍 FYNDR — School Lost & Found")

page = st.sidebar.radio("Go to:", ["Staff Panel", "Student Panel"])

if page == "Staff Panel":
    staff_panel.run()
elif page == "Student Panel":
    student_panel.run()
