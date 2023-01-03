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


def send_echo():
    message = input()
    config_dict = get_default_config()
    config_dict['language'] = 'en'
    try:
        observation = mgr.weather_at_place(message)
    except pyowm.commons.exceptions.NotFoundError as notFound:
        print('No such place, maybe u are wrong')
        return
    WeatherResult = observation.weather
    print(WeatherResult)
    # curr_temperature = str(WeatherResult.temperature('celsius')["temp"])
    # min_temperature = str(WeatherResult.temperature('celsius')["temp_min"])
    # max_temperature = str(WeatherResult.temperature('celsius')["temp_max"])
    # humidity = str(WeatherResult.humidity)
    # list_locations = coor.geocode(message)
    #
    # one_call = mgr.one_call(list_locations[0].lat, list_locations[0].lon)
    #
    #
    #
    #
    #
    # if 'sun' in WeatherResult.detailed_status:
    #     answer = "In " + message + " now " + WeatherResult.detailed_status + "☀️\n\n"
    # elif 'rain' in WeatherResult.detailed_status:
    #     answer = "In " + message + " now " + WeatherResult.detailed_status + "🌧\n\n"
    # elif 'clouds' in WeatherResult.detailed_status:
    #     answer = "In " + message + " now " + WeatherResult.detailed_status + "☁️\n\n"
    # else:
    #     answer = "In " + message + " now " + WeatherResult.detailed_status + "\n\n"
    # answer += "Temperature is now around " + curr_temperature + " degree celsius" + "\n\n"
    # answer += "Min temperature for today is " + min_temperature + " degree celsius" + "\n\n"
    # answer += "Max temperature for today is " + max_temperature + " degree celsius" + "\n\n"
    # if int(humidity) > 50:
    #     answer += "Humidity is about " + humidity + "%💦\n\n"
    # else:
    #     answer += "Humidity is about " + humidity + "%💧\n\n"
    # print(answer)
    # ans = ''
    # for i in range(7):
    #     today = date.today() + timedelta(days=i)
    #     ans +='Date: '+ str(today)+ '  Temperature: '+ one_call.forecast_daily[i].temperature('celsius')['day'] + \
    #           '°С  Weather: ' + str(one_call.forecast_daily[i].detailed_status) + '\n'
    # print(ans)


if __name__ == '__main__':
    send_echo()

