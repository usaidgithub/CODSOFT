import random
from flask import Flask, render_template, request, jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)

password = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz123456790@#$%&*"

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit_query', methods=['POST'])
@cross_origin()
def submit_query():
    length = int(request.form.get('guess'))
    generated_password = ''.join(random.choice(password) for _ in range(length))
    return jsonify({'message': generated_password})

@app.route('/reset_game', methods=['GET'])
@cross_origin()
def reset_game():
    return jsonify({'message': 'Game reset successfully'})

if __name__ == '__main__':
    app.run(debug=True, port=3000)
