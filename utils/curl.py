import subprocess #import modules to run system command
import json

# Define your accounts array
account = [
    {"username": "svtqa", "password": "password"}
]

def execute_curl_command(curl_command):
    process = subprocess.Popen(curl_command, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    stdout, stderr = process.communicate()
    return process.returncode, stdout, stderr

def get_token_and_launch_game(username, password):
    # Step 1: Get the token
    curl_login = (
        'curl -X POST https://dummy.pwqr820.com:8080/api/login '
        '-H "Content-Type: application/json" '
        '-H "Accept-Language: en" '
        '-d "{{\\"username\\":\\"{}\\",\\"password\\":\\"{}\\"}}"'.format(username, password)
    )

    returncode, stdout, stderr = execute_curl_command(curl_login)

    if returncode != 0:
        print("Error getting token for {}: {}".format(username, stderr))
        return None

    try:
        response_data = json.loads(stdout)
        token = response_data.get('data').get('token')
        print("Token for {}: {}".format(username, token))
    except (json.JSONDecodeError, AttributeError):
        print("Failed to parse JSON response or token not found.")
        return None

    # Step 2: Use the token in the authorization header
    curl_authorized = (
        'curl https://dummy.pwqr820.com:8080/api/game/launch/26/216 '
        '-H "Accept: application/json" '
        '-H "Accept-Language: en" '
        '-H "Authorization: Bearer {}"'.format(token)
    )

    returncode, stdout, stderr = execute_curl_command(curl_authorized)

    if returncode != 0:
        print("Error launching game for {}: {}".format(username, stderr))
        return None

    try:
        response_data = json.loads(stdout)
        url = response_data.get('data').get('url')
        print("Lobby launch URL for {}: {}".format(username, url))
        return url  # Return the game URL
    except (json.JSONDecodeError, AttributeError):
        print("Failed to parse JSON response or URL not found.")
        return None

# Entry point for script execution
if __name__ == "__main__":
    for account in account:
        get_token_and_launch_game(account["username"], account["password"])