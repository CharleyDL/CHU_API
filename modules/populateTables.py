#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By   : Charley ∆. Lebarbier
# Date Created : Monday 23 Jan. 2023
# ==============================================================================

import json
import mysql.connector as mysqlco
import pandas as pd

## Set connection configuration to the db
config = {
    "host" : "localhost",
    "user" :"root",
    "password" : "example",
    "database" : "CHU_api",
    "port" : "3307"
}


## Loading json for db
def read_json() -> dict:
    """Read and Extract data from a JSON file"""

    with open('../data/data.json') as data:
        content = json.load(data)

    return content

def dict_to_dataframe(data:dict) -> pd.DataFrame:
    """Transform dictionary to Dataframe"""
    return pd.DataFrame.from_dict(data, orient='index')



if __name__ == "__main__":

    try:
        db = mysqlco.connect(**config)
        cursor = db.cursor()

        # Load the content json and prepare table content to inject
        content = read_json()
        material = content['materiel']
        employee = content['employé.e informatique']

        # Inject Material Content into 'materiel' table
        for i in material:
            # Convert the dict into dataframe
            material_content = dict_to_dataframe(i)

            for index, data in material_content.iterrows():
                sql = f"""
                        INSERT INTO materiel (id, hardware_name, hardware_size, hardware_condition) 
                             VALUES ("{ index }",
                                     "{ data[0] }",
                                     "{ data[1] }",
                                     "{ data[2] }")
                                 ON DUPLICATE KEY 
                             UPDATE hardware_name = "{ data[0] }",
                                    hardware_size = "{ data[1] }",
                                    hardware_condition = "{ data[2] }";
                       """
                cursor.execute(sql)
                db.commit()

        # Inject Employee Content into 'employee' table
        for i in employee:
            # Convert the dict into dataframe
            employee_content = dict_to_dataframe(i)

            for index, data in employee_content.iterrows():
                sql = f"""
                        INSERT INTO employee (id, last_name, first_name, age, job_position) 
                             VALUES ("{ index }",
                                     "{ data[0] }",
                                     "{ data[1] }",
                                     "{ data[2] }",
                                     "{ data[3] }")
                                 ON DUPLICATE KEY 
                             UPDATE last_name = "{ data[0] }",
                                    first_name = "{ data[1] }",
                                    age = "{ data[2] }",
                                    job_position = "{ data[3] }";
                       """
                cursor.execute(sql)
                db.commit()

        print("Initialisation de la Base de Données : OK")


    except Exception as e:
        print(e)


    finally:
        if db.is_connected():
            cursor.close()
            db.close()