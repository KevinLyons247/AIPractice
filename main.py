from flask import Flask, render_template, request, jsonify, session
import openai
from dotenv import load_dotenv
import os
from datetime import datetime

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
app.secret_key = os.urandom(24)  # Required for session management

# Initialize OpenAI
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/')
def home():
    # Initialize conversation history if it doesn't exist
    if 'conversation' not in session:
        session['conversation'] = []
    return render_template('index.html', conversation=session.get('conversation', []))

@app.route('/get_response', methods=['POST'])
def get_response():
    user_input = request.json.get('message', '')
    try:
        # Get existing conversation history
        conversation = session.get('conversation', [])
        
        # Add user message to history
        conversation.append({
            'role': 'user',
            'content': user_input,
            'timestamp': datetime.now().strftime('%H:%M:%S')
        })
        
        # Get AI response
        response = openai.ChatCompletion.create(
            model="gpt-3.5-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful AI assistant."},
                *[{"role": msg['role'], "content": msg['content']} for msg in conversation]
            ]
        )
        
        ai_response = response.choices[0].message['content']
        
        # Add AI response to history
        conversation.append({
            'role': 'assistant',
            'content': ai_response,
            'timestamp': datetime.now().strftime('%H:%M:%S')
        })
        
        # Update session
        session['conversation'] = conversation
        
        return jsonify({
            "response": ai_response,
            "conversation": conversation
        })
    except Exception as e:
        return jsonify({"error": str(e)}), 500

@app.route('/clear_history', methods=['POST'])
def clear_history():
    session['conversation'] = []
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(debug=True)
