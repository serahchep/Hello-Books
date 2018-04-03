from flask import Flask, render_template, url_for

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'hello world!'

if __name__ == '__main__':
    app.run(debug=True) 