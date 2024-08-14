from flask import Flask, request, jsonify, render_template

from utils import get_response, predict_class

app = Flask(__name__, template_folder='static')


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/handle_message', methods=['POST'])
def handle_message():
    message = request.json['message']
    intents_list = predict_class(message)  # No need to pass additional parameters
    response = get_response(intents_list)  # No need to pass additional parameters

    return jsonify({'response': response})


# curl -X POST http://127.0.0.1:5000/handle_message -d '{"message":"what is coding"}' -H "Content-Type: application/json"


if __name__ == '__main__':
    app.run(debug=False,host='0.0.0.0')
