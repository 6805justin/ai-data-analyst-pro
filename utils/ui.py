import streamlit as st

def initialize_ui_state():
    if "query_history" not in st.session_state:
        st.session_state.query_history = []

def apply_theme():
    st.markdown("""
    <style>
    :root {
        --bg: #0f172a;
        --card: #1e293b;
        --card-2: #111827;
        --text: #e2e8f0;
        --muted: #94a3b8;
        --border: #334155;
        --accent: #facc15;
    }

    .stApp {
        background-color: var(--bg);
        color: var(--text);
    }

    .block-container {
        padding-top: 1.8rem;
        padding-bottom: 2rem;
    }

    /* SIDEBAR */
    section[data-testid="stSidebar"] {
        background: linear-gradient(180deg, #111827, #0f172a);
        border-right: 1px solid #1f2937;
    }

    section[data-testid="stSidebar"] * {
        color: #e5e7eb !important;
    }

    /* HERO */
    .hero-card {
        background: linear-gradient(135deg, #1e293b, #0f172a);
        padding: 2.4rem;
        border-radius: 22px;
        color: #f8fafc;
        box-shadow: 0 10px 35px rgba(0,0,0,0.35);
        border: 1px solid #334155;
        animation: fadeIn 0.7s ease-in-out;
    }

    /* FEATURE CARDS */
    .feature-card {
        background: var(--card);
        padding: 1.3rem;
        border-radius: 18px;
        border: 1px solid var(--border);
        box-shadow: 0 6px 18px rgba(0,0,0,0.22);
        color: var(--text);
        transition: transform 0.2s ease;
    }

    .feature-card:hover {
        transform: translateY(-4px);
    }

    /* METRIC CARDS */
    .metric-card {
        background: var(--card-2);
        padding: 1rem;
        border-radius: 16px;
        border: 1px solid #374151;
        text-align: center;
    }

    /* TEXT */
    .small-muted {
        color: var(--muted);
    }

    /* HEADINGS */
    h1, h2, h3 {
        color: var(--accent);
    }

    /* BUTTON */
    div.stButton > button {
        background: linear-gradient(135deg, #facc15, #eab308);
        color: #111827;
        border-radius: 12px;
        font-weight: 600;
    }

    /* INPUT FIX */
    input, textarea {
        color: white !important;
    }

    div[data-baseweb="select"] * {
        color: white !important;
    }

    /* QUERY HISTORY */
    .query-history-card {
        background: #111827;
        border: 1px solid #374151;
        padding: 0.9rem;
        border-radius: 14px;
        margin-bottom: 0.7rem;
    }

    @keyframes fadeIn {
        from {opacity: 0; transform: translateY(12px);}
        to {opacity: 1; transform: translateY(0);}
    }
    </style>
    """, unsafe_allow_html=True)


def render_sidebar():
    with st.sidebar:
        st.markdown("## AI Data Analyst Pro")
        st.caption("AI-powered analytics workspace")

        st.markdown("---")

        st.markdown("### Workflow")
        st.write("1. Upload and Preview")
        st.write("2. EDA Report")
        st.write("3. Clean and Merge")
        st.write("4. Ask Data")
        st.write("5. Export")

        st.markdown("---")

        st.markdown("### Sample Questions")
        st.write("• Show total sales by segment")
        st.write("• Show total sales by category")
        st.write("• Show average sales by state")
        st.write("• Show total sales by month")


def add_query_to_history(question, sql, rows):
    st.session_state.query_history.insert(0, {
        "question": question,
        "sql": sql,
        "rows": rows
    })
    st.session_state.query_history = st.session_state.query_history[:8]


def render_query_history():
    st.subheader("Recent Queries")

    if not st.session_state.query_history:
        st.info("No queries yet.")
        return

    for q in st.session_state.query_history:
        st.markdown(f"""
        <div class="query-history-card">
            <strong>Question:</strong> {q["question"]}<br>
            <strong>Rows:</strong> {q["rows"]}
        </div>
        """, unsafe_allow_html=True)

        st.code(q["sql"], language="sql")