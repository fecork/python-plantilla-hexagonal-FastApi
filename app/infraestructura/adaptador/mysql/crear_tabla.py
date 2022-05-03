import os
import pymysql
from app.infraestructura.adaptador.mysql.crear_db import establecer_conexion
from dotenv import load_dotenv


load_dotenv()


def crear_tabla():
    print("Creando Tabla Pagos")
    base_de_datos = os.getenv("NAME_DB")

    db = establecer_conexion()
    cursor = db.cursor()

    sql_db = f"USE {base_de_datos}"

    sql_crear = (
        "CREATE TABLE pagos (documentoIdentificacionArrendatario int,"
        " codigoInmueble varchar(32), fechaPago Date, valorPagado int, PRIMARY"
        " KEY(documentoIdentificacionArrendatario, codigoInmueble));"
    )

    sql_tablas = f"SHOW FULL TABLES FROM {base_de_datos}"
    try:
        cursor.execute(sql_db)
        cursor.execute(sql_crear)
        db.commit()
        cursor.execute(sql_tablas)
    except:
        db.rollback()
