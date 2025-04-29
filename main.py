from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/', methods=['POST'])
def slack_event():
    data = request.get_json()
    # Slack의 URL 검증용 challenge 응답
    if 'challenge' in data:
        return jsonify({'challenge': data['challenge']})

    # 이후 Slack 메시지 이벤트도 여기서 처리할 수 있음
    return '', 200

@app.route('/', methods=['GET'])
def health():
    return 'OK', 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=8080)
