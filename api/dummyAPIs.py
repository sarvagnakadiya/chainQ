from flask import Flask, request, jsonify
from flask_cors import CORS  
from dotenv import load_dotenv
import os

load_dotenv()

app = Flask(__name__)

CORS(app)  # Use CORS with your Flask app

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Dummy Answer API! Send a POST request to /get_answer with a JSON body containing 'user_prompt' to get a dummy answer."

@app.route('/get_answer', methods=['POST'])
def get_dummy_answer():
    try:
        user_prompt = request.json['user_prompt']  # Assuming the input is sent as JSON in the request body
        
        # Dummy response
        dummy_answer = "This is a dummy answer for the prompt: " + user_prompt
        return jsonify({'answer': dummy_answer})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5002)
