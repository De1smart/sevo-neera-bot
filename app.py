from flask import Flask, jsonify
import os
import dialogflow_v2 as dialogflow

app = Flask(__name__)

# Google Cloud Dialogflow credentials (ensure the file exists and is in the correct location)
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow-service-key.json"

# Home route
@app.route('/')
def home():
    return "Bot is live and ready to serve requests!"

# Webhook route for handling messages
@app.route('/webhook', methods=['POST'])
def webhook():
    # This is where your chatbot code will handle incoming messages from Twilio/WhatsApp
    return jsonify({"status": "success"})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
