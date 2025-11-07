# import the data in python environment and then turn it into sql
import pandas as pd
import mysql.connector

# connect sql
try:

    df = pd.read_csv(
        '/WA_Fn-UseC_-Telco-Customer-Churn.csv')
    print(f"CSV : {len(df)} rows")

    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",  # keyword
        database="mydemo"
    )
    cursor = conn.cursor()
    print("connected!")

#load data in sql
    df.to_sql('telco_churn', conn, if_exists='replace', index=False)
