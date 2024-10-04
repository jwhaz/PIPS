import string
import random
import requests
import uuid

def generate_conversation_id():
    return str(uuid.uuid4())
def generate_error_code():
    return str(random.randint(100000, 999999))

def send_to_discord_error(error_code, error_message):   
    webhook_url = "https://discordapp.com/api/webhooks/1278486604574621808/SAsTInDa0JDXVSdcd874j8kQP6SAvkDg3Au823E1nszFyhZD6NyYuR2K4xnGZKnKhBsu"
    
    content = f"⚠️ **Error Report** ⚠️\n\n"
    content += f"Error Code: `{error_code}`\n"
    content += f"Error Message: {error_message}\n"
    
    payload = {"content": content}
    requests.post(webhook_url, json=payload)