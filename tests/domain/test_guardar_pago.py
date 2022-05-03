import logging
from unittest.mock import Mock
from app.dominio.servicio.guardar_pago import GuardarPago
from app.dominio.modelo.arrendatario_dto import ArrendatarioDto


def test_guardar_pago():
    guardar = GuardarPago()
    puerto = Mock()

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    puerto.servicio.return_value = None

    res = guardar.servicio(arrendatario, puerto)

    assert res == None


def test_consultar():
    guardar = GuardarPago()
    puerto = Mock()

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    puerto.consultar_pago.return_value = None

    res = guardar.consultar(arrendatario, puerto)

    assert res == None


def test_actualizar():
    guardar = GuardarPago()
    puerto = Mock()

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    puerto.actualizar_pago.return_value = None

    res = guardar.actualizar(arrendatario, puerto)

    assert res == None
