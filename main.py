import requests
from google.transit import gtfs_realtime_pb2
from google.protobuf.json_format import MessageToDict
from dotenv import load_dotenv
import json
import os

# Load environment variables from .env
load_dotenv()

# Obtain api key and api url
api_key = os.getenv("API_KEY")
api_url = os.getenv("API_URL")

# Headers with authentication token
headers = {"Authorization": f"{api_key}"}

# GET request using headers
response = requests.get(api_url, headers=headers)

# Verify response
if response.status_code == 200:
    # Create the object FeedMessage
    feed = gtfs_realtime_pb2.FeedMessage()

    # Parse the protobuf response
    feed.ParseFromString(response.content)

    # Convert from Protobuf to dictionary
    feed_dict = MessageToDict(feed)

    # Show response in JSON format
    print(json.dumps(feed_dict, indent=2))
else:
    print(f"Error: {response.status_code}")
