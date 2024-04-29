import requests
from datetime import datetime

ID = "graph id"
USERNAME = "username"
TOKEN = "token"
pixela_endpoint = "https://pixe.la/v1/users"

parameters = {
    "token": TOKEN,
    "username": USERNAME,
    "agreeTermsOfService": "yes",
    "notMinor": "yes"
}

# response = requests.post(url=pixela_endpoint, json=parameters)
# print(response.text)

graph_endpoint = f"{pixela_endpoint}/{USERNAME}/graphs"

graph_config = {
    "id": ID,
    "name": "Study Time",
    "unit": "hours",
    "type": "float",
    "color": "kuro"
}

header = {
    "X-USER-TOKEN": TOKEN
}

# response = requests.post(url=graph_endpoint, json=graph_config, headers=header)
# print(response.text)

input_endpoint = f"{graph_endpoint}/{ID}"

today = datetime.now()

graph_input = {
    "date": today.strftime("%Y%m%d"),
    "quantity": input("How many hours did you study today?: ")
}

response = requests.post(url=input_endpoint, json=graph_input, headers=header)
print(response.text)

delete_endpoint = f"{input_endpoint}/20230911"

graph_update = {
    "quantity": "1"
}

# response = requests.delete(url=delete_endpoint, headers=header)
# print(response.text)
