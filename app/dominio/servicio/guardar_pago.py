import logging

from typing import TYPE_CHECKING


if TYPE_CHECKING:
    from app.dominio.puerto.puerto_mysql import PuertoMysql


class GuardarPago:
    def servicio(self, arrendatario, puerto: "PuertoMysql"):
        puerto.insertar(self, arrendatario)

    def consultar(self, arrendatario, puerto: "PuertoMysql"):
        return puerto.consultar_pago(self, arrendatario)

    def actualizar(self, arrendatario, puerto: "PuertoMysql"):
        puerto.actualizar_pago(self, arrendatario)
