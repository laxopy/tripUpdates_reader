import requests
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
from dotenv import load_dotenv
import json
import os

# Load environment variables from .env
load_dotenv()

# Obtain API key and API URL
api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL")

# Initialize headers dictionary
headers = {}

# If API key is present, add Authorization header
if api_key:
    headers["Authorization"] = api_key

try:
    # Make GET request with or without headers
    response = requests.get(api_url, headers=headers)

    if response.status_code == 200:
        # Parse GTFS-RT protobuf message
        feed = gtfs_realtime_pb2.FeedMessage()
        feed.ParseFromString(response.content)

        # Convert protobuf to dictionary
        feed_dict = MessageToDict(feed)

        # Save to JSON file
        with open("gtfs_rt.json", "w") as json_file:
            json.dump(feed_dict, json_file, indent=2)

        print("Response successfully written to gtfs_rt.json")
    else:
        print(f"Error: Received status code {response.status_code}")

except requests.exceptions.RequestException as e:
    print(f"Request failed: {e}")
