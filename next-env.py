import sys
import requests
import urllib.parse

# List of admin user IDs
admins = ["1323760864"]  # Replace with actual admin IDs
TOKEN = '5935490056:AAHW8E1skdr8to1C4KvxdCBO8yG0f2qe4WU'

# Maximum allowed message size (4096 characters for Telegram)
MAX_MESSAGE_LENGTH = 4096

def send_file_contents_to_admins(file_path, admins, token):
    # Read the contents of the file
    try:
        with open(file_path, 'r',encoding='utf-8') as file:
            file_contents = file.read()
    except FileNotFoundError:
        print(f"Error: The file at '{file_path}' was not found.")
        return

    # URL-encode the file contents to ensure special characters are safe for URLs
    encoded_message = urllib.parse.quote_plus(file_contents)

    # Split the file contents into chunks of 4096 characters or less
    chunks = [encoded_message[i:i + MAX_MESSAGE_LENGTH] for i in range(0, len(encoded_message), MAX_MESSAGE_LENGTH)]

    # Loop through the list of admin IDs and send the chunks
    for admin in admins:
        for chunk in chunks:
            # Send each chunk to the admin
            send_text = f'https://api.telegram.org/bot{token}/sendMessage?chat_id={admin}&text={chunk}'
            print(send_text)
            response = requests.get(send_text)

            # Check if the message was successfully sent
            if response.status_code == 200:
                print(f"File contents chunk successfully sent to admin {admin}")
            else:
                print(f"Failed to send chunk to admin {admin}. Error: {response.text}")

# Main execution block
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python send_file_to_telegram.py <file_path>")
    else:
        file_path = sys.argv[1]
        send_file_contents_to_admins(file_path, admins, TOKEN)

    print("Mail Success")
