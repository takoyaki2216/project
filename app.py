from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = 'fire_alarm'

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        mode = request.args.get('hub.mode')

        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Verification failed', 403

    elif request.method == 'POST':
        data = request.get_json()
        print("Incoming POST data:", data)

        # Extract PSID
        try:
            sender_id = data['entry'][0]['messaging'][0]['sender']['id']
            print("Sender PSID:", sender_id)
        except Exception as e:
            print("Error extracting PSID:", e)

        return 'EVENT_RECEIVED', 200
