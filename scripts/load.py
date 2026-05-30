import pandas as pd
from sqlalchemy import create_engine
from utils import logger


def run_pipeline():

    try:
        logger.info("Starting load process")

        file_path = "data/uber-rides-data1.csv"

        df = pd.read_csv(file_path)

        df["Date/Time"] = pd.to_datetime(df["Date/Time"])

        df["Hour"] = df["Date/Time"].dt.hour
        df["Day"] = df["Date/Time"].dt.day
        df["Month"] = df["Date/Time"].dt.month

        logger.info("Transformation completed")

        engine = create_engine(
            "mysql+pymysql://etl_user:etl123@localhost/uber_etl"
        )

        logger.info("Connected to MySQL database")

        df.to_sql(
            name="uber_rides",
            con=engine,
            if_exists="replace",
            index=False
        )

        logger.info("Data loaded successfully into MySQL")

        print("Data loaded successfully into MySQL")

    except Exception as e:
        logger.error(f"Load process failed: {e}")

        print(f"Error: {e}")


if __name__ == "__main__":
    run_pipeline()
