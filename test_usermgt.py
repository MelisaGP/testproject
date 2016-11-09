import pytest
import files

@pytest.fixture
def client(request):
    client = files.app.test_client()
    return client

def test_get_all_files(client):
	result = client.get('/v1.0/files',follow_redirects=True)
	assert b'files' in result.data
	




