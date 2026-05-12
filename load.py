import os
from sqlalchemy import create_engine
from transform import transform
from dotenv import load_dotenv

load_dotenv()

def load():
    df = transform()

    av_url = os.getenv("AIVEN_DB_URL")
    engine = create_engine(av_url)

    df.to_sql(
        "exchanges",
        engine,
        index=False,
        if_exists="replace"
    )

    print("Data loaded successfully into exchanges table!")

if __name__ == "__main__":
    load()