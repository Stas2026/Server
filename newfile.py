from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return "Привіт з Flask сервера!"

@app.route('/get_data', methods=['GET'])
def get_data():
    return "Це просто текстова відповідь від сервера!"

@app.route('/post_data', methods=['POST'])
def post_data():
    return "Дані отримано на сервері!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)