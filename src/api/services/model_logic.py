from pathlib import Path

import numpy as np
import pandas as pd
import pickle

from src.api.core.models import Car
from src.api.core.utils import save_predictions


current_dir = Path(__file__).resolve().parent
project_root = current_dir.parent.parent.parent
model_path = project_root / 'src' / 'ml' / 'weights' / 'best_model.pkl'


with open(model_path, 'rb') as f:
    inference = pickle.load(f)
    model = inference["model"]
    scaler = inference["scaler"]
    encoder_ohe = inference["encoder_ohe"]
    columns = inference["columns"]


def ohe_encoding_data(df: pd.DataFrame, encoder_ohe) -> pd.DataFrame:
    columns = df.select_dtypes(include='object').columns.tolist()
    df_ohe = encoder_ohe.transform(df[columns])
    df_ohe = pd.DataFrame(data=df_ohe, columns=encoder_ohe.get_feature_names_out(), index=df.index)
    df_ohe_final = pd.concat([df.drop(columns=columns), df_ohe], axis=1)
    return df_ohe_final


def std_scale(df: pd.DataFrame, scale_std) -> pd.DataFrame:
    df_scale = scale_std.transform(df)
    df_scale = pd.DataFrame(df_scale, columns=df.columns, index=df.index)
    return df_scale


def preprocess_data(df: pd.DataFrame) -> pd.DataFrame:
    engine_liters = df['engine'] / 1000
    df['horses_per_liter'] = df['max_power'] / engine_liters
    df['horses_per_liter'] = df['horses_per_liter'].apply(lambda x: round(x, 3))
    df['year_squared'] = df['year'] ** 2
    df['is_third_or_more_owner'] = df['owner'].apply(lambda x: 1 if x in ['Third Owner', 'Fourth & Above Owner'] else 0)
    df['is_trustworthy_seller'] = (
            (df['owner'].isin(['First Owner', 'Second Owner'])) &
            (df['seller_type'] == 'Trustmark Dealer')
    ).astype(int)

    df_ohe = ohe_encoding_data(df=df, encoder_ohe=encoder_ohe)
    df_ohe_scaled = std_scale(df=df_ohe, scale_std=scaler)

    return df_ohe_scaled


def make_single_prediction(car: Car):
    try:
        df = pd.DataFrame([car.dict()])
        df_preprocessed = preprocess_data(df)
        prediction = model.predict(df_preprocessed)
        return float(np.expm1(prediction[0]))
    except Exception as e:
        raise Exception(e)


def make_bulk_prediction(file):
    input_data = pd.read_csv(file.file)
    input_data_preprocessed = preprocess_data(input_data)
    predictions = model.predict(input_data_preprocessed)
    input_data["predicted_price"] = predictions
    result_file = save_predictions(input_data)
    return result_file