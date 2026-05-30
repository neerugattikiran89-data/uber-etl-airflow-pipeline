import pandas as pd
from utils import logger

try:
    logger.info("Starting data transformation")

    file_path = "data/uber-rides-data1.csv"

    df = pd.read_csv(file_path)

    logger.info("Dataset loaded for transformation")

    
    df["Date/Time"] = pd.to_datetime(df["Date/Time"])

    logger.info("Converted Date/Time column to datetime")

   
    df["Hour"] = df["Date/Time"].dt.hour
    df["Day"] = df["Date/Time"].dt.day
    df["Month"] = df["Date/Time"].dt.month

    logger.info("Created Hour, Day, Month columns")

    
    df.dropna(inplace=True)

    logger.info("Removed null values")

    print(df.head())

    print("\nTransformed Dataset Shape:")
    print(df.shape)

except Exception as e:
    logger.error(f"Transformation error: {e}")

    print(f"Error: {e}")
