from flask import Flask
import os
from datetime import datetime
from database import Database

app = Flask(__name__)

@app.route('/')
def index():
    db = Database()
    name = os.getenv('NAME', 'World')
    result = db.fetchone("SELECT @@version AS Version, GETUTCDATE() CurrentDate")
    db.close()
    return 'Hi %s!, <p><b>Current date:</b> %s</p><p><b>Catabse version:</b> %s</p>' % (name, result.get('Version', "n/a"), result.get('CurrentDate', 'n/a'))

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=80)