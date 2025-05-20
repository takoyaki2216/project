from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = 'fire_alarm'  # Use the exact same token in Facebook setup

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Facebook is trying to verify your webhook
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        if token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Invalid verification token', 403

    elif request.method == 'POST':
        # Facebook will send a POST request with messages here
        print(request.json)
        return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
