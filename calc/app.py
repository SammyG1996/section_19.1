# Put your app in here.
from flask import Flask, request

app = Flask(__name__)

@app.route('/add')
def add():
  total = int(request.args['a']) + int(request.args['b'])
  return str(total)

@app.route('/sub')
def sub():
  total = int(request.args['a']) - int(request.args['b'])
  return str(total)

@app.route('/mult')
def mult():
  total = int(request.args['a']) * int(request.args['b'])
  return str(total)

@app.route('/div')
def div():
  total = int(request.args['a']) / int(request.args['b'])
  return str(total)