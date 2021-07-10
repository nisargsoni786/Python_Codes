import pytest,json
from method.a import create_app

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_methodgett(client):
    rv=client.get('/gett')
    assert rv.status_code==200

def test_method_postt(client):
    payload={'name':'nisarg'}
    ress={'name':'nisarg','surname':'soni'}
    rv=client.post('/postt',json=payload)
    assert rv.status_code==200
    assert ress==rv.get_json()