import pytest
import json
from flask_app import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config['TESTING'] = True

    with app.test_client() as client:
        yield client


def test_base(client):
    """[summary]
        this function will test the response comming from '/' endpoint is 200 or not
    """
    response= client.get('/')
    assert response.status_code == 200


def test_rasa(client):
    """[summary]
       this function will test the response comming from '/get' endpoint is 200 or not
    """
    payload= {'msg':'hii'}
    response= client.get('/get',json=payload)
    assert response.status_code == 200
