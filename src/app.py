import logging; logger=logging.getLogger(__name__)
import flask
import sqlite
import os
DEBUG=True
app = flask.Flask(__name__)
app.config.from_object(__name__)

def get_db():
    store = sqlite.open("store.sqlite3")
    logger.debug("Opening store.sqlite3")
    return store

####
# Routing Functions
####
@app.route('/')
def main():
    pass

@app.route('/wiki/<page>')
def wiki(page):
    store = get_db()
    if not page in store:
        flask.abort(404)
    else:
        return flask.render_template_string(store[page])

if __name__ == "__main__":
    app.run()
