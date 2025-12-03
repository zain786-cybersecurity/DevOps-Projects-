from flask import Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "Hello from my own DevOps CI/CD Project so excited to share it with you!"

if __name__ == "__main__":
    app.run()
