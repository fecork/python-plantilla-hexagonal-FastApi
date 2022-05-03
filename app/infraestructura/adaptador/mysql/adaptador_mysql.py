import os
import pymysql
import logging
import datetime

from app.dominio.puerto.puerto_mysql import PuertoMysql
from app.dominio.modelo.arrendatario_dto import ArrendatarioDto
from app.dominio.servicio.validar_fechas import ValidarFechas
from dotenv import load_dotenv


load_dotenv()


class AdaptadorMysql(PuertoMysql):
    def __init__(self):
        self.respuesta = {}

    def prueba_base(self, arrendatario: ArrendatarioDto) -> ArrendatarioDto:
        # def prueba_base(self):
        return arrendatario

    def conectar_db(self):
        print("Resultados de PyMySQL:")
        host = os.getenv("HOST_DB")
        user = os.getenv("USUARIO_DB")
        passw = os.getenv("PASSWORD_DB")
        name_db = os.getenv("NAME_DB")
        conexion = pymysql.connect(
            host=host, user=user, passwd=passw, db=name_db
        )
        return conexion

    def ver_tabla(self, arrendatario: ArrendatarioDto) -> ArrendatarioDto:
        print("Revisando Tabla")

        query = (
            "SELECT documentoIdentificacionArrendatario, codigoInmueble FROM"
            " pagos"
        )
        conexion = self.conectar_db()
        cursor = conexion.cursor()
        cursor.execute(query)

        for (
            documentoIdentificacionArrendatario,
            codigoInmueble,
        ) in cursor.fetchall():
            print(documentoIdentificacionArrendatario, codigoInmueble)
        conexion.close()

    def insertar(self, data, arrendatario):

        query = (
            "INSERT INTO `pagos` (documentoIdentificacionArrendatario,"
            " codigoInmueble, fechaPago, ValorPagado) VALUES (%s, %s, %s, %s)"
        )

        conexion = self.conectar_db()
        cursor = conexion.cursor()
        cursor.execute(
            query,
            (
                arrendatario.documentoIdentificacionArrendatario,
                arrendatario.codigoInmueble,
                arrendatario.fechaPago,
                arrendatario.valorPagado,
            ),
        )
        conexion.commit()

        sql = "SELECT * FROM `pagos`"
        cursor.execute(sql)

        result = cursor.fetchall()
        for i in result:
            print(i)

        self.ver_tabla(arrendatario)
        conexion.close()

    def consultar_pago(self, data, arrendatario):
        try:

            cursor = self.buscar_arrendatario(self, arrendatario)
            cursor.fetchone
            for pago in cursor.fetchone():
                print(pago)

            return pago
        except Exception as e:

            return False

    def buscar_arrendatario(self, data, arrendatario):
        identificacion = arrendatario.documentoIdentificacionArrendatario
        codigo = str(arrendatario.codigoInmueble)
        query = (
            "SELECT valorPagado FROM `pagos` WHERE"
            f" documentoIdentificacionArrendatario = {identificacion} AND"
            f" codigoInmueble = '{codigo}'"
        )

        conexion = self.conectar_db()
        cursor = conexion.cursor()
        cursor.execute(query)
        return cursor

    def actualizar_pago(self, data, arrendatario):
        try:
            pago_actual = self.consultar_pago(data, arrendatario)
            pago_abono = arrendatario.valorPagado
            total = pago_actual + pago_abono

            identificacion = arrendatario.documentoIdentificacionArrendatario
            codigo = str(arrendatario.codigoInmueble)
            query = (
                f"UPDATE `pagos` SET valorPagado = {total} WHERE"
                f" documentoIdentificacionArrendatario = {identificacion} AND"
                f" codigoInmueble = '{codigo}'"
            )

            print(query)

            conexion = self.conectar_db()
            cursor = conexion.cursor()
            cursor.execute(query)
            conexion.commit()

            return cursor
        except Exception as e:
            print(e)
            return False

    def consultar_totalidad_pagos(self):
        try:
            validar = ValidarFechas()
            lista_respuestas = []
            conexion = self.conectar_db()
            cursor = conexion.cursor()

            sql = "SELECT * FROM `pagos`"
            cursor.execute(sql)

            records = cursor.fetchall()
            lista_respuestas = []
            columnNames = [column[0] for column in cursor.description]

            for record in records:
                lista_respuestas.append(dict(zip(columnNames, record)))

            for respuesta in lista_respuestas:
                print(respuesta["fechaPago"])
                print(type(respuesta["fechaPago"]))
                respuesta["fechaPago"] = validar.parsear_fecha_string(
                    respuesta["fechaPago"].strftime("%d/%m/%Y")
                )

            conexion.close()
            return lista_respuestas

        except Exception as e:
            print(e)
            return False
