import json
import logging
import requests

from flask import Flask, request, redirect
from twilio import twiml


app = Flask(__name__)

def send_to_slack(from_number, message_body):
    webhook_url = "https://hooks.slack.com/services/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"
    payload = {
        "text": "{}: {}".format(from_number, message_body)
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
    number = request.form['From']
    message_body = request.form['Body']
    send_to_slack(number, message_body)

if __name__ == '__main__':
    app.run()
