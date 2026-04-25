from flask import Flask
import subprocess

app = Flask(__name)

@app.route("/trigger-audit", methods=["POST"])
def run():
    print(">>> Signal Received.")
    subprocess.run(["python", "sentry_node.py"])
    return {"status": "Audit Triggered"}, 200

if name == "__main__":
    app.run(host="0.0.0.0", port=5000)
