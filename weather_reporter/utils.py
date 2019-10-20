import requests

#api_key = "API_Key"
BASE_URL = "https://weather.com/"
TYPE_URL = BASE_URL + "type/"
LOCATION_SEARCH_URL = BASE_URL + "location/search/"
WEATHER_INFO_URL = TYPE_URL + "location/{}/"


def get_location_id(query):
	"""
	get location id
	"""
    r = requests.get(LOCATION_SEARCH_URL, params={'query':query})
    data = r.json()
    if len(data):
        return data[0]['woeid']


def get_weather(query, date, type):
	"""
	get weather data
	"""
	location_id = get_location_id(query)
	if location_id is None:
		return "Location not found."
	r = requests.get(WEATHER_INFO_URL.format(location_id,date,type))
	data = r.json()
	result = {}
	result['location'] = data['title']
	result['weather'] = []
	for day_weather in data['consolidated_weather']:
	    result['weather'].append({
	        'date': day_weather['applicable_date'],
	        'min_temp': round(day_weather['min_temp'], 2),
	        'max_temp': round(day_weather['max_temp'], 2),
	        'weather_state_name': day_weather['weather_state_name']
	    })
	return result


def print_weather_details(data):
	"""
	print weather details
	"""
    print("Location:", data['location'], end='\n\n')
    for row in data['weather']:
        print("Date:", row['date'])
        print("Weather Type:", row['weather_state_name'])
        print("Min Temp.:", row['min_temp'])
        print("Max Temp.:", row['max_temp'])
