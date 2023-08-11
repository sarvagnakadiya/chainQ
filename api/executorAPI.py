from flask import Flask, request, jsonify
from flask_cors import CORS  
from langchain import OpenAI, SQLDatabase
from langchain.agents import create_sql_agent
from langchain.agents.agent_toolkits import SQLDatabaseToolkit
from langchain.sql_database import SQLDatabase
from langchain.llms.openai import OpenAI
from langchain.agents import AgentExecutor
from langchain.agents.agent_types import AgentType
from langchain.chat_models import ChatOpenAI
from dotenv import load_dotenv
import os

load_dotenv()

OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

db = SQLDatabase.from_uri('sqlite:///chainQ.db')
toolkit = SQLDatabaseToolkit(db=db, llm=OpenAI(temperature=0))

agent_executor = create_sql_agent(
    llm=OpenAI(temperature=0),
    toolkit=toolkit,
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

def get_answer(user_prompt):
    try:
        answer = agent_executor.run(user_prompt)
        return answer
    except Exception as e:
        return str(e)
app = Flask(__name__)

CORS(app)  # Use CORS with your Flask app

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
    app.run(host='0.0.0.0', port=5001)
