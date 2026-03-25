import re
import pandas as pd
import streamlit as st
from utils.db import save_df_to_sqlite
from utils.ui import apply_theme, render_sidebar
apply_theme()
render_sidebar()

if "datasets" not in st.session_state:
    st.session_state.datasets = {}

if "active_table" not in st.session_state:
    st.session_state.active_table = None

st.title("Upload and Preview")

uploaded_file = st.file_uploader("Upload CSV", type=["csv"])

if uploaded_file:
    try:
        df = pd.read_csv(uploaded_file)

        table_name = re.sub(r"[^a-zA-Z0-9_]", "_", uploaded_file.name.split(".")[0].lower())

        st.session_state.datasets[table_name] = df
        st.session_state.active_table = table_name

        save_df_to_sqlite(df, table_name)

        st.success(f"File uploaded and saved as table: {table_name}")

    except Exception as e:
        st.error(f"Upload failed: {e}")

if st.session_state.active_table:
    df = st.session_state.datasets[st.session_state.active_table]
    st.subheader("Preview")
    st.dataframe(df.head(), use_container_width=True)