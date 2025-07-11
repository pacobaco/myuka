# app.py
from flask import Flask, render_template_string
from content_generator import generate_content

app = Flask(__name__)

@app.route("/")
def index():
    html = generate_content()
    return render_template_string(html)

if __name__ == "__main__":
    app.run(host="127.0.0.1", port=8080)