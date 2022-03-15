from flask import Flask

app = Flask(__name__)

@app.route("/server.java")
def server():
    return open("server.java").read()
 
app.run()
