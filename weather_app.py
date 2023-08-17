import requests

def get_weather_data(city):
    api_key = "1f46d6f85b46afdedf4e35da7f032a61"
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    response = requests.get(base_url, params=params)
    data = response.json()

    return data

def main():
    city = input("Introdu numele orașului: ")

    weather_data = get_weather_data(city)

    if weather_data["cod"] == 200:
        temperature = weather_data["main"]["temp"]
        weather_description = weather_data["weather"][0]["description"]

        print(f"Temperatura în {city} este de {temperature} °C.")
        print(f"Descriere: {weather_description}")
    else:
        print("Nu s-a putut obține datele despre vreme.")

if __name__ == "__main__":
    main()
