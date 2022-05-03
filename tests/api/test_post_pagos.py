def test_post_vote(client):
    response = client.post("/api/pagos")
    assert response.status_code == 422


def test_post_pagos_abono(client):

    identificacion = 123456789
    codigo = "abc123"
    valor = 500000
    fecha = "02-01-2020"

    data = {
        "documentoIdentificacionArrendatario": identificacion,
        "codigoInmueble": codigo,
        "valorPagado": valor,
        "fechaPago": fecha,
    }

    url = "/api/pagos"

    response = client.post(url, json=data)

    assert response.status_code == 200
