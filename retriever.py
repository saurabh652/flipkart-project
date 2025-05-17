import pandas as pd
from dotenv import load_dotenv
import google.generativeai as genai
import os

def retrieve_products(parsed_query):
    df = pd.read_csv("E:\\flipkart brainworks project\\flipkart_laptops_detailed.csv")
    df["price"] = pd.to_numeric(df["price"], errors="coerce")
    df = df[df["price"] <= parsed_query["price"]]
    print("After price filter:", len(df))  # Debug

    df = df[df["category"].str.lower() == parsed_query["category"]]
    print("After category filter:", len(df))  # Debug

    # Match any keyword feature
    feature_mask = pd.Series([False] * len(df))
    for feature in parsed_query["features"]:
        feature_mask |= (
            df["description"].str.contains(feature, case=False, na=False) |
            df["specs"].str.contains(feature, case=False, na=False) |
            df["battery_life"].astype(str).str.contains(feature, case=False, na=False)
        )

    if parsed_query["features"]:
        df = df[feature_mask]

    print("After feature match:", len(df))  # Debug
    return df[["product_id", "name", "price", "battery_life", "brand", "description", "specs"]].head(3).to_dict(orient="records")