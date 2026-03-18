import streamlit as st
from utils.ui import apply_theme, render_sidebar
apply_theme()
render_sidebar()
st.title("Export")

if st.session_state.active_table and st.session_state.active_table in st.session_state.datasets:
    current_df = st.session_state.datasets[st.session_state.active_table]
    st.subheader("Download current dataset")
    st.download_button(
        "Download current dataset CSV",
        current_df.to_csv(index=False),
        file_name=f"{st.session_state.active_table}.csv",
        mime="text/csv"
    )
else:
    st.info("No dataset available yet.")

if "query_result" in st.session_state and st.session_state.query_result is not None:
    st.subheader("Download latest query result")
    st.download_button(
        "Download query result CSV",
        st.session_state.query_result.to_csv(index=False),
        file_name="query_result.csv",
        mime="text/csv"
    )
else:
    st.info("No query result available yet.")