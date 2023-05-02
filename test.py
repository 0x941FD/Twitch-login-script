import requests

# Replace these values with your own Client ID, Client Secret, and access token
client_id = "your_client_id_here"
client_secret = "your_client_secret_here"
access_token = "your_access_token_here"

# Define the endpoint URL for the Twitch API's user authentication method
auth_url = "https://id.twitch.tv/oauth2/validate"

# Set the authorization headers for the API request
headers = {
    "Client-ID": client_id,
    "Authorization": f"OAuth {access_token}"
}

# Send the API request to the user authentication endpoint
response = requests.get(auth_url, headers=headers)

# Check the response status code to ensure that the authentication was successful
if response.status_code == 200:
    # Authentication successful, print the user ID and login name
    user_data = response.json()
    user_id = user_data["user_id"]
    login_name = user_data["login"]
    print(f"User authenticated! User ID: {user_id}, Login Name: {login_name}")
else:
    # Authentication failed, print the error message
    error_data = response.json()
    error_message = error_data["message"]
    print(f"Authentication failed: {error_message}")
