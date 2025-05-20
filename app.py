from flask import Flask, request

app = Flask(__name__)

VERIFY_TOKEN = 'your_verify_token_here'

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        # Facebook Webhook Verification
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')
        if token == VERIFY_TOKEN:
            return challenge
        return 'Verification token mismatch', 403
    elif request.method == 'POST':
        # Handle incoming messages (optional)
        print(request.json)
        return 'OK', 200

if __name__ == '__main__':
    app.run()
