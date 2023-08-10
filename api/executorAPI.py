from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['GET'])
def home():
    return "Welcome to the Answer Retrieval API! Send a POST request to /get_answer with a JSON body containing 'user_prompt' to get an answer."

@app.route('/get_answer', methods=['POST'])
def get_answer_route():
    try:
        user_prompt = request.json['user_prompt']  # Assuming the input is sent as JSON in the request body
        
        # You would need to import and implement the 'get_answer' function
        answer = get_answer(user_prompt)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)