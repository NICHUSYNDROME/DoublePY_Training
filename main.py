import json
from flask import Flask, render_template, send_from_directory

app = Flask(__name__, template_folder='PinyinTable')

@app.route('/')
def index():
    return render_template('HanYuPinYin.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('PinyinTable', filename)

if __name__ == '__main__':
    app.run(debug=True)
