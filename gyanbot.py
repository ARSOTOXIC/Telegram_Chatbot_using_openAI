import telebot
import openai

# Set up the OpenAI API key
openai.api_key = " your_openAI_key"

# Set up the Telegram bot
bot = telebot.TeleBot("your telegram bot id")

# Dictionary of predetermined responses
responses = {
    "What is your name,what is ": " Toxic often call me zygon",
    "what is the weather today?": "I'm sorry, I don't have that information.",
    "how/How old are you?": "I am a virtual assistant, so I don't have an age but my creator age is 20!",
    "how are you?": "I'm doing well, thank you for asking!",
    "who made you": "I was made with hate by toxic!"
}

# Handler for the /start command
@bot.message_handler(commands=['start'])
def start_command(message):
    bot.reply_to(message, "Hi there! How can I assist you today?")

# Handler for messages
@bot.message_handler(func=lambda message: True)
def chatbot_response(message):
    # Check if the message is a predetermined query
    if message.text.lower() in responses:
        bot.reply_to(message, responses[message.text.lower()])
    else:
        # Use OpenAI to generate a response
        response = openai.Completion.create(
            engine="text-davinci-003",
            prompt=f"{message.text}",
            temperature=0.5,
            max_tokens=600,
            n=1,
            stop=None,
        )
        
        # Send the response back to the user
        bot.reply_to(message, response.choices[0].text)

# Start the bot
bot.polling()
