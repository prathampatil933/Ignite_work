from flask import Flask, render_template, request, jsonify, make_response, send_from_directory
import os

app = Flask(__name__)

app.config['UPLOAD_FOLDER'] = 'static'

@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, max-age=0'
    return response


@app.route('/hello', methods=['GET'])
def hello():
    language = request.args.get('language', '').capitalize()

    messages = {
        "French": "Bonjour le monde",
        "English": "Hello world",
        "Hindi": "Namastey sansar"
    }

    if language in messages:
        response = {
            "ID": "Pratham_Patil_01020200198",
            "msgText": messages[language]
        }
        return jsonify(response), 200
    else:
        error_response = {
            "error_message": "The requested language is not supported"
        }
        return jsonify(error_response), 400


@app.route('/static/<path:filename>')
def serve_static(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)


if __name__ == '__main__':
    app.run(host='localhost', port=5000)
