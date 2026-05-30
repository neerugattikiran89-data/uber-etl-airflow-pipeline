import pandas as pd
from utils import logger

try:
    logger.info("Starting data extraction")

    file_path = "data/uber-rides-data1.csv"

    df = pd.read_csv(file_path)

    logger.info("Dataset loaded successfully")

    print(df.head())

    print("\nShape of Dataset:")
    print(df.shape)

    logger.info(f"Dataset shape: {df.shape}")

except Exception as e:
    logger.error(f"Error occurred: {e}")

    print(f"Error: {e}")
