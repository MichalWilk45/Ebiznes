package main

import (
	"log"
	"net/http"
	"server_/handlers"
)

func main() {
	http.HandleFunc("/products", handlers.GetProducts)
	http.HandleFunc("/payment", handlers.HandlePayment)

	log.Println("Server listening on port 8080...")
	log.Fatal(http.ListenAndServe(":8080", nil))
}
