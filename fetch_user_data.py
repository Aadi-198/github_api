import requests

home_url = "https://api.github.com/users/"

user_name = input("Enter your GitHub Username:\t")

user_url = home_url + user_name

response = requests.get(user_url)

if response.status_code == 200:
    print(f"Fetching {user_name}'s data")
else:
    print(f"Failed to fetch {user_name}'s data.\nError Code {response.status_code} !")