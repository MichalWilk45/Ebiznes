import React from "react";
import axios from "axios";
import { useCart } from "../hooks/useCart";

export default function Payments() {
  const { cartItems } = useCart();

  const handlePayment = () => {
    const payload = {
      cartItems: cartItems.map((item) => ({
        productId: item.id,
        quantity: 1,
      }))
    };

    axios.post("http://localhost:8080/payment", payload, {
      headers: { 'Content-Type': 'application/json' }
    })
      .then((res) => alert("Płatność zakończona pomyślnie!"))
      .catch((err) => console.error(err));
  };

  return (
    <div>
      <h1>Płatności</h1>
      <button onClick={handlePayment}>Złóż zamówienie</button>
    </div>
  );
}
