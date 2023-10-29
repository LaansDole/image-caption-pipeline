from fastapi.testclient import TestClient
from main import app  # Updated import statement

client = TestClient(app)


def test_get_data() -> None:
    """
    Test getting data
    """
    response = client.get("/data")
    assert (
        response.status_code == 200
    ), f"Expected status code 200, but got {response.status_code}."
