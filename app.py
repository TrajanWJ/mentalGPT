from flask import Flask, render_template, request, url_for, redirect
import re
import random
import back
import datetime
import openai
from back import Chat

conversation = Chat()

app = Flask(__name__, template_folder='templates', static_folder='static')

@app.route('/')
def menu():
    return render_template('chat.html')

@app.route('/chat', methods=['GET'])
def chat():
    chat_name = request.args.get('name') 
    return render_template('chat.html', chat_name=chat_name)

@app.route('/get_bot_response', methods=['POST'])
def get_bot_response():
    user_message = request.form['user_input']
    bot_response = conversation.generate_message(user_message)
    return bot_response

@app.route('/get_hotlines', methods=['POST'])
def get_hotlines():
    return conversation.get_hotlines()

@app.route('/reload')
def reload():
    return redirect(url_for('index'))


if __name__ == '__main__':
    app.run(debug=True)
      
