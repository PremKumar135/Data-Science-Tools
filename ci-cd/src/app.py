from flask import Flask

app =Flask(__name__)

@app.route('/')
def index():
    msg = "Hello, world! This is Prem Kumar"
    return msg

if __name__ == '__main__':
    app.run()
