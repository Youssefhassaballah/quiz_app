import requests
import json

parameters = {
    "amount": 10,
    "type":"boolean"
}
response = requests.get("https://opentdb.com/api.php", parameters)
response.raise_for_status()
data = response.json()
question_data = data["results"]

