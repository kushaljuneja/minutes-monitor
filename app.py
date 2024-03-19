from flask import Flask, jsonify, render_template
import sqlite3

app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/get_tasks')
def get_data():
    # connect to sqlite db
    conn = sqlite3.connect("database.sqlite3")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()

    cur.execute("select * from RECORD_TB")

    rows = cur.fetchall()

    data = [dict(row) for row in rows]

    conn.close()

    return jsonify({'data': data})


if __name__ == '__main__':
    app.run(host='100.90.40.115', port=5000, debug=True)