import app


def test_index():
    app.app.testing = True
    cliente = app.app.test_client()
    respuesta = cliente.get("/")
    assert respuesta.status_code == 200


def test_api():
    app.app.testing = True
    cliente = app.app.test_client()
    respuesta = cliente.get("/api/indicadores")
    assert respuesta.status_code == 200
    assert respuesta.content_type == "application/json"
