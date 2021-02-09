import os
import sqlite3
import csv
import pandas as pd
from sqlalchemy import create_engine


CWD = os.getcwd()
UPLOAD_FOLDER = os.path.join(CWD, 'uploads')
DATABASE = os.path.join(CWD, 'database.db')


def get_uploaded_files():
    return [f for f in os.listdir(UPLOAD_FOLDER)]

def get_engine(db_file):
    conn = create_engine(f"sqlite:///{db_file}", echo=True)
    return conn

def read_file(filename):
    columns = ['id', 'first_name', 'last_name', 'street_address', 'state',
               'zip', 'change_in_purchase_status', 'product_id',
               'product_name', 'product_purchase_amount', 'timestamp']

    filename = os.path.join(UPLOAD_FOLDER, filename)
    df = pd.read_csv(filename, sep='\t', names=columns, header=None)
    return df

def upload_file(df, table, connection):
    df.to_sql(table, connection, if_exists='replace', index=False)

