from flask import Flask, request
import os
from twilio.twiml.messaging_response import MessagingResponse
from google.cloud import dialogflow_v2 as dialogflow
import uuid

# Ensure your service account file is recognized
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow-service-key.json"

# Initialize Flask app
app = Flask(__name__)

# Root route to confirm the app is live
@app.route("/")
def home():
    return "Sevo Neera @2026 WhatsApp bot is running."

# Webhook route for Twilio
@app.route("/webhook", methods=["POST"])
def webhook():
    incoming_msg = request.values.get("Body", "")
    phone_number = request.values.get("From", "")
    
    session_id = str(uuid.uuid4())
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path("sevoneera-2026-bxgr", session_id)

    text_input = dialogflow.types.TextInput(text=incoming_msg, language_code="en")
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        reply = response.query_result.fulfillment_text
    except Exception as e:
        reply = "Sorry, something went wrong while contacting Dialogflow."
        print(f"[ERROR] {e}")

    # Reply via Twilio
    twilio_response = MessagingResponse()
    twilio_response.message(reply)
    return str(twilio_response)

if __name__ == "__main__":
    app.run()
