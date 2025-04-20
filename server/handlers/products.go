package handlers

import (
	"encoding/json"
	"net/http"
	"server_/models"
)

func GetProducts(w http.ResponseWriter, r *http.Request) {
	products := []models.Product{
		{ID: 1, Name: "Produkt A", Price: 10.99},
		{ID: 2, Name: "Produkt B", Price: 20.49},
	}

	w.Header().Set("Content-Type", "application/json")
	w.Header().Set("Access-Control-Allow-Origin", "*") // CORS
	json.NewEncoder(w).Encode(products)
}
