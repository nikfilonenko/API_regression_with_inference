import pandas as pd

def save_predictions(df: pd.DataFrame, file_name="predictions.csv") -> str:
    file_path = f"output/{file_name}"
    df.to_csv(file_path, index=False)
    return file_path