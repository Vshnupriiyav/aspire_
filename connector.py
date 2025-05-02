import pandas as pd
import numpy as np
import pymysql
import sys
import sqlalchemy



cred = { 'user': 'vishnupriya', 'password': 'P'}

def data_fetch_v2(query,*, 
                  cred=cred, db='aspiredb', 
                  host="13.235.168.161", **kwargs):
    """
    Fetches data for the given query from the database.

    Args:
        query (str):
        cred (dict): {"user" : "<user name>", "password" : "<password>"}
        db (str): 
        host (str):
        kwargs : 

    Returns:
        success_flag (bool):
        output (pd.DataFrame): 
        error_msg (str):
    """
    success_flag = False
    output = pd.DataFrame()
    error_msg = ""
    db_url = rf"mysql+pymysql://{cred['user']}:{cred['password']}@{host}/{db}"
    engine = sqlalchemy.create_engine(db_url)
    output = pd.read_sql(query, engine, **kwargs)
    print(output)
    success_flag = True

    try:
        db_url = rf"mysql+pymysql://{cred['user']}:{cred['password']}@{host}/{db}"
        engine = sqlalchemy.create_engine(db_url)
        output = pd.read_sql(query, engine, **kwargs)
        print(output)
        success_flag = True
    except Exception as e:
        success_flag = False
        error_msg = f"error in data_fetch, {type(e)._name_}: {str(e)}"
    finally:
        return success_flag, output, error_msg
    
 
