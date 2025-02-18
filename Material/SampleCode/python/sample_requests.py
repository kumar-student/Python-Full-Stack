import requests
from requests.exceptions import HTTPError

try:
    response = requests.get("https://api.github.com/")
    print(response.status_code)
    if response:
        print("Request succesfull")
        response.encoding="utf-8"
        print(response.headers)
    else:
        print("Request failed")
except HTTPError as e:
    print("HTTP Error: {e}")
except Exception as e:
    print(f"Occurred: {e}")