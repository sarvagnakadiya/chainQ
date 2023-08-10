from flask import Flask, request, jsonify
from agent_executor import get_answer

app = Flask(__name__)

@app.route('/get_answer', methods=['POST'])
def get_answer_route():
    try:
        user_prompt = request.json['user_prompt']  # Assuming the input is sent as JSON in the request body
        
        answer = get_answer(user_prompt)
        return jsonify({'answer': answer})
    except Exception as e:
        return jsonify({'error': str(e)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)