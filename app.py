import os
import json

import openai
from flask import Flask, redirect, render_template, request, url_for,jsonify

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")


@app.route("/chat", methods=("GET", "POST"))
def index():
    prompt = request.args.get('prompt')
    qId = request.args.get('QId')
    print(prompt)
    if request.method == "POST":
        response = openai.Completion.create(
            model="text-davinci-003",
            prompt="how are you",
              temperature=0.3,
              max_tokens=30,
              top_p=1.0,
              frequency_penalty=0.5,
              presence_penalty=0.2
        )
        print(response.choices[0].text)
        return jsonify({'response': response.choices[0].text,
                    'QId': qId})

@app.route('/hello/', methods=['GET', 'POST'])
def welcome():
    return "Hello World!"

if __name__ == '__main__':
    app.debug = True
    app.run(host='0.0.0.0', port=80)
