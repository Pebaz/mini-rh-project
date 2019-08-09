import test_common
import pytest
from rh.routes import *


@pytest.fixture
def client():
	"""
	PyTest fixture for providing access to a mocked WSGI app instance.
	"""
	yield app.test_client()



def test_top10(client):
    result = client.get('/top10/genres')

    print(dir(result))

