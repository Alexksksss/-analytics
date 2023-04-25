import requests
import json

access_token = "YOUR_TOKEN"

# поиск айди страны
method_name = 'database.getCountries'
url = f'https://api.vk.com/method/{method_name}'
params = {
    "code": 'RU',
    "v": 5.131,
    "access_token": access_token
}
country_id = requests.get(url, params=params).json()["response"]['items'][0]['id']

# поиск айди города
method_name = 'database.getCities'
city_name = 'Томск'
url = f'https://api.vk.com/method/{method_name}'
params = {
    "country_id": country_id,
    "q": city_name,
    "count": 1,
    "v": 5.131,
    "access_token": access_token
}
city_id = requests.get(url, params=params).json()["response"]['items'][0]['id']

# поиск университетов
method_name = 'database.getUniversities'
url = f'https://api.vk.com/method/{method_name}'
params = {
    "city_id": city_id,
    "v": 5.131,
    "access_token": access_token
}
universities = requests.get(url, params=params).json()["response"]['items']

# поиск факультетов
univ_list = []
method_name = 'database.getFaculties'
url = f'https://api.vk.com/method/{method_name}'
for uni in universities:
    uni_id = uni['id']
    params = {
        "university_id": uni_id,
        "v": 5.131,
        "access_token": access_token
    }

    faculties = requests.get(url, params=params).json()["response"]['items']
    univ_list.append({
        "universities": uni,
        "faculties": faculties
    })

result_l = {
    "cities": [{
        "city_id": city_id,
        "name": city_name,
        "universities": univ_list
    }]
}
# result_str=(str(result_l)).replace(", 'universities': [{",', ',1)
# print(result_str)


with open("task1.json", "w") as f:
    result = {"result": result_l}
    json.dump(result, f, ensure_ascii=False)