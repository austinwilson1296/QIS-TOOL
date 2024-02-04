from flask import Flask, render_template, request, redirect, url_for


app = Flask(__name__)

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/create-repair-job')
def create_repair():
  return render_template('create_repair.html')
if __name__ == '__main__':
  app.run(host='0.0.0.0', port=8080)
    