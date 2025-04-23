import requests

BASE_URL = "http://localhost:8080"

# Pomocnicza funkcja do tworzenia obiektów
def create_category(name, description=""):
    return requests.post(f"{BASE_URL}/categories", json={"name": name, "description": description})

def create_product(name, price, stock, category_id):
    return requests.post(f"{BASE_URL}/products", json={
        "name": name,
        "description": "desc",
        "price": price,
        "stock_count": stock,
        "category_id": category_id
    })

# Testy kategorii
def test_create_and_get_category():
    r = create_category("TestCat", "A test category")
    assert r.status_code == 201
    data = r.json()
    assert data["name"] == "TestCat"
    assert "id" in data

    get_r = requests.get(f"{BASE_URL}/categories/{data['id']}")
    assert get_r.status_code == 200
    assert get_r.json()["description"] == "A test category"

def test_create_category_negative():
    r = requests.post(f"{BASE_URL}/categories", json={})
    assert r.status_code in (400, 422)

def test_get_all_categories():
    r = requests.get(f"{BASE_URL}/categories")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

# Testy produktów
def test_create_product_and_fetch():
    cat = create_category("Electronics").json()
    r = create_product("Laptop", 1500.0, 10, cat["id"])
    assert r.status_code == 201
    product = r.json()
    assert product["name"] == "Laptop"
    assert product["price"] == 1500.0
    assert product["stock_count"] == 10

    fetched = requests.get(f"{BASE_URL}/products/{product['id']}")
    assert fetched.status_code == 200
    assert fetched.json()["category_id"] == cat["id"]

def test_create_product_negative():
    r = create_product("", -5, -1, 99999)
    assert r.status_code in (400, 422)

def test_get_all_products():
    r = requests.get(f"{BASE_URL}/products")
    assert r.status_code == 200
    assert isinstance(r.json(), list)

# Testy wyszukiwania i filtrów (jeśli są dostępne)
def test_filter_products_by_category():
    cat = create_category("Books").json()
    create_product("Book1", 20.0, 3, cat["id"])
    create_product("Book2", 25.0, 2, cat["id"])
    
    r = requests.get(f"{BASE_URL}/products?category_id={cat['id']}")
    assert r.status_code == 200
    products = r.json()
    for p in products:
        assert p["category_id"] == cat["id"]

# Minimum 50 asercji
def test_bulk_assertions():
    for i in range(10):
        r = create_category(f"Cat{i}")
        assert r.status_code == 201
        cat_id = r.json()["id"]

        p = create_product(f"Prod{i}", 20 + i, 5 + i, cat_id)
        assert p.status_code == 201
        prod = p.json()

        assert prod["name"] == f"Prod{i}"
        assert prod["price"] == 20 + i
        assert prod["stock_count"] == 5 + i
        assert prod["category_id"] == cat_id
