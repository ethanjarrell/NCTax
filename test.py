from nctax import app
from flask import json

def test_successful_get():
    response = app.test_client().get('/tax', data=json.dumps({'county': 'Lee', 'amount': '$12.75'}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data == {
    "data": {
        "County": "Lee",
        "Sales Amount": "$12.75",
        "Sales Tax Amount": "$0.89",
        "Tax Rate": "7%",
        "Total Sale": "$13.64"
    }
}

def test_bad_parameters_county():
    response = app.test_client().get('/tax', data=json.dumps({'county': 'NotACounty', 'amount': 12.75}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data == {'error': 'Not a valid NC County'}

def test_bad_parameters_amount():
    response = app.test_client().get('/tax', data=json.dumps({'county': 'Lee', 'amount': 'blxxv'}),
        content_type='application/json',
    )

    data = json.loads(response.get_data(as_text=True))

    assert response.status_code == 200
    assert data == {'error': 'Not a valid sales amount'}
