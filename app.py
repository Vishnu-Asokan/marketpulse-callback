
from flask import Flask, request

app = Flask(__name__)

@app.route("/", methods=["GET"])
def home():
    return "MarketPulse callback service is running."

@app.route("/callback", methods=["GET"])
def callback():
    # Do not log or display authentication tokens.
    if request.args.get("error"):
        return "Authentication was not completed. Return to MarketPulse.", 400

    if request.args.get("code"):
        return (
            "Authorization response received. "
            "Return to MarketPulse on your own computer."
        )

    return "Callback endpoint is ready."

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
