from app import app

def test_home():
    client = app.test_client()
    res = client.get('/')
    assert res.status_code == 200
    assert b"Hello from Flask!" in res.data

def test_secret():
    client = app.test_client()
    res = client.get('/secret')
    assert res.status_code == 200
    assert b"Secret message:" in res.data


