import requests

home_url = "https://api.github.com/users/"

user_name = input("Enter your GitHub Username:\t")

user_url = home_url + user_name

response = requests.get(user_url)

if response.status_code == 200:
    user_data = response.json()
    print(f"Fetching {user_name}'s data ...\n")
    print(f"User name : {user_data.get('name')}")
    print(f"Name : {user_data.get('login')}")
    print(f"About : {user_data.get('bio')}")
    print(f"Location : {user_data.get('location')}")
    print(f"Number of public repos : {user_data.get('public_repos')}\n")
else:
    print(f"Failed to fetch {user_name}'s data.\nError Code {response.status_code} !")