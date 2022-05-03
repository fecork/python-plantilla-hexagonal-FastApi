def test_get_pagos(client):
    response = client.get("/api/pagos")
    assert response.status_code == 200
