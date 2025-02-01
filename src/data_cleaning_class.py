import pandas as pd
class dataCleaning:
    def __init__(self, path):
        self.path = path
    def clean_data(self):
            
        # Load raw data (CSV as an example)
        df = pd.read_csv(self.path)

        df = df.drop_duplicates()

        df = df.fillna({"Text": "No message"})  # Fill missing text messages
        df = df.dropna(subset=["Message ID", "Date"])  # Ensure critical fields are not empty

        df["Date"] = pd.to_datetime(df["Date"])

        df["Text"] = df["Text"].str.lower()

        assert df["Message ID"].is_unique, "Duplicate message IDs found!"
        assert df["Text"].notnull().all(), "Null text values detected!"
        return df


