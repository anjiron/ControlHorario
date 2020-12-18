import sqlite3
import pandas
import pickle
import os

def new_db(name):
	conexion = sqlite3.connect(name)
	cursor = conexion.cursor()

	cursor.execute("CREATE TABLE tabla_control (fecha DATE , hora_entrada TIME, hora_salida TIME, horas_diarias TIME)")

	conexion.close()

def insert_data_db(name, entrada):
    conexion = sqlite3.connect(name)
    cursor = conexion.cursor()
    cursor.execute('INSERT INTO tabla_control(fecha, hora_entrada, hora_salida, horas_diarias) VALUES(?, ?, ?, ?)', entrada)
    conexion.commit()

    conexion.close()


def get_all_data(db_name, table_name):
    conexion = sqlite3.connect(db_name)

    query = f"SELECT * FROM {table_name}"

    data = pandas.read_sql_query(query, conexion)
    conexion.close()

    return data


def save_pickle(data, path, file_name):
    if not os.path.exists(path):
        os.makedirs(path)
    if isinstance(data, pandas.DataFrame):
        data.to_pickle(f"{path}/{file_name}.pkl")
    else:
        with open(f"{path}/{file_name}.pkl", 'wb') as file_name:
            pickle.dump(data, file_name)

def load_pickle(path, file_name):
    return pandas.read_pickle(f"{path}/{file_name}.pkl")