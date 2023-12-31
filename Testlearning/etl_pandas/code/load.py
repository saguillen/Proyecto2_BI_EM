from pandas import DataFrame
import pandas as pd

import sys


from constant import connection, add_constraint
# Load the data based on type
'''
:param type: Input Storage type (db|csv) Based on type data stored in MySQL or FileSystem
:param df: Input Dataframe
:param target: Input target -For filesystem - Location where to store the data
                            -For MySQL - table name
'''


def load(type: str, df: DataFrame, target: str, constraints: list=None):
    
    try:
        # Write data on mysql database with table name
        if type=="db":
            mydb = connection()
            df.to_sql(target, con=mydb, if_exists='replace', index=False)
            print(f"Data succesfully loaded to MySQL Database !!")
            for constraint in constraints:
                 add_constraint(mydb,constraint)
        
        if type=="csv":
            # Write data on filesystem
            df.to_csv(target, index=False)
            print(f"Data succesfully loaded to filesystem !!")
            
    except FileExistsError as e:
            print("File alsready exists: 'etl_pandas/output/EM_salud2021-2017.csv'")
        
