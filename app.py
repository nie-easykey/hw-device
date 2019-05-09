from flask import Flask, render_template, request
app = Flask(__name__)

rfid = "3000"

@app.route('/')
def hello_world():
    return render_template("index.html")

@app.route("/rfid", methods=["GET","POST"])
def rfid_handler():
    global rfid
    if request.method == "GET":
        return rfid
    elif request.method == "POST":
        rfid = str(request.get_json()["id"])
    return "OK"


app.run(host="0.0.0.0",port=5000, debug=True)
