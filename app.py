import os
from flask import Flask, request
from google.cloud import dialogflow_v2 as dialogflow
import json

app = Flask(__name__)

# Set the credentials environment variable
os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow-service-key.json"

# Dialogflow settings
DIALOGFLOW_PROJECT_ID = "sevoneera-2026-bxgr"
DIALOGFLOW_LANGUAGE_CODE = "en"
SESSION_ID = "me"

@app.route("/webhook", methods=["POST"])
def webhook():
    try:
        incoming_msg = request.json["Body"]
        response_text = detect_intent_text(incoming_msg)
        return response_text
    except Exception as e:
        return "Something went wrong while contacting Dialogflow"

def detect_intent_text(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)

    text_input = dialogflow.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.QueryInput(text=text_input)

    response = session_client.detect_intent(
        request={"session": session, "query_input": query_input}
    )

    return response.query_result.fulfillment_text

if __name__ == "__main__":
    app.run()
