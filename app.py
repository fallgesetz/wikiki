import flask
import sqlite3dbm

app = flask.Flask(__name__)
app.config.from_object(__name__)


@app.route('/')
def main():
    pass

@app.route('wiki/<page>')
def wiki(page):
    pass

if __name__ == "__main__":
    app.run()
