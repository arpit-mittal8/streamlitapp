# main.py
import streamlit as st
import page1
import brain_tumor_classification
import park_pred  # Import the Parkinson's page module

# Initialize session state
if 'page' not in st.session_state:
    st.session_state.page = 'home'

# Navigation based on session state
if st.session_state.page == 'home':
    page1.main()
elif st.session_state.page == 'brain_tumor_classification':
    brain_tumor_classification.main()
elif st.session_state.page == 'park_pred':  # Update to 'park_pred' for Parkinson's page
    park_pred.main()
