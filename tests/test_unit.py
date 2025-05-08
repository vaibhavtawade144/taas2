def test_loan_approval():
    data = {"amount": 40000}
    assert data["amount"] < 50000
