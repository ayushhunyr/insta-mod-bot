from instagrapi import Client
import time
import os
import re

# Hosting settings (Inhe hum Render par setup karenge)
USERNAME = os.environ.get("INSTA_USER")
PASSWORD = os.environ.get("INSTA_PASS")
GROUP_ID = os.environ.get("GROUP_ID")

cl = Client()

def run_bot():
    try:
        # Instagram login
        print(f"Logging in as {USERNAME}...")
        cl.login(USERNAME, PASSWORD)
        print("Logged in successfully!")

        # URL detect karne ka pattern
        url_pattern = r'https?://[^\s]+|discord\.gg/|t\.me/'

        while True:
            # Group ke messages check karna
            thread = cl.direct_thread(GROUP_ID)
            messages = thread.messages
            
            for msg in messages:
                # Agar message mein link hai aur wo bot ne nahi bheja
                if re.search(url_pattern, str(msg.text).lower()):
                    try:
                        cl.direct_message_delete(GROUP_ID, msg.id)
                        print(f"Deleted a link: {msg.text}")
                    except Exception as delete_error:
                        print(f"Could not delete: {delete_error}")
            
            # 30 seconds ka wait taaki account ban na ho
            time.sleep(30)

    except Exception as e:
        print(f"Error occurred: {e}")
        print("Retrying in 60 seconds...")
        time.sleep(60)
        run_bot()

if __name__ == "__main__":
    run_bot()
