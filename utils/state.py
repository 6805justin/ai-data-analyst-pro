import streamlit as st

def initialize_session_state():
    if "datasets" not in st.session_state:
        st.session_state.datasets = {}

    if "active_table" not in st.session_state:
        st.session_state.active_table = None

    if "cleaned_data" not in st.session_state:
        st.session_state.cleaned_data = None

    if "merged_data" not in st.session_state:
        st.session_state.merged_data = None