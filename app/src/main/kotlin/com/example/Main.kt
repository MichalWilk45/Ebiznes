package com.example

import dev.kord.core.Kord
import dev.kord.core.event.listener
import dev.kord.rest.builder.message.create
import io.ktor.application.*
import io.ktor.features.ContentNegotiation
import io.ktor.http.ContentType
import io.ktor.jackson.jackson
import io.ktor.response.respond
import io.ktor.routing.Route
import io.ktor.routing.get
import io.ktor.server.engine.embeddedServer
import io.ktor.server.netty.Netty
import io.ktor.server.routing.routing
import kotlinx.coroutines.launch
import kotlinx.coroutines.runBlocking
import io.github.cdimascio.dotenv.Dotenv

fun main() {
    //Załadowanie zmiennych z pliku .env
    val dotenv = Dotenv.load()
    val discordToken = dotenv["DISCORD_TOKEN"]

    // Rozpoczęcie serwera Ktor
    embeddedServer(Netty, port = 8080) {
        install(ContentNegotiation) {
            jackson { }
        }

        routing {
            // Trasa do testu
            get("/ping") {
                call.respond("Pong!")
            }
        }
    }.start(wait = false)

    // Uruchomienie bota Discord
    runBlocking {
        val bot = Kord(discordToken!!)

        bot.on<Event> {
            println("Bot uruchomiony!")
        }

        bot.login()
    }
}
