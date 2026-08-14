import pytest
import requests

from api.booking_client import BookingAPIClient

BASE_URL = "https://restful-booker.herokuapp.com"

class ApiSession(requests.Session):
    def request(self, method, url, **kwargs):
        kwargs.setdefault("timeout", 10)
        return super().request(method, BASE_URL + url, **kwargs)

@pytest.fixture(scope="session")
def api_session():
    session =  ApiSession()
    session.headers.update({"Accept": "application/json"})
    yield session
    session.close()


@pytest.fixture
def booking_client(api_session):
    return BookingAPIClient(api_session)
  
  
  