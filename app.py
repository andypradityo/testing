from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, Flask! [version 2]"

if __name__ == "__main__":
    # Please do not set debug=True in production
    app.run(host="0.0.0.0", port=5000, debug=True)