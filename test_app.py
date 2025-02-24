import app

def test_index():
    app.app.testing = True
    cliente = app.app.test_client()
    respuesta = cliente.get('/')
    assert respuesta.status_code == 200
    assert b"Indicadores del curso" in respuesta.data
