import os
from flask import Flask, request
import json
from twilio.twiml.messaging_response import MessagingResponse
import google.cloud.dialogflow_v2 as dialogflow  # Updated to the new Dialogflow package
import dialogflow_handler  # Make sure this is imported after the environment is set

# Set up the path to the service account key
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow-service-key.json"

# Initialize Flask app
app = Flask(__name__)

@app.route("/webhook", methods=["POST"])
def webhook():
    # Get the message from WhatsApp
    message_body = request.form['Body']
    sender_number = request.form['From']

    # Process message with Dialogflow
    response_text = dialogflow_handler.get_dialogflow_response(message_body)

    # Respond to the message on WhatsApp
    resp = MessagingResponse()
    resp.message(response_text)

    return str(resp)

if __name__ == "__main__":
    app.run(debug=True)
