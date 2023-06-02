from flask import Flask, send_file
app = Flask(__name__)

def gpt_query(str_q):
    from EdgeGPT import Query, Cookie
    q = Query(str_q,style="creative",cookies="./cookies.zip")
    return q.sources


@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route("/gpt/<str_q>", methods=["GET"])
def get_gpt(str_q):
    if len(str_q) > 0:
        return gpt_query(str_q.replace("_"," "))
    return "question not found."

@app.route("/f/<file_name>", methods=["GET"])
def get_file(file_name):
    if len(file_name) > 0:
        return send_file(f"./{file_name}")
    return "file not found."

if __name__ == '__main__':
    app.run(host="0.0.0.0",port=8080) #host="0.0.0.0",port=8080
