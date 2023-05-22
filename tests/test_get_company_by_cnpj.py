from fastapi.testclient import TestClient
from main import app

client = TestClient(app)


def test_get_root():
    response = client.get("/")
    assert response.status_code == 200
    assert response.json() == {"InfoInvest": "AI"}


def test_get_company_by_cnpj_invalid_id():
    """
    CNPJ with invalid id number
    :return:
    """
    response = client.get("/companies/08773135000101")
    assert response.status_code == 404


def test_get_company_by_cnpj_invalid_size():
    """
    CNPJ with wrong size 15 characters and 13 characters
    :return:
    """
    response = client.get("/companies/087731350001011")
    assert response.status_code == 400

    response = client.get("/companies/0877313500010")
    assert response.status_code == 400
