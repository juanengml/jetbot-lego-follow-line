from requests import get, post
from lodge import logger

def test_status_endpoint(endpoint):
    result = get(endpoint).json()
    assert "alive" == result['status'] , "API not avaliable"

def test_check_motor(endpoint):
    result = post(endpoint, data = {"controle": "p"}).json()
    assert "work_motor" == result['status'], "API Motor is Not receive data"

if __name__ == "__main__":
   logger.info("Test Integration")
   endpoint = "http://0.0.0.0:8080/api/arduino/"
   test_status_endpoint(endpoint)
   test_check_motor(endpoint)
