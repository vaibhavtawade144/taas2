import requests

def test_apply_loan():
    url = "http://localhost:5000/apply-loan"
    response = requests.post(url, json={"amount": 30000})
    assert response.status_code == 200
