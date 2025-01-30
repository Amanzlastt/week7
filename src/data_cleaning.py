import pandas as pd
class dataCleaniing:
    def __init__(self):
        self.data


    def clean_data(self,datapath):
            
        # Load raw data (CSV as an example)
        df = pd.read_csv(datapath)

        # Preview data
        print(df.head())


        df = df.drop_duplicates()

        df = df.fillna({"text": "No message"})  # Fill missing text messages
        df = df.dropna(subset=["message_id", "date"])  # Ensure critical fields are not empty

        df["date"] = pd.to_datetime(df["date"])

        df["text"] = df["text"].str.lower()

        assert df["message_id"].is_unique, "Duplicate message IDs found!"
        assert df["text"].notnull().all(), "Null text values detected!"

        self.data = df 
        return self.data


