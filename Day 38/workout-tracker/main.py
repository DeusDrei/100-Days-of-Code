import requests
from datetime import datetime

APP_ID = "app_id"
API_KEY = "api_key"
exercise_endpoint = "endpoint"
gsheet_post_endpoint = "g_sheet_endpoint"

headers = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY
}

parameters = {
    "query": input("Tell me which exercises you did: ")
}

response_query = requests.post(url=exercise_endpoint, json=parameters, headers=headers)
new_list = response_query.json()


today = datetime.now()


for i in new_list["exercises"]:

    to_input = {
        "workout": {
            "date": today.strftime("%d/%m/%Y"),
            "time": today.strftime("%X"),
            "exercise": i["name"].title(),
            "duration": i["duration_min"],
            "calories": i["nf_calories"]
        }
    }

    response_post = requests.post(gsheet_post_endpoint, json=to_input)
    print(response_post.text)
