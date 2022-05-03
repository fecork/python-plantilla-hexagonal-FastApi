from app.dominio.servicio.consultar_pagos import ConsultarPagos
from app.dominio.excepciones.error_del_negocio import ErrorDelNegocio

from app.infraestructura.adaptador.mysql.adaptador_mysql import AdaptadorMysql

import logging


consultar = ConsultarPagos()
adaptador = AdaptadorMysql()
error_del_negocio = ErrorDelNegocio()


class ManejadorConsultaPagos:
    def ejecutar(self):

        return consultar.consultar_pagos(adaptador)
