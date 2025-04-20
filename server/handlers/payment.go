package handlers

import (
	"encoding/json"
	"fmt"
	"net/http"
)

type PaymentRequest struct {
	CartItems []struct {
		ProductID int `json:"productId"`
		Quantity  int `json:"quantity"`
	} `json:"cartItems"`
}

func HandlePayment(w http.ResponseWriter, r *http.Request) {
	var payment PaymentRequest
	err := json.NewDecoder(r.Body).Decode(&payment)
	if err != nil {
		http.Error(w, "Invalid request", http.StatusBadRequest)
		return
	}

	fmt.Println("Received payment request:", payment)

	w.Header().Set("Access-Control-Allow-Origin", "*") // CORS
	w.WriteHeader(http.StatusOK)
	w.Write([]byte(`{"status": "ok"}`))
}
