import pandas as pd
import csv

def save_predictions(df: pd.DataFrame, file_name="predictions.csv") -> str:
    file_path = f"{file_name}"
    df.to_csv(file_path, index=False)
    return file_path

def is_csv(file) -> bool:
    try:
        # Читаем первые строки файла, чтобы проверить его как CSV
        content = file.file.read().decode('utf-8')
        file.file.seek(0)  # Возвращаем курсор файла в начало для дальнейшей обработки
        csv.Sniffer().sniff(content)  # Проверяем, имеет ли файл структуру CSV
        return True
    except Exception:
        return False
