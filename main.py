import pyowm
import telebot

owm = pyowm.OWM('c573593d16b4a358d2173235964ff4bd')
bot = telebot.TeleBot("5056359791:AAGnked4PGcSXLQarE9hB7IE0h0EhawaFu8", parse_mode=None)

mgr = owm.weather_manager()


@bot.message_handler(content_types=['text'])
def send_echo(message):
    observation = mgr.weather_at_place(message.text)
    WeatherResult = observation.weather
    curr_temperature = str(WeatherResult.temperature('celsius')["temp"])
    min_temperature = str(WeatherResult.temperature('celsius')["temp_min"])
    max_temperature = str(WeatherResult.temperature('celsius')["temp_max"])
    humidity = str(WeatherResult.humidity)

    answer = "In " + message.text + " now " + WeatherResult.detailed_status + "\n\n"
    answer += "Temperature is now around " + curr_temperature + "\n\n"
    answer += "Min temperature for today is " + min_temperature + "\n\n"
    answer += "Max temperature for today is " + max_temperature + "\n\n"
    answer += "Humidity is about " + humidity + "\n\n"

    bot.send_message(message.chat.id, answer)
bot.infinity_polling()

