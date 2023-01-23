#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# ==============================================================================
# Created By   : Charley ∆. Lebarbier
# Date Created : Monday 23 Jan. 2023
# ==============================================================================

from flask import jsonify, render_template, request

from app import app
from .db import get_db_config, db_connect


path = "config.json"
config = get_db_config(path)

myDB = db_connect(config)
cursor = myDB.cursor()
dbOK = myDB.is_connected()


################################################################################
####  HTML BASE - Documentation
################################################################################

@app.route('/')
def api():
    return render_template('api.html', title='API - Documentation')


################################################################################
####  MATERIEL TABLE
################################################################################

@app.route('/api/materiel', methods=['GET'])
def get_materials():
    try:
        query = """ SELECT * FROM materiel; """
        cursor.execute(query)
        result_db = cursor.fetchall()
        return jsonify(result_db)

    except Exception as e:
        return  { "result" : e }


@app.route('/api/materiel/<int:id>', methods=['GET'])
def get_one_material(id):
    try:
        query = f""" SELECT * FROM materiel WHERE id = "{id}"; """
        cursor.execute(query)
        result_db = cursor.fetchone()
        return jsonify(result_db)

    except Exception as e:
        return  { "result" : e }


@app.route('/api/materiel', methods=['POST'])
def add_material():
    record = request.get_json()
    try:
        query = f"""
                    INSERT INTO materiel (hardware_name, hardware_size, hardware_condition)
                         VALUES ("{ record['hardware_name'] }",
                                 "{ record['hardware_size'] }",
                                 "{ record['hardware_condition'] }");
                 """
        cursor.execute(query)
        myDB.commit()

        result_db = get_materials()
        return result_db

    except Exception as e:
        return  { "result" : e }


@app.route('/api/materiel', methods=['PUT'])
def update_material():
    record =request.get_json()
    try:
        query = f"""
                    UPDATE materiel
                       SET hardware_name = "{ record['hardware_name'] }",
                           hardware_size = "{ record['hardware_size'] }",
                           hardware_condition = "{ record['hardware_condition'] }"
                     WHERE id = "{ record['id'] }";
                 """
        cursor.execute(query)
        myDB.commit()

        result_db = get_materials()
        return result_db

    except Exception as e:
        return  { "result" : e }


@app.route('/api/materiel', methods=['DELETE'])
def del_material():
    record = request.get_json()
    try:
        query = f""" DELETE FROM materiel WHERE id = "{ record['id'] }"; """
        cursor.execute(query)
        myDB.commit()

        result_db = get_materials()
        return result_db

    except Exception as e:
        return  { "result" : e }


################################################################################
####  EMPLOYEE TABLE
################################################################################

@app.route('/api/employee', methods=['GET'])
def get_employees():
    try:
        query = """ SELECT * FROM employee; """
        cursor.execute(query)
        result_db = cursor.fetchall()
        return jsonify(result_db)

    except Exception as e:
        return  { "result" : e }


@app.route('/api/employee/<int:id>', methods=['GET'])
def get_one_employee(id):
    try:
        query = f""" SELECT * FROM employee WHERE id = "{id}"; """
        cursor.execute(query)
        result_db = cursor.fetchone()
        return jsonify(result_db)

    except Exception as e:
        return  { "result" : e }


@app.route('/api/employee', methods=['POST'])
def add_employee():
    record = request.get_json()
    try:
        query = f"""
                    INSERT INTO employee (last_name, first_name, age, job_position) 
                         VALUES ("{ record['last_name'] }",
                                 "{ record['first_name'] }",
                                 "{ record['age'] }",
                                 "{ record['job_position'] }");
                 """
        cursor.execute(query)
        myDB.commit()

        result_db = get_employees()
        return result_db

    except Exception as e:
        return  { "result" : e }


@app.route('/api/employee', methods=['PUT'])
def update_employee():
    record =request.get_json()
    try:
        query = f"""
                  UPDATE employee
                     SET last_name = "{ record['last_name'] }",
                        first_name = "{ record['first_name'] }",
                               age = "{ record['age'] }",
                      job_position = "{ record['job_position'] }"
                   WHERE id = "{ record['id'] }";
                 """
        cursor.execute(query)
        myDB.commit()

        result_db = get_employees()
        return result_db

    except Exception as e:
        return  { "result" : e }


@app.route('/api/employee', methods=['DELETE'])
def del_employee():
    record = request.get_json()
    try:
        query = f""" DELETE FROM employee WHERE id = "{ record['id'] }"; """
        cursor.execute(query)
        myDB.commit()

        result_db = get_employees()
        return result_db

    except Exception as e:
        return  { "result" : e }