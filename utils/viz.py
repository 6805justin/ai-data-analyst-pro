import pandas as pd
import plotly.express as px


def create_chart(df: pd.DataFrame):
    if df is None or df.empty or len(df.columns) < 2:
        return None

    x_col = df.columns[0]
    numeric_cols = df.select_dtypes(include="number").columns.tolist()

    if not numeric_cols:
        return None

    y_col = numeric_cols[0]

    if df[x_col].nunique() <= 20:
        return px.bar(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}")

    return px.line(df, x=x_col, y=y_col, title=f"{y_col} by {x_col}")