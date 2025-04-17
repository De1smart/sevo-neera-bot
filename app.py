
from flask import Flask, request
from twilio.twiml.messaging_response import MessagingResponse
import dialogflow_handler

app = Flask(__name__)

@app.route('/webhook', methods=['POST'])
def webhook():
    incoming_msg = request.values.get('Body', '').strip()
    resp = MessagingResponse()
    reply = dialogflow_handler.get_dialogflow_reply(incoming_msg)
    resp.message(reply)
    return str(resp)

if __name__ == '__main__':
    app.run(debug=True)
