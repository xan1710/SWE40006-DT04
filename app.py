from flask import Flask, render_template_string, request
import socket
import os

app = Flask(__name__)

APP_TITLE = os.environ.get("APP_TITLE", "SWE40006 Docker Demo")

INDEX_HTML = """
<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>
    <h1>{{ title }}</h1>
    <form action="/greet" method="post">
        <input type="text" name="name" placeholder="Your name">
        <button type="submit">Greet me</button>
    </form>
</body>
</html>
"""

RESULT_HTML = """
<!DOCTYPE html>
<html>
<head><title>{{ title }}</title></head>
<body>
    <h1>Hello, {{ name }}!</h1>
    <a href="/">Back</a>
</body>
</html>
"""

@app.route("/")
def home():
    return render_template_string(INDEX_HTML, title=APP_TITLE)

@app.route("/greet", methods=["POST"])
def greet():
    name = request.form.get("name", "stranger")
    return render_template_string(RESULT_HTML, title=APP_TITLE, name=name)

@app.route("/health")
def health():
    return {"status": "ok"}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)