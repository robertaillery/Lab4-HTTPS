import httpx

# IMPORTANT: Update this URL with the one from your Codespace's PORTS tab
url = "https://ominous-barnacle-g4wpg5rqj5v4cwqvr-3956.app.github.dev/"

# --- Existing GET requests ---
print("--- Testing GET request on root (/) ---")
response = httpx.get(url)
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")

# --- Existing POST request to /echo ---
mydata = {
    "text": "Hello Phil!",
    "param2": "Making a POST request",
    "body": "my own value"
}
print("\n--- Testing POST request on /echo ---")
response = httpx.post(url + "echo", data=mydata)
print(f"Status Code: {response.status_code}")
print(f"Response Text: {response.text}")


# --- NEW: POST request to test the /factors endpoint ---
factors_data = {'inINT': '12'}
print("\n--- Testing POST request on /factors with inINT=12 ---")
try:
    response = httpx.post(url + "factors", data=factors_data)
    print(f"Status Code: {response.status_code}")
    # The response is JSON, so we can print it directly
    print(f"Response JSON: {response.text}")
except httpx.RequestError as exc:
    print(f"An error occurred while requesting {exc.request.url!r}.")