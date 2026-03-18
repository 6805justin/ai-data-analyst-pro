import pandas as pd

def remove_duplicates(df: pd.DataFrame):
    return df.drop_duplicates()

def drop_columns(df: pd.DataFrame, cols):
    return df.drop(columns=cols)

def fill_missing(df: pd.DataFrame, strategy="mean"):
    df_copy = df.copy()

    for col in df_copy.columns:
        if df_copy[col].dtype in ["float64", "int64"]:
            if strategy == "mean":
                df_copy[col].fillna(df_copy[col].mean(), inplace=True)
            elif strategy == "median":
                df_copy[col].fillna(df_copy[col].median(), inplace=True)
        else:
            df_copy[col].fillna("Unknown", inplace=True)

    return df_copy

def convert_to_datetime(df: pd.DataFrame, cols):
    df_copy = df.copy()

    for col in cols:
        df_copy[col] = pd.to_datetime(df_copy[col], dayfirst=True, errors="coerce")

    return df_copy