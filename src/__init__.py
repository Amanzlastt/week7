# import pandas as pd
# import os
# import sys
# sys.path.append(os.path.abspath("../src"))

from src.data_cleaning_class import dataCleaning
df_chem = dataCleaning("C:\\Users\\Aman\\Desktop\\week7\\data\\chemed123_messages.csv")
# df_doctor = pd.read_csv("C:\\Users\\Aman\\Desktop\\week7\\data\\doctorset_messages.csv")
df_chem = df_chem.clean_data()
# df_doctor = dataCleaning(df_doctor)


print(df_chem.head())
