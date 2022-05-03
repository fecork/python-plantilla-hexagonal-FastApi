# import the mysql client for python

import os
from dotenv import load_dotenv

import pymysql

load_dotenv()


def crear_base_de_datos():
    print("Creando Base de Datos")
    name_db = os.getenv("NAME_DB")

    connection_instance = establecer_conexion()

    try:

        cursor_insatnce = connection_instance.cursor()
        sql_statement = "CREATE DATABASE IF NOT EXISTS " + name_db
        cursor_insatnce.execute(sql_statement)
        sql_query = "SHOW DATABASES"
        cursor_insatnce.execute(sql_query)
        database_list = cursor_insatnce.fetchall()
        for datatbase in database_list:
            print(datatbase)

    except Exception as e:

        print("Exeception occured:{}".format(e))

    finally:

        connection_instance.close()


def establecer_conexion():
    print("Conectando a Servidor")

    host_db = os.getenv("HOST_DB")
    user_db = os.getenv("USUARIO_DB")
    pass_db = os.getenv("PASSWORD_DB")

    char_set = "utf8mb4"

    cursor_type = pymysql.cursors.DictCursor

    connection_instance = pymysql.connect(
        host=host_db,
        user=user_db,
        password=pass_db,
        charset=char_set,
        cursorclass=cursor_type,
    )

    return connection_instance
