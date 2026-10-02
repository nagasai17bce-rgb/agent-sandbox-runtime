from fastapi.testclient import TestClient
from app.main import app
client=TestClient(app)
def test_execution():
    data=client.post("/v1/run",json={"value":"print('ok')"}).json()
    assert data["exit_code"]==0
    assert data["stdout"].strip()=="ok"
