from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return 'Hello, world! This is my Flask web app.'

if __name__ == '__main__':
    app.run(debug=True)
