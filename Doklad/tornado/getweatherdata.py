import requests
import json
import asyncio
import time


def get_id(path: str)-> str: 
    # json.dumps(dict)
    with open(path, "r") as key:
        return key.readlines()[0]

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

async def get_a_lot_of_data():
    key = get_id('./appid.txt')
    cities = ["Saint Petersburg,RU", "Orenburg,RU", "Samara,RU", "Ufa,RU", "Moscow, RU", "Kazan, RU" "Chicago,USA", "Dhaka,BD", "London,UK", "Paris, FR", "Paris, CA"]
    all_weather = []
    for city in cities:
        assert type(get_weather_data(city, key)) == str
        # print(get_weather_data(city, key)) 
        assert ('name', 'coord' in get_weather_data(city, key)) and ('country', 'feels_like' in get_weather_data(city, key))
        all_weather.append(get_weather_data(city, key))
    print('all data fetched')
    return all_weather

async def write_a_lot_of_data(data: list):
    for each in data:
        each = json.dumps(each)
    with open('result.txt', 'a', encoding='utf-8') as res:
        print(*data, file=res)
        print('\n', file=res)
    print('all data written')


async def main():
    while True:
        start_time = time.time()
        task1 = asyncio.create_task(get_a_lot_of_data())  
        await asyncio.sleep(10)
        value = await task1
        await write_a_lot_of_data(value)
        print("\n--- %s seconds ---" % (time.time() - start_time))
    
asyncio.run(main())
