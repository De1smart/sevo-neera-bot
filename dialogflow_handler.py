
import os
from google.cloud import dialogflow_v2 as dialogflow
from google.api_core.exceptions import InvalidArgument

os.environ["GOOGLE_APPLICATION_CREDENTIALS"] = "dialogflow-service-key.json"
DIALOGFLOW_PROJECT_ID = "sevoneera-2026-bxgr"
DIALOGFLOW_LANGUAGE_CODE = "en"
SESSION_ID = "current-user-id"

def get_dialogflow_reply(text):
    session_client = dialogflow.SessionsClient()
    session = session_client.session_path(DIALOGFLOW_PROJECT_ID, SESSION_ID)
    text_input = dialogflow.types.TextInput(text=text, language_code=DIALOGFLOW_LANGUAGE_CODE)
    query_input = dialogflow.types.QueryInput(text=text_input)

    try:
        response = session_client.detect_intent(request={"session": session, "query_input": query_input})
        return response.query_result.fulfillment_text
    except InvalidArgument:
        return "Something went wrong while contacting Dialogflow."
