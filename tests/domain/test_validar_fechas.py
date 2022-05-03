import pytest
from datetime import datetime

from app.dominio.servicio.validar_fechas import ValidarFechas
from app.dominio.modelo.arrendatario_dto import ArrendatarioDto


def test_validar_formato():

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    validar = ValidarFechas()

    respuesta = validar.formato_fecha(arrendatario)

    assert respuesta == False


def test_fecha_impar():

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "01-01-2022"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    validar = ValidarFechas()

    respuesta = validar.formato_fecha(arrendatario)

    assert respuesta == False


def test_parsear_fecha():

    with pytest.raises(ValueError):

        fecha = "2022-01-31"
        validar = ValidarFechas()
        validar.parsear_fecha(fecha)

    fecha = "01/01/2022"
    date_time_obj = datetime.strptime(fecha, "%d/%m/%Y")
    validar = ValidarFechas()
    respuesta = validar.parsear_fecha(fecha)
    assert respuesta == date_time_obj
