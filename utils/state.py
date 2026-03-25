import streamlit as st

def initialize_session_state():
    if "datasets" not in st.session_state:
        st.session_state.datasets = {}
    if "active_table" not in st.session_state:
        st.session_state.active_table = None
        import streamlit as st

def init_session_state():
    defaults = {
        "datasets": {},
        "active_table": None,
        "cleaned_data": None,
        "merged_data": None,
    }

    for key, value in defaults.items():
        if key not in st.session_state:
            st.session_state[key] = value