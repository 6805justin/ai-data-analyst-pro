
from io import StringIO
import os
import re

import streamlit as st
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()


def get_api_key():
    env_key = os.getenv("OPENAI_API_KEY")
    if env_key:
        return env_key

    try:
        return st.secrets["OPENAI_API_KEY"]
    except Exception:
        return None


api_key = get_api_key()

if not api_key:
    raise ValueError(
        "No OpenAI API key found. Add OPENAI_API_KEY to your .env file locally, "
        "or add it to Streamlit secrets after deployment."
    )

client = OpenAI(api_key=api_key)


def clean_sql_response(sql_text: str) -> str:
    sql_text = sql_text.strip()

    sql_text = re.sub(r"^```sql\s*", "", sql_text, flags=re.IGNORECASE)
    sql_text = re.sub(r"^```\s*", "", sql_text)
    sql_text = re.sub(r"\s*```$", "", sql_text)

    return sql_text.strip()


def generate_sql(question: str, table_name: str, schema: str) -> str:
    prompt = f"""
You are a data analyst writing SQL for SQLite.

Important rules:
- Use SQLite syntax only.
- Do NOT use DATE_TRUNC.
- For month grouping in SQLite, use: strftime('%Y-%m', "column name")
- Use ONLY the exact table name provided.
- Use ONLY the exact column names from the schema.
- If a column name has spaces, wrap it in double quotes.
- Return ONLY the SQL query.
- Do NOT return markdown.
- Do NOT use code fences.
- Generate only SELECT queries.

Table name:
{table_name}

Schema:
{schema}

User question:
{question}
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You generate valid SQLite SELECT queries only."},
            {"role": "user", "content": prompt}
        ],
        temperature=0
    )

    raw_sql = response.choices[0].message.content.strip()
    return clean_sql_response(raw_sql)


def generate_business_insight(question: str, result_df) -> str:
    csv_buffer = StringIO()
    result_df.head(20).to_csv(csv_buffer, index=False)

    prompt = f"""
You are a business analyst.

The user asked:
{question}

The result sample is:
{csv_buffer.getvalue()}

Write 2 short lines explaining the key takeaway clearly.
"""

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": "You explain analytics results clearly for business users."},
            {"role": "user", "content": prompt}
        ],
        temperature=0.2
    )

    return response.choices[0].message.content.strip()