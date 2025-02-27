from flask import Flask

app = Flask(__name__)

@app.route("/")
def index():
    return "hello world from railway"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3002, debug=True)