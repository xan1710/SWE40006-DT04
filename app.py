from sys import version
from flask import Flask, jsontify

app = Flask(__name__)

@app.route("/")
def home():
    return """
    <!DOCTYPE html>
    <html>
    <head>
        <title>SWE40006 Docker App</title>
    </head>
    <body>
        <h1>SWE40006 Docker Deployment</h1>
        <p>Task 4.2 Credit Level</p>
        <p>This application is running inside a Docker container.</p>
    </body>
    </html>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)