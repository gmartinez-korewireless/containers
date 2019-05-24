from flask import Flask
import os
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def index():
    name = os.getenv('NAME', 'World')
    return 'Hi %s!, today is <b>%s</b>' % (name, datetime.today().strftime("%A %d, %B %Y"))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)