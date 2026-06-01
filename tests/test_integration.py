import pytest
import requests
import os

# L'URL de base de l'API (localhost par défaut pour les tests locaux)
BASE_URL = os.environ.get("API_BASE_URL", "http://localhost:5000")

class TestRootRoute:
    """Tests pour la route GET /"""

    def test_hello_world_status_code(self):
        """Vérifie que la route / retourne un code 200"""
        response = requests.get(f"{BASE_URL}/")
        assert response.status_code == 200

    def test_hello_world_message(self):
        """Vérifie que la route / retourne le bon message"""
        response = requests.get(f"{BASE_URL}/")
        data = response.json()
        assert "message" in data
        assert data["message"] == "Hello World!"

    def test_hello_world_content_type(self):
        """Vérifie que la réponse est bien du JSON"""
        response = requests.get(f"{BASE_URL}/")
        assert "application/json" in response.headers["Content-Type"]

class TestItemsRoute:
    """Tests pour les routes GET et POST /items"""

    def test_get_items_status_code(self):
        """Vérifie que GET /items retourne 200"""
        response = requests.get(f"{BASE_URL}/items")
        assert response.status_code == 200

    def test_get_items_returns_list(self):
        """Vérifie que GET /items retourne une liste"""
        response = requests.get(f"{BASE_URL}/items")
        data = response.json()
        assert "items" in data
        assert isinstance(data["items"], list)

    def test_get_items_not_empty(self):
        """Vérifie que la liste d'items n'est pas vide au départ"""
        response = requests.get(f"{BASE_URL}/items")
        data = response.json()
        assert len(data["items"]) > 0

    def test_post_item_status_code(self):
        """Vérifie que POST /items retourne 201"""
        new_item = {"name": "Mango", "price": 2.50}
        response = requests.post(f"{BASE_URL}/items", json=new_item)
        assert response.status_code == 201

    def test_post_item_confirmation_message(self):
        """Vérifie le message de confirmation après ajout"""
        new_item = {"name": "Pineapple", "price": 4.00}
        response = requests.post(f"{BASE_URL}/items", json=new_item)
        data = response.json()
        assert "message" in data
        assert data["message"] == "Item ajouté avec succès"

    def test_post_item_appears_in_list(self):
        """Vérifie que l'item ajouté apparaît bien dans la liste"""
        new_item = {"name": "UniqueTestItem_XYZ", "price": 9.99}
        requests.post(f"{BASE_URL}/items", json=new_item)
        response = requests.get(f"{BASE_URL}/items")
        data = response.json()
        names = [item["name"] for item in data["items"]]
        assert "UniqueTestItem_XYZ" in names

    def test_post_item_missing_name(self):
        """Vérifie qu'un item sans nom retourne une erreur 400"""
        bad_item = {"price": 1.00}
        response = requests.post(f"{BASE_URL}/items", json=bad_item)
        assert response.status_code == 400

    def test_post_item_contains_id(self):
        """Vérifie que l'item créé possède bien un ID"""
        new_item = {"name": "Grape", "price": 5.00}
        response = requests.post(f"{BASE_URL}/items", json=new_item)
        data = response.json()
        assert "item" in data
        assert "id" in data["item"]