import streamlit as st
from utils.state import initialize_session_state
from utils.ui import apply_theme, render_sidebar, initialize_ui_state
from utils.state import initialize_session_state

initialize_session_state()
st.set_page_config(
    page_title="AI Data Analyst Pro",
    page_icon="📊",
    layout="wide"
)

initialize_session_state()
initialize_ui_state()
apply_theme()
render_sidebar()

st.markdown("""
<div class="hero-card">
    <h1>AI Data Analyst Pro 📊</h1>
    <p style="font-size:1.08rem; margin-bottom:0.6rem;">
        Turn raw datasets into charts, SQL, and business insights using plain English.
    </p>
    <p class="small-muted" style="margin-bottom:0;">
        Upload → Explore → Clean → Ask → Visualize → Export
    </p>
</div>
""", unsafe_allow_html=True)

st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="feature-card">
        <h3>📁 Upload & Explore</h3>
        <p class="small-muted">
            Upload one or more CSV files and preview them instantly.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="feature-card">
        <h3>🧹 Clean & Prepare</h3>
        <p class="small-muted">
            Handle missing values, standardize text, convert dates, and merge files.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="feature-card">
        <h3>🤖 Ask Your Data</h3>
        <p class="small-muted">
            Ask business questions in plain English and get SQL, charts, and insight.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.write("")

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown('<div class="metric-card"><h3>CSV Upload</h3><p class="small-muted">Fast dataset ingestion</p></div>', unsafe_allow_html=True)
with m2:
    st.markdown('<div class="metric-card"><h3>EDA</h3><p class="small-muted">Stats, duplicates, missing values</p></div>', unsafe_allow_html=True)
with m3:
    st.markdown('<div class="metric-card"><h3>AI Query</h3><p class="small-muted">Natural language to SQL</p></div>', unsafe_allow_html=True)
with m4:
    st.markdown('<div class="metric-card"><h3>Export</h3><p class="small-muted">Download data and results</p></div>', unsafe_allow_html=True)

st.write("")
st.subheader("How to use")
st.markdown("""
1. Go to **Upload and Preview** and upload a CSV  
2. Open **EDA Report** to inspect the dataset  
3. Use **Clean and Merge** to prepare your data  
4. Open **Ask Data** and ask your question  
5. Use **Export** to download outputs  
""")

st.subheader("Best example questions")
st.write("- Show total sales by segment")
st.write("- Show total sales by category")
st.write("- Show average sales by state")
st.write("- Show total sales by month")
st.markdown("""
<div class="feature-card">
    <h3>✨ What makes this different</h3>
    <p class="small-muted">
        This app is not just a dashboard. It supports real analyst workflows:
        data upload, EDA, cleaning, merging, AI querying, charting, and export.
    </p>
</div>
""", unsafe_allow_html=True)