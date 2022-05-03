import logging
from unittest.mock import Mock
from app.dominio.servicio.calcular_deuda import CalcularDeuda

from app.dominio.modelo.arrendatario_dto import ArrendatarioDto


def test_calcular_deuda_pago_total():
    calcular = CalcularDeuda()
    puerto = Mock()
    puerto.consultar_pago.return_value = 500000

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    respuesta = calcular.calcular_deuda(arrendatario, puerto)

    assert respuesta == "gracias por pagar todo tu arriendo"


def test_calcular_deuda_pago_parcial():
    calcular = CalcularDeuda()
    puerto = Mock()
    puerto.consultar_pago.return_value = 200000

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    respuesta = calcular.calcular_deuda(arrendatario, puerto)

    deuda = arrendatario.valorPagado - puerto.consultar_pago.return_value

    assert (
        respuesta
        == "Gracias por tu abono sin embargo recuerda que te hace falta pagar"
        f" ${deuda}"
    )
