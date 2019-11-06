from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/debug/<var>')
def debug_flask(var):
    x = 42 / int(var)
    return 'x is {}'.format(x)

if __name__ == '__main__':
    app.run(debug=True)
