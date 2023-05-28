from flask import Flask, send_file
app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/<file_name>", methods=["GET"])
def get_file(file_name):
    if len(file_name) > 0:
        return send_file(f"./{file_name}", attachment_filename=file_name)
    return "file not found."

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=80)
