from flask import Flask, jsonify, request
import scraping

app = Flask(__name__)


@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(scraping.amazing_title)


@app.route('/data', methods=['POST'])
def receive_data():
    data = request.get_json()
    return jsonify(data)


if __name__ == '__main__':
    app.run(debug=True)
