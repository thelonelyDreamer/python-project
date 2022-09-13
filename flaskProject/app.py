from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

@app.route('/{id}')
def hi(id):
    print(id)
    return "hi"


if __name__ == '__main__':
    app.run()
