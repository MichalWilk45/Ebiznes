import React from "react";
import { useCart } from "../hooks/useCart";
import { Link } from "react-router-dom";

export default function Cart() {
  const { cartItems } = useCart();

  return (
    <div>
      <h1>Koszyk</h1>
      {cartItems.length === 0 ? (
        <p>Twój koszyk jest pusty.</p>
      ) : (
        cartItems.map((item, index) => (
          <div key={index}>{item.name} - {item.price} zł</div>
        ))
      )}
      <br />
      <Link to="/payments">Przejdź do płatności</Link>
    </div>
  );
}