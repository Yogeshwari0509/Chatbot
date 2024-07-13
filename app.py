from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def index():
    return "Chatbot is running!"

@app.route('/chat', methods=['POST'])
def chat():
    user_input = request.json.get('message')
    response = get_response(user_input)
    return jsonify({"response": response})

def get_response(user_input):
    # Basic rule-based responses
    if "hello" in user_input.lower():
        return "Hello! How can I help you today?"
    elif "bye" in user_input.lower():
        return "Goodbye! Have a great day!"
    else:
        return "I'm not sure how to respond to that."

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
