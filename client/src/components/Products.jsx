import React, { useEffect, useState } from "react";
import axios from "axios";
import { useCart } from "../hooks/useCart";

export default function Products() {
  const [products, setProducts] = useState([]);
  const { cartItems, setCartItems } = useCart();

  useEffect(() => {
    axios.get("http://localhost:8080/products", { headers: { 'Content-Type': 'application/json' } })
      .then((res) => setProducts(res.data))
      .catch((err) => console.error(err));
  }, []);

  const addToCart = (product) => {
    setCartItems([...cartItems, product]);
  };

  return (
    <div>
      <h1>Produkty</h1>
      {products.map((p) => (
        <div key={p.id}>
          <span>{p.name} - {p.price} zł</span>
          <button onClick={() => addToCart(p)}>Dodaj do koszyka</button>
        </div>
      ))}
    </div>
  );
}