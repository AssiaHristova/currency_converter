def test_home(client):
    response = client.get("/")
    assert response.status_code == 200
    assert b'Currency Converter' in response.data


def test_home_with_invalid_input(client):
    data = {'amount': 'ten', 'from_curr': 'TTD', 'to_curr': 'ZMW'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'Bad Request' in response.data


def test_home_with_valid_input(client):
    data = {'amount': 10, 'from_curr': 'TTD', 'to_curr': 'ZMW'}
    response = client.post('/', data=data)
    assert response.status_code == 200
    assert b'26.37' in response.data
