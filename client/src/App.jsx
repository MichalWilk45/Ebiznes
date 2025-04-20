import React from "react";
import { BrowserRouter, Routes, Route } from "react-router-dom";
import Products from "./components/Products";
import Cart from "./components/Cart";
import Payments from "./components/Payments";
import { CartProvider } from "./hooks/useCart";

export default function App() {
  return (
    <CartProvider>
      <BrowserRouter>
        <Routes>
          <Route path="/" element={<Products />} />
          <Route path="/products" element={<Products />} />
          <Route path="/cart" element={<Cart />} />
          <Route path="/payment" element={<Payments />} />
        </Routes>
      </BrowserRouter>
    </CartProvider>
  );
}
