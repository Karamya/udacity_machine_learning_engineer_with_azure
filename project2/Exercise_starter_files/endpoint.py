import requests
import json

# URL for the web service, should be similar to:
# 'http://8530a665-66f3-49c8-a953-b82a2d312917.eastus.azurecontainer.io/score'
scoring_uri = "http://eb1db414-aaab-4cc7-a7bd-709c6463f17c.germanywestcentral.azurecontainer.io/score"

# If the service is authenticated, set the key or token
key = "vV4iqX7EfEa9NAVi2XhaP4omHR0kdlko"

# Two sets of data to score, so we get two results back
data = {
    "Inputs": {
        "data": [
            {
                "instant": 1,
                "date": "2013-01-01 00:00:00,000000",
                "season": 1,
                "yr": 0,
                "mnth": 1,
                "weekday": 6,
                "weathersit": 2,
                "temp": 0.344167,
                "atemp": 0.363625,
                "hum": 0.805833,
                "windspeed": 0.160446,
                "casual": 331,
                "registered": 654,
            },
        ]
    },
    "GlobalParameters": 0.0,
}
# Convert to JSON string
input_data = json.dumps(data)
with open("data.json", "w") as _f:
    _f.write(input_data)

# Set the content type
headers = {"Content-Type": "application/json"}
# If authentication is enabled, set the authorization header
headers["Authorization"] = f"Bearer {key}"

# Make the request and display the response
resp = requests.post(scoring_uri, input_data, headers=headers)
print(resp.json())
