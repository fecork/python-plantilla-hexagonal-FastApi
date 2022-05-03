import logging
from unittest.mock import Mock
from app.dominio.servicio.consultar_pagos import ConsultarPagos

from app.dominio.modelo.arrendatario_dto import ArrendatarioDto


def test_calcular_deuda_pago_total():
    consultar = ConsultarPagos()
    puerto = Mock()
    respuesta = [
        {
            "documentoIdentificacionArrendatario": 111,
            "codigoInmueble": "111",
            "fechaPago": "2020-01-13",
            "valorPagado": 1000000,
        },
        {
            "documentoIdentificacionArrendatario": 111,
            "codigoInmueble": "222",
            "fechaPago": "2020-01-13",
            "valorPagado": 1000000,
        },
    ]
    puerto.consultar_totalidad_pagos.return_value = respuesta

    res = consultar.consultar_pagos(puerto)

    assert type(res) == list
