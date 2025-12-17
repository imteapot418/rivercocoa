import sys
import requests

# List of admin user IDs
admins = ["1323760864"]  # Replace with actual admin IDs
TOKEN = '5935490056:AAHW8E1skdr8to1C4KvxdCBO8yG0f2qe4WU'

def send_file_contents_to_admins(file_path, admins, token):
    # Read the contents of the file
    try:
        with open(file_path, 'r') as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return

    # Loop through the list of admin IDs and send the contents of the file
    for admin in admins:
        # Construct the message to send
        message = file_contents
        
        # Construct the Telegram Bot API URL
        send_text = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={admin}&text={message}'

        # Send the message via a GET request
        response = requests.get(send_text)

        # Check if the message was successfully sent
        if response.status_code == 200:
            print(f"File contents successfully sent to admin {admin}")
        else:
            print(f"Failed to send message to admin {admin}. Error: {response.text}")

# Main execution block
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python send_file_to_telegram.py <file_path>")
    else:
        file_path = sys.argv[1]
        send_file_contents_to_admins(file_path, admins, TOKEN)

    print("Mail Success")
