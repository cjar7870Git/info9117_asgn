from flask import Flask, request

app = Flask(__name__)
host="localhost"
port="5000"
address="http://{0}:{1}".format(host,port)


def serve_forever():
    app.run(host, port)

def shutdown_server():
    func = request.environ.get('werkzeug.server.shutdown')
    if func is None:
        raise RuntimeError("Not running with Werkzeug server")
    func()

@app.route('/shutdown')
def shutdown():
    shutdown_server()

@app.route('/')
def hello():
    return 'Hello World'

if __name__ == '__main__':
    serve_forever()