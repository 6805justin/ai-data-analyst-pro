import streamlit as st
from utils.cleaning import remove_duplicates, fill_missing, drop_columns, convert_to_datetime
from utils.db import save_df_to_sqlite
from utils.ui import apply_theme, render_sidebar
apply_theme()
render_sidebar()
st.title("Clean and Transform Data")

if not st.session_state.datasets or not st.session_state.active_table:
    st.warning("Please upload a dataset first.")
else:
    df = st.session_state.datasets[st.session_state.active_table]

    st.subheader("Current Data")
    st.dataframe(df.head())

    # 🔹 Remove duplicates
    if st.button("Remove Duplicates"):
        df = remove_duplicates(df)
        st.success("Duplicates removed")

    # 🔹 Fill missing
    strategy = st.selectbox("Missing Value Strategy", ["mean", "median"])
    if st.button("Fill Missing Values"):
        df = fill_missing(df, strategy)
        st.success("Missing values handled")

    # 🔹 Drop columns
    cols_to_drop = st.multiselect("Select columns to drop", df.columns)
    if st.button("Drop Selected Columns"):
        df = drop_columns(df, cols_to_drop)
        st.success("Columns dropped")

    # 🔹 Convert dates
    date_cols = st.multiselect("Convert to datetime", df.columns)
    if st.button("Convert to Datetime"):
        df = convert_to_datetime(df, date_cols)
        st.success("Converted to datetime")

    # Save updated dataframe
    st.session_state.datasets[st.session_state.active_table] = df
    save_df_to_sqlite(df, st.session_state.active_table)

    st.subheader("Updated Data")
    st.dataframe(df.head())