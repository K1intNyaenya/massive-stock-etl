import json
import pandas as pd

def transform():
    # load raw data
    with open("raw_data.json", "r") as f:
        data = json.load(f)

    # normalize to dataframe
    df = pd.json_normalize(data["results"])

    # fill missing columns with NaN before selecting
    expected_cols = ["id", "name", "type", "asset_class", "locale", "mic", "operating_mic", "participant_id", "url"]
    for col in expected_cols:
        if col not in df.columns:
            df[col] = None

    # select and reorder
    df = df[expected_cols]

    # rename for clarity
    df = rename_columns(df)

    # fill NaN values
    df = df.fillna("N/A")

    print(df)
    return df

def rename_columns(df):
    df = df.rename(columns={
        "id": "exchange_id",
        "name": "exchange_name",
        "type": "exchange_type",
        "mic": "mic_code",
        "operating_mic": "operating_mic_code",
        "url": "website"
    })
    
    return df

if __name__ == "__main__":
    transform()