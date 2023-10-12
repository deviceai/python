from flask import Flask, session
app = Flask(__name__)
app.secret_key = '1234567890'
app.config['SESSION_TYPE'] = 'filesystem'

@app.route('/')
def home():
    x = session.get('x', None)
    if not x:
        session['x'] = 1
    elif x>=10:
        session.clear()
        return "Session cleared"
    else:
        session['x'] += 1
    return str(session['x'])

@app.route('/<int:x>')
def count(x):
    s = session.get('sum', None)
    if not s:
        session['sum'] = x
    else:
        session['sum']+=x
    return str(session['sum'])

if __name__ == '__main__':
    app.run(host='0.0.0.0')