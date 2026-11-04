from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <h1>Welcome to DevOps CI/CD Pipeline!</h1>
    <p>Application deployed successfully using Jenkins and Docker.</p>
    """

@app.route("/health")
def health():
    return jsonify({
        "status": "success",
        "message": "Application is running"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
