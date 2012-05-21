# external imports
import logging; logger=logging.getLogger(__name__)
import os
# external/not std imports
import flask
import creole
# package imports
import sqlite
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

@app.route('/<page>')
def wiki(page):
    store = get_db()
    if not page in store:
        flask.abort(404)
    else:
        text = store[page].decode()
        morphed_text = creole.creole2html(text)
        return flask.render_template("entry.html", key=page, value=morphed_text)

if __name__ == "__main__":
    app.run()
