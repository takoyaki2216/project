from flask import Flask, request

app = Flask(__name__)

# Make SURE this token is EXACTLY what you enter in Facebook Developer Console
VERIFY_TOKEN = 'fire_alarm'  # <- Set this to a known string

@app.route('/', methods=['GET', 'POST'])
def webhook():
    if request.method == 'GET':
        mode = request.args.get('hub.mode')
        token = request.args.get('hub.verify_token')
        challenge = request.args.get('hub.challenge')

        # Correct verification logic
        if mode == 'subscribe' and token == VERIFY_TOKEN:
            return challenge, 200
        else:
            return 'Verification failed. Tokens do not match.', 403

    elif request.method == 'POST':
        print(request.json)
        return 'EVENT_RECEIVED', 200

    return 'Not a valid request', 404

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
