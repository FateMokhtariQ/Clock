from flask import Flask, render_template
from datetime import datetime

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('clock.html', time=datetime.now().strftime('%H:%M:%S'))

if __name__ == '__main__':
    app.run(debug=True)
