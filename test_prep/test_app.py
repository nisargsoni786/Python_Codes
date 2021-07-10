from app import create_app
import pytest,json

# def test_main():
#     flask_app = create_app('flask_test.cfg')

#     with flask_app.test_client() as client:
#         res=client.get('/')
#         assert res.status_code==200

@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.app_context():
        with app.test_client() as client:
            yield client

def test_main(client):
    rv=client.get('/')
    print(rv)
    assert rv.status_code==200

def test_main2(client):
    rv=client.get('/a')
    print(rv)
    assert rv.status_code==200

def test_main3(client):
    rv=client.get('/b')
    print(rv)
    assert rv.status_code==200

def test_post(client):
    rv=client.post('/c',json={'name':'nisarg'})
    print(rv)
    assert rv.get_json()=={'name':'nisarg'}
    assert rv.status_code==200