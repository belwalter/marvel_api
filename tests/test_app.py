import pytest
from fastapi.testclient import TestClient
from main import app

client = TestClient(app)

@pytest.fixture
def test_data():
    return {
        "kang": {
            "name": "Kang",
            "alias": "Kang the Conqueror",
            "real_name": "Nathaniel Richards",
            "short_bio": "Kang the Conqueror is a time-traveling warlord.",
            "first_appearance": 1964,
            "is_villian": True,
            "image_url": "http://localhost:8005/images/kang.png"
        },
        "hulk": {
            "name": "Hulk",
            "alias": "The Hulk",
            "real_name": "Bruce Banner",
            "short_bio": "Hulk is a gamma-powered superhero with incredible strength.",
            "first_appearance": 1962,
            "image_url": "http://localhost:8005/images/hulk.png"
        }
    }

def test_get_marvel_villain_success(test_data):
    response = client.get("/marvel_character/kang")
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == test_data['kang']['name']
    assert data['alias'] == test_data['kang']['alias']
    assert data['real_name'] == test_data['kang']['real_name']
    assert data['first_appearance'] == test_data['kang']['first_appearance']
    assert 'is_villian' in data and data['is_villian'] == test_data['kang']['is_villian']
    assert data['image_url'] == test_data['kang']['image_url']

def test_get_marvel_hero_success(test_data):
    response = client.get("/marvel_character/hulk")
    assert response.status_code == 200
    data = response.json()
    assert data['name'] == test_data['hulk']['name']
    assert data['alias'] == test_data['hulk']['alias']
    assert data['real_name'] == test_data['hulk']['real_name']
    assert data['first_appearance'] == test_data['hulk']['first_appearance']
    assert 'is_villian' not in data
    assert data['image_url'] == test_data['hulk']['image_url']

def test_get_marvel_character_not_found():
    response = client.get("/marvel_character/sarasa")
    assert response.status_code == 404
    assert response.json() == {"detail": "Character not found"}

def test_static_image_serving():
    response = client.get("/images/kang.png")
    assert response.status_code == 200
    assert response.headers["content-type"] == "image/png"

