from langdetect import detect
import pyowm
import telebot
from pyowm.utils.config import get_default_config
from langdetect import DetectorFactory
from datetime import date
from datetime import timedelta

DetectorFactory.seed = 0
owm = pyowm.OWM('c573593d16b4a358d2173235964ff4bd')
bot = telebot.TeleBot("5056359791:AAGnked4PGcSXLQarE9hB7IE0h0EhawaFu8")
mgr = owm.weather_manager()
coor = owm.geocoding_manager()

@bot.message_handler(content_types=['text'])
def send_echo(message):
    lang = detect(message.text)
    if '7' not in message.text:
        if lang == "uk":
            config_dict = get_default_config()
            config_dict['language'] = 'ua'
            try:
                observation = mgr.weather_at_place(message.text)
            except pyowm.commons.exceptions.NotFoundError as notFound:
                bot.send_message(message.chat.id, 'Ми не знайшли такого місця, можливо ви помилились, спробуйте ще раз')
                return
            WeatherResult = observation.weather
            curr_temperature = str(WeatherResult.temperature('celsius')["temp"])
            min_temperature = str(WeatherResult.temperature('celsius')["temp_min"])
            max_temperature = str(WeatherResult.temperature('celsius')["temp_max"])
            humidity = str(WeatherResult.humidity)

            if 'сонячно' in WeatherResult.detailed_status:
                answer = "В " + message.text + " зараз " + WeatherResult.detailed_status + "☀️\n\n"
            elif 'дощ' in WeatherResult.detailed_status:
                answer = "В " + message.text + " зараз " + WeatherResult.detailed_status + "🌧\n\n"
            elif 'хмар' in WeatherResult.detailed_status:
                answer = "В " + message.text + " зараз " + WeatherResult.detailed_status + "☁️\n\n"
            else:
                answer = "В " + message.text + " зараз " + WeatherResult.detailed_status + "\n\n"
            answer += "Температура зараз близько " + curr_temperature + " °С" + "\n\n"
            answer += "Мінімальна температура на сьогодні " + min_temperature + " °С" + "\n\n"
            answer += "Максимальна температура на сьогодні " + max_temperature + " °С" + "\n\n"
            if int(humidity) > 50:
                answer += "Вологість приблизно " + humidity + "%💦\n\n"
            else:
                answer += "Вологість приблизно " + humidity + "%💧\n\n"

            bot.send_message(message.chat.id, answer)
        else:
            config_dict = get_default_config()
            config_dict['language'] = 'en'
            try:
                observation = mgr.weather_at_place(message.text)
            except pyowm.commons.exceptions.NotFoundError as notFound:
                bot.send_message(message.chat.id,'No such place, maybe you spelled it wrong')
                return
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
            else:
                answer = "In " + message.text + " now " + WeatherResult.detailed_status + "\n\n"
            answer += "Temperature is now around " + curr_temperature + " °С" + "\n\n"
            answer += "Min temperature for today is " + min_temperature + " °С" + "\n\n"
            answer += "Max temperature for today is " + max_temperature + " °С" + "\n\n"
            if int(humidity) > 50:
                answer += "Humidity is about " + humidity + "%💦\n\n"
            else:
                answer += "Humidity is about " + humidity + "%💧\n\n"

            bot.send_message(message.chat.id, answer)
    else:
        answer = ''
        if lang == "uk":
            config_dict = get_default_config()
            config_dict['language'] = 'ua'
            try:
                observation = mgr.weather_at_place((message.text).split(' ')[0])
            except pyowm.commons.exceptions.NotFoundError as notFound:
                bot.send_message(message.chat.id, 'Ми не знайшли такого місця, можливо ви помилились, спробуйте ще раз')
                return
            list_locations = coor.geocode((message.text).split(' ')[0])
            one_call = mgr.one_call(list_locations[0].lat, list_locations[0].lon)

            answer += f'Прогноз погоди у {(message.text).split(" ")[0]} на наступні 7 днів: \n'
            for i in range(7):
                today = date.today() + timedelta(days=i)
                answer += 'Дата: ' + str(today) + '  Температура: '
                answer += str(one_call.forecast_daily[i].temperature('celsius')['day'])
                answer += '°С  Погода: '
                answer += str(one_call.forecast_daily[i].detailed_status)
                answer += '\n'

            bot.send_message(message.chat.id, answer)
        else:
            config_dict = get_default_config()
            config_dict['language'] = 'en'
            try:
                observation = mgr.weather_at_place((message.text).split(' ')[0])
            except pyowm.commons.exceptions.NotFoundError as notFound:
                bot.send_message(message.chat.id,'No such place, maybe you spelled it wrong')
                return
            list_locations = coor.geocode((message.text).split(' ')[0])
            one_call = mgr.one_call(list_locations[0].lat, list_locations[0].lon)

            answer += f'Weather forecast in {(message.text).split(" ")[0]} for the next 7 days: \n'
            for i in range(7):
                today = date.today() + timedelta(days=i)
                # answer += 'Date: '+ str(today) + '  Temperature: ' + str(one_call.forecast_daily[i].temperature('celsius')[
                #     'day']) + '°С  Weather: ' + str(one_call.forecast_daily[i].detailed_status)
                answer += 'Date: ' + str(today) + '  Temperature: '
                answer += str(one_call.forecast_daily[i].temperature('celsius')['day'])
                answer += '°С  Weather: '
                answer += str(one_call.forecast_daily[i].detailed_status)
                answer += '\n'

            bot.send_message(message.chat.id, answer)


bot.polling(non_stop=True)

