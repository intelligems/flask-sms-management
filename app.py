import json
import logging
import requests

from flask import Flask, jsonify, request, redirect
from twilio import twiml


app = Flask(__name__)

def send_to_slack(from_number, to_number, message_body):
    webhook_url = os.getenv('SLACK_WEBHOOK_URL', None)
    if not webhook_url:
        logging.error('Cannot proceed without the slack webhook url')
        return
    payload = {
        "text": "({} -> {}): {}".format(from_number, to_number, message_body)
    }
    requests.post(url=webhook_url, data=json.dumps(payload))
    logging.info("Sent message to slack")


def respond_with_sms(to, message):
    resp = twiml.Response()
    resp.message('Hello {}: {}'.format(number, message_body))


@app.route('/', methods=['GET'])
def index():
    return redirect("https://www.intelligems.eu", code=301)


@app.route('/sms/', methods=['POST'])
def sms():
    try:
        from_number = request.form['From']
        to_number = request.form['To']
        message_body = request.form['Body']
        send_to_slack(from_number, to_number, message_body)
        return "forwarded with success"
    except Exception as e:
        logging.error(e)
        return str(e)


if __name__ == '__main__':
    app.run()
