import requests

BASE_URL = "http://localhost:8080"

def test_create_product_without_required_fields():
    res = requests.post(f"{BASE_URL}/products", json={})
    assert res.status_code in (400, 422)

def test_get_nonexistent_product():
    res = requests.get(f"{BASE_URL}/products/999999")
    assert res.status_code == 404

def test_update_product_with_invalid_data():
    res = requests.put(f"{BASE_URL}/products/1", json={"price": -100})
    assert res.status_code in (400, 422, 404)

def test_delete_nonexistent_product():
    res = requests.delete(f"{BASE_URL}/products/999999")
    assert res.status_code in (404, 400)

def test_create_category_without_name():
    res = requests.post(f"{BASE_URL}/categories", json={})
    assert res.status_code in (400, 422)

def test_get_nonexistent_category():
    res = requests.get(f"{BASE_URL}/categories/999999")
    assert res.status_code == 404

def test_update_category_with_invalid_data():
    res = requests.put(f"{BASE_URL}/categories/1", json={"name": ""})
    assert res.status_code in (400, 422, 404)

def test_delete_nonexistent_category():
    res = requests.delete(f"{BASE_URL}/categories/999999")
    assert res.status_code in (404, 400)

def test_add_cart_item_with_invalid_product_id():
    payload = {
        "product_id": 999999,  # non-existent
        "quantity": 1,
        "cart_id": 1
    }
    res = requests.post(f"{BASE_URL}/cart-items", json=payload)
    assert res.status_code in (400, 404)

def test_add_cart_item_with_negative_quantity():
    payload = {
        "product_id": 1,
        "quantity": -5,
        "cart_id": 1
    }
    res = requests.post(f"{BASE_URL}/cart-items", json=payload)
    assert res.status_code in (400, 422)

def test_get_cart_that_does_not_exist():
    res = requests.get(f"{BASE_URL}/cart/999999")
    assert res.status_code == 404

def test_update_nonexistent_cart_item():
    res = requests.put(f"{BASE_URL}/cart-items/999999", json={"quantity": 2})
    assert res.status_code == 404

def test_delete_nonexistent_cart_item():
    res = requests.delete(f"{BASE_URL}/cart-items/999999")
    assert res.status_code == 404
