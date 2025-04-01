import io.ktor.server.application.*
import io.ktor.server.plugins.contentnegotiation.*
import io.ktor.server.response.*
import io.ktor.server.routing.*
import io.ktor.server.engine.*
import io.ktor.server.netty.*
import io.ktor.serialization.jackson.*
import io.github.cdimascio.dotenv.Dotenv
import bot.DiscordBot

fun main() {
    // Załadowanie zmiennych z pliku .env
    val dotenv = Dotenv.load()
    val discordToken = dotenv["DISCORD_TOKEN"] ?: run {
        println("ERROR: DISCORD_TOKEN not found in .env file")
        return
    }

    println("Starting Ktor server...")
    // Rozpoczęcie serwera Ktor
    embeddedServer(Netty, port = 8080) {
        install(ContentNegotiation) {
            jackson()
        }

        routing {
            // Trasa do testu
            get("/ping") {
                call.respond("Pong!")
            }
        }
    }.start(wait = false)
    println("Ktor server started on port 8080")

    // Uruchomienie bota Discord używając JDA
    println("Connecting to Discord...")
    try {
        val discordBot = DiscordBot(discordToken)
        println("Discord bot connected successfully!")
    } catch (e: Exception) {
        println("Error connecting to Discord: ${e.message}")
        e.printStackTrace()
    }
}