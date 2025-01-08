import os
import requests

# Specify the file to send
FILE_PATH = "sender/cat.jpg"
RECEIVER_URL = "http://receiver:5000/upload"

def send_file():
    # Check if the file exists
    if not os.path.exists(FILE_PATH):
        print(f"Error: File '{FILE_PATH}' not found!")
        return

    # Open the file in binary mode and send it via a POST request
    with open(FILE_PATH, "rb") as file:
        try:
            response = requests.post(RECEIVER_URL, files={"file": file})
            print(f"Response: {response.status_code} - {response.text}")
        except requests.exceptions.RequestException as e:
            print(f"Error: Could not connect to receiver. {e}")

if __name__ == "__main__":
    send_file()
