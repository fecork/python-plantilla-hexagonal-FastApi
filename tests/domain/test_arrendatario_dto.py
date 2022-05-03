import uuid

from app.dominio.modelo.arrendatario_dto import ArrendatarioDto


def test_vote_existing_vote_id():

    identificacion = "123456789"
    codigo = "abc123"
    valor = 500000
    fecha = "2020-01-01"

    arrendatario = ArrendatarioDto(identificacion, codigo, valor, fecha)

    assert arrendatario.documentoIdentificacionArrendatario == identificacion
