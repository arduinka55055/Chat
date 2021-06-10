from flask import Flask, render_template, request, redirect, url_for
from flask.globals import session, session
from flask_socketio import SocketIO, join_room, leave_room, emit
from flask_session import Session
import json
from router import Router
PIDOR=Router()

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'FUCKYOU'
app.config['SESSION_TYPE'] = 'filesystem'

Session(app)

app.config.update(SESSION_COOKIE_SAMESITE="None", SESSION_COOKIE_SECURE=True)
socketio = SocketIO(app, manage_session=False)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('index.html')


@app.route('/chat', methods=['GET', 'POST'])
def chat_between_users():
    if (request.method == 'POST'):
       username = request.form['username']  
       room = request.form['room']

       session['username'] = username    
       session['room'] = room
       return render_template('chat.html', session = session)
    else:
        if (session.get('username') is not None):
            return render_template('chat.html', session = session)
        else:
            return redirect(url_for('index'))


@socketio.on('join', namespace='/chat')
def join_to_the_chat(message):
    room = session.get('room')
    join_room(room)
    
    emit('status', PIDOR.hello(session.get('username')), room=room)
    #return json.dumps({'msg': session.get('username')}), ' Только что присоденился к чату!'


@socketio.on('text', namespace="/chat")   
def text(message):
    room = session.get('room') 
    print(session.get('username'))
    PIDOR.request(message['msg'],session.get('username'))
    emit('message', PIDOR.response(), room=room)   
    #return json.dumps


@socketio.on('left', namespace='/chat')
def left(message):
    room = session.get('room')
    username = session.get('username')
    leave_room(room)
    #session.clear('')
    
    emit('status', PIDOR.bye(session.get('username')), room=room)



if __name__ == '__main__':
    socketio.run(app)  