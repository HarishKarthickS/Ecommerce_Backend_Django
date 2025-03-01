from django.test import TestCase, Client
from django.contrib.auth.models import User
from api.models import Product, Order

class EcommerceTests(TestCase):
    def setUp(self):
        """Create test data before each test runs."""
        self.client = Client()
        self.user = User.objects.create_user(username="testuser", password="password123")
        self.product = Product.objects.create(
            name="Test Product",
            description="A test product",
            price=10.99,
            category="Test"
        )

    # =======================
    # USER AUTH TESTS
    # =======================
    def test_register_user(self):
        response = self.client.post("/api/register/", {
            "username": "newuser",
            "email": "newuser@example.com",
            "password": "securepassword",
            "password2": "securepassword"
        })
        self.assertEqual(response.status_code, 201)
        self.assertIn("access", response.json())  # Check if JWT token is returned

    def test_login_user(self):
        response = self.client.post("/api/login/", {
            "username": "testuser",
            "password": "password123"
        })
        self.assertEqual(response.status_code, 200)
        self.assertIn("access", response.json())

    # =======================
    # PRODUCT TESTS
    # =======================
    def test_get_products(self):
        response = self.client.get("/api/products/")
        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.json()), 1)

    def test_create_product(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post("/api/products/", {
            "name": "New Product",
            "description": "A new test product",
            "price": 19.99,
            "category": "Test"
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["name"], "New Product")

    # =======================
    # ORDER TESTS
    # =======================
    def test_create_order(self):
        self.client.login(username="testuser", password="password123")
        response = self.client.post("/api/orders/", {
            "order_items": [{"product_id": self.product.id, "quantity": 2}]
        })
        self.assertEqual(response.status_code, 201)
        self.assertEqual(response.json()["total"], self.product.price * 2)

