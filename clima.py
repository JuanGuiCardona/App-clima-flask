import requests

def get_weather(city):
    api_key = "8965b46da079e92d08cb1c58a8828f0f"
    base_url = "http://api.openweathermap.org/data/2.5/weather?"
    complete_url = f"{base_url}q={city}&lang=es&appid={api_key}&units=metric"
    response = requests.get(complete_url)

    if response.status_code == 200:
        data = response.json()
        main = data['main']
        wind = data['wind']
        weather_description = data['weather'][0]['description']


    return{
        "Temperature": main['temp'],
        "pressure": main['pressure'],
        "Humidity": main['humidity'],
        "Wind_Speed": wind['speed'],
        "Description": weather_description 
    }

