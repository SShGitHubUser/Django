# Токен для работы с API сайта OpenWeatherMap.org
OWM_TOKEN = ''

# Строка запроса информации о погоде с сайта OpenWeatherMap.org
OWM_URL = ''.join(['https://api.openweathermap.org/data/2.5/weather?q={city}&appid=',
                   OWM_TOKEN, '&units=metric&lang=','en']) # lang 'en','ua','ru'

# Токен для работы с API DRF в уроке 7, задаче 7
DRF_TOKEN = ''
