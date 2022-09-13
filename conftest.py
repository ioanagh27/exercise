import pytest
import app
from controllers import data

@pytest.fixture
def api(monkeypatch):
    test_flowers = [
        {'id': 1, 'name': 'test1', 'colour': 'white', 'water': True},
        {'id': 2, 'name': 'test2', 'colour': 'purple', 'water': False}
    ]
    monkeypatch.setattr(data, "flowers", test_flowers)
    api = app.app.test_client()
    return api