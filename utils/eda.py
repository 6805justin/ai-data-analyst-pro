import pandas as pd

def dataset_overview(df: pd.DataFrame):
    return {
        "rows": df.shape[0],
        "columns": df.shape[1],
        "duplicates": int(df.duplicated().sum())
    }

def missing_values_report(df: pd.DataFrame) -> pd.DataFrame:
    report = pd.DataFrame({
        "column": df.columns,
        "missing_count": df.isnull().sum().values,
        "missing_pct": (df.isnull().sum().values / len(df) * 100).round(2)
    })
    return report.sort_values(by="missing_pct", ascending=False)

def summary_stats(df: pd.DataFrame) -> pd.DataFrame:
    try:
        return df.describe(include="all").transpose()
    except Exception:
        return pd.DataFrame()

def detect_date_columns(df: pd.DataFrame):
    possible_dates = []
    for col in df.columns:
        if "date" in col.lower() or "time" in col.lower():
            possible_dates.append(col)
    return possible_dates