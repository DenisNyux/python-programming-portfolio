import requests
import json

def get_weather_data(place: str, api_key: str = None)-> json:
    result = None
    try:
        req = requests.get("http://api.openweathermap.org/data/2.5/weather",
                            params={'q': place, 'units': 'metric', 'appid': api_key})
        data = req.json()
        # print(type(data))
        frm_data = {
            "name": data['name'],
            "coord": {
                "lon": data['coord']['lon'],
                "lat": data['coord']['lat']
            },
            "country": data['sys']['country'],
            # "temperature": data['main']['temp'],
            "feels_like": data['main']['feels_like'],            
            "timezone": 'UTC+' + str(data['timezone']//3600) if data['timezone']//3600>0 else 'UTC' + str(data['timezone']//3600)
        }
        result = json.dumps(frm_data)
    except Exception as e:
        print("Exception:", e)
    return result



def get_id(path: str)-> str:
    with open(path, "r") as key:
        return key.readlines()[0]

if __name__ == "__main__":
    cities = ["Saint Petersburg,RU", "Chicago,USA", "Dhaka,BD"]
    key = get_id('./appid.txt')
    # names = ['name', 'coord', 'country', 'feels_like']
    for city in cities:
        assert type(get_weather_data(city, key)) == str
        print(get_weather_data(city, key)) 
        assert ('name', 'coord' in get_weather_data(city, key)) and ('country', 'feels_like' in get_weather_data(city, key))
