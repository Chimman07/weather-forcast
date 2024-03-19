import requests

API_key = "9fd4bf93cb93e839f2663982c26130c8"


def get_data(place, days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_key}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list']
    values = 8 * days
    filtered_data = filtered_data[:values]

    return filtered_data


if __name__ == "__main__":
    print(get_data(place="tokyo", days=2))
