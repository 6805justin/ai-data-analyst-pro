import streamlit as st
from utils.eda import dataset_overview, missing_values_report, summary_stats, detect_date_columns
from utils.ui import apply_theme, render_sidebar
apply_theme()
render_sidebar()
st.title("EDA Report")

if not st.session_state.datasets or not st.session_state.active_table:
    st.warning("Please upload a dataset first.")
else:
    df = st.session_state.datasets[st.session_state.active_table]

    overview = dataset_overview(df)

    col1, col2, col3 = st.columns(3)
    col1.metric("Rows", overview["rows"])
    col2.metric("Columns", overview["columns"])
    col3.metric("Duplicates", overview["duplicates"])

    st.subheader("Missing Values")
    st.dataframe(missing_values_report(df), use_container_width=True)

    st.subheader("Summary Statistics")
    stats_df = summary_stats(df)
    if not stats_df.empty:
        st.dataframe(stats_df, use_container_width=True)
    else:
        st.info("No summary statistics available.")

    st.subheader("Possible Date Columns")
    date_cols = detect_date_columns(df)
    if date_cols:
        st.success(f"Detected date columns: {', '.join(date_cols)}")
    else:
        st.write("No obvious date columns detected.")