import streamlit as st
from utils.llm import generate_sql, generate_business_insight
from utils.db import run_query, get_schema
from utils.viz import create_chart
from utils.ui import apply_theme, render_sidebar, add_query_to_history, render_query_history

apply_theme()
render_sidebar()

st.title("Ask Your Data")

if not st.session_state.datasets or not st.session_state.active_table:
    st.warning("Upload data first.")
else:
    table_name = st.session_state.active_table
    schema = get_schema(table_name)

    left_col, right_col = st.columns([2, 1])

    with left_col:
        st.subheader("Ask a question about your data")
        st.caption("Example: Show total sales by month")

        st.markdown("### Try questions like:")
        st.write("- Show total sales by segment")
        st.write("- Show total sales by category")
        st.write("- Show average sales by state")
        st.write("- Show total sales by month")

        question = st.text_input("Enter your question")

        with st.expander("Current schema"):
            st.code(schema)

        if st.button("Run Query") and question:
            try:
                with st.spinner("Thinking through your data and generating SQL..."):
                    sql = generate_sql(question, table_name, schema)

                st.subheader("Generated SQL")
                st.code(sql, language="sql")

                with st.spinner("Running query and building results..."):
                    result = run_query(sql)
                    st.session_state.query_result = result

                add_query_to_history(question, sql, len(result))

                st.subheader("Result")
                st.dataframe(result, use_container_width=True)
                st.write(f"Rows returned: {len(result)}")

                fig = create_chart(result)
                if fig is not None:
                    st.subheader("Chart")
                    st.plotly_chart(fig, use_container_width=True)

                if not result.empty:
                    with st.spinner("Writing a business-friendly explanation..."):
                        insight = generate_business_insight(question, result)
                    st.subheader("Business Insight")
                    st.write(insight)

            except Exception as e:
                st.error(f"Something went wrong: {e}")

    with right_col:
        render_query_history()