import pytest
import files

@pytest.fixture
def client(request):
    client = files.app.test_client()
    return client

def test_get_all_files(client):
	result = client.get('/v1.0/files',follow_redirects=True)
	assert b'files' in result.data
	
def test_post_files(client):
  parcial_2  = {'file': 'parcial_2', 'content': 'Parcial Melisa'}
  parcial = client.post('/v1.0/files',data = parcial_2)
  assert "HTTP 201 CREATE"



