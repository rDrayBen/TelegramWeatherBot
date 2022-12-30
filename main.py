from langdetect import detect
import pyowm
import telebot
from pyowm.utils.config import get_default_config
from langdetect import DetectorFactory

DetectorFactory.seed = 0
owm = pyowm.OWM('c573593d16b4a358d2173235964ff4bd')
bot = telebot.TeleBot("5056359791:AAGnked4PGcSXLQarE9hB7IE0h0EhawaFu8")
mgr = owm.weather_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
    lang = detect(message.text)
    if lang == "uk":
        config_dict = get_default_config()
        config_dict['language'] = 'ua'
        observation = mgr.weather_at_place(message.text)
        WeatherResult = observation.weather
        curr_temperature = str(WeatherResult.temperature('celsius')["temp"])
        min_temperature = str(WeatherResult.temperature('celsius')["temp_min"])
        max_temperature = str(WeatherResult.temperature('celsius')["temp_max"])
        humidity = str(WeatherResult.humidity)

        if 'сонячно' in WeatherResult.detailed_status:
            answer = "В " + message.text + " зараз " + WeatherResult.detailed_status + "☀️\n\n"
        elif 'дощ' in WeatherResult.detailed_status:
            answer = "В " + message.text + " зараз " + WeatherResult.detailed_status + "🌧\n\n"
        elif 'хмарно' in WeatherResult.detailed_status:
            answer = "В " + message.text + " зараз " + WeatherResult.detailed_status + "☁️\n\n"
        answer += "Температура зараз близько " + curr_temperature + " градусів Цельсію" + "\n\n"
        answer += "Мінімальна температура на сьогодні " + min_temperature + " градусів Цельсію" + "\n\n"
        answer += "Максимальна температура на сьогодні " + max_temperature + " градусів Цельсію" + "\n\n"
        if int(humidity) > 50:
            answer += "Вологість приблизно " + humidity + "%💦\n\n"
        else:
            answer += "Вологість приблизно " + humidity + "%💧\n\n"

        bot.send_message(message.chat.id, answer)
    else:
        config_dict = get_default_config()
        config_dict['language'] = 'en'
        observation = mgr.weather_at_place(message.text)
        WeatherResult = observation.weather
        curr_temperature = str(WeatherResult.temperature('celsius')["temp"])
        min_temperature = str(WeatherResult.temperature('celsius')["temp_min"])
        max_temperature = str(WeatherResult.temperature('celsius')["temp_max"])
        humidity = str(WeatherResult.humidity)

        if 'sun' in WeatherResult.detailed_status:
            answer = "In " + message.text + " now " + WeatherResult.detailed_status + "☀️\n\n"
        elif 'rain' in WeatherResult.detailed_status:
            answer = "In " + message.text + " now " + WeatherResult.detailed_status + "🌧\n\n"
        elif 'clouds' in WeatherResult.detailed_status:
            answer = "In " + message.text + " now " + WeatherResult.detailed_status + "☁️\n\n"
        answer += "Temperature is now around " + curr_temperature + " degree celsius" + "\n\n"
        answer += "Min temperature for today is " + min_temperature + " degree celsius" + "\n\n"
        answer += "Max temperature for today is " + max_temperature + " degree celsius" + "\n\n"
        if int(humidity) > 50:
            answer += "Humidity is about " + humidity + "%💦\n\n"
        else:
            answer += "Humidity is about " + humidity + "%💧\n\n"
        bot.send_message(message.chat.id, answer)



bot.infinity_polling()

