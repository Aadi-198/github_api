import requests

home_url = "https://api.github.com/users/"

user_name = input("Enter your GitHub Username:\t")

user_url = home_url + user_name

user_response = requests.get(user_url)

if user_response.status_code == 200:
    user_data = user_response.json()
    print(f"\nFetching {user_name}'s data ...\n")
    print(f"Name : {user_data.get('name')}")
    print(f"User name : {user_data.get('login')}")
    print(f"About : {user_data.get('bio')}")
    print(f"Location : {user_data.get('location')}")
    print(f"Number of public repos : {user_data.get('public_repos')}\n")
else:
    print(f"Failed to fetch {user_name}'s data.\nError Code {user_response.status_code} !")

activity_url = user_url + "/events"

activity_response = requests.get(activity_url)

if activity_response.status_code == 200:
    activity_data = activity_response.json()
    print(f"Fetching {user_name}'s activity data ...\n")
    recent_activities = activity_data[:3]
    for count_activity in recent_activities:
        activity_id = count_activity.get('id')
        activity_type = count_activity.get('type')
        print(f"{activity_id} - {activity_type}")
    print()
else:
    print(f"Failed to fetch {user_name}'s activity data.\nError Code {activity_response.status_code} !")