import os
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == "__main__":
    # Use the port Render provides, default to 5000 if not set
    port = int(os.environ.get("PORT", 5000))
    # Listen on all interfaces, not just localhost
    app.run(host="0.0.0.0", port=port)
