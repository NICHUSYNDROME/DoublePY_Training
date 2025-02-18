import json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='PinyinTable')

@app.route('/')
def index():
    return render_template('HanYuPinYin.html')

@app.route('/<path:path>')
def serve_static(path):
    if path.startswith('assets/'):
        return send_from_directory('.', path)
    return send_from_directory('PinyinTable', path)

import webbrowser

if __name__ == '__main__':
    webbrowser.open("http://127.0.0.1:5000")
    app.run(debug=False)
