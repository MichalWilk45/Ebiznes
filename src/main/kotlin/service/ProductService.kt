package service

object ProductService {
    private val categories = listOf("Elektronika", "Książki", "Odzież", "Sport", "Jedzenie")

    private val products = mapOf(
        "elektronika" to listOf("Laptop", "Smartfon", "Kamera"),
        "książki" to listOf("Harry Potter", "Wiedźmin", "Clean Code"),
        "odzież" to listOf("Koszulka", "Jeansy", "Kurtka"),
        "sport" to listOf("Piłka", "Rower", "Hantle"),
        "jedzenie" to listOf("Chleb", "Ser", "Pizza")
    )

    fun getCategories(): String {
        return "Dostępne kategorie: " + categories.joinToString(", ")
    }

    fun getProducts(category: String): String {
        val normalizedCategory = category.lowercase()
        return products[normalizedCategory]?.joinToString(", ")
            ?.let { "Produkty w kategorii $category: $it" }
            ?: "Nie znaleziono kategorii: $category"
    }
}
