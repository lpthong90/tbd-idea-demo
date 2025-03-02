from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

def test_read_root() -> None:
    """Test the root endpoint returns the expected HTML content."""
    response = client.get("/")
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert "Demo Trunk-Based Development" in response.text

def test_template_exists() -> None:
    """Test that the template file exists and is accessible."""
    response = client.get("/")
    assert response.status_code == 200
    assert "<!DOCTYPE html>" in response.text
    assert "<title>TBD Demo</title>" in response.text