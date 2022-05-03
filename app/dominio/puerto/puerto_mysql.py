import abc
from app.dominio.modelo.arrendatario_dto import ArrendatarioDto


class PuertoMysql(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def prueba_base(self, arrendatario_dto: ArrendatarioDto) -> ArrendatarioDto:
        raise NotImplementedError

    @abc.abstractmethod
    def conectar_db(self, arrendatario_dto: ArrendatarioDto) -> ArrendatarioDto:
        raise NotImplementedError

    @abc.abstractmethod
    def ver_tabla(self, arrendatario_dto: ArrendatarioDto) -> ArrendatarioDto:
        raise NotImplementedError

    @abc.abstractmethod
    def insertar(
        self, data, arrendatario_dto: ArrendatarioDto
    ) -> ArrendatarioDto:
        raise NotImplementedError

    @abc.abstractmethod
    def consultar_pago(
        self, data, arrendatario_dto: ArrendatarioDto
    ) -> ArrendatarioDto:
        raise NotImplementedError

    @abc.abstractmethod
    def buscar_arrendatario(
        self, data, arrendatario_dto: ArrendatarioDto
    ) -> ArrendatarioDto:
        raise NotImplementedError

    @abc.abstractmethod
    def actualizar_pago(
        self, data, arrendatario_dto: ArrendatarioDto
    ) -> ArrendatarioDto:
        raise NotImplementedError

    @abc.abstractmethod
    def consultar_totalidad_pagos(self):
        raise NotImplementedError
