package bot

import net.dv8tion.jda.api.JDABuilder
import net.dv8tion.jda.api.entities.Activity
import net.dv8tion.jda.api.events.message.MessageReceivedEvent
import net.dv8tion.jda.api.hooks.ListenerAdapter
import service.ProductService

class DiscordBot(token: String) : ListenerAdapter() {
    private val jda = JDABuilder.createDefault(token)
        .addEventListeners(this)
        .setActivity(Activity.playing("Ktor & Discord!")) // Status bota
        .build()

    override fun onMessageReceived(event: MessageReceivedEvent) {
        val message = event.message.contentRaw
        val botMention = event.jda.selfUser.asMention

        if (message.startsWith(botMention)) {
            val response = handleUserMessage(message.removePrefix(botMention).trim())
            event.channel.sendMessage(response).queue()
        }
    }

    private fun handleUserMessage(message: String): String {
        return when {
            message == "categories" -> ProductService.getCategories()
            message.startsWith("products") -> {
                val category = message.removePrefix("products").trim()
                ProductService.getProducts(category)
            }
            else -> "Nie rozumiem tej wiadomości. 😕"
        }
    }
}
