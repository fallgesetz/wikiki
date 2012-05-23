"""
sqlite3dbm.sshelve modified to work with Flask...
"""
import sqlite3dbm
import flask


def open(filename):
    # _app_ctx_stack for >>0.9 but uh, can't install that apparently
    ctx = flask._request_ctx_stack.top
    sqlite_name = 'sqlite_%s' % filename
    if hasattr(ctx, sqlite_name ):
        db = getattr(ctx, sqlite_name)
    else:
        db = sqlite3dbm.sshelve.open(filename)
        setattr(ctx, sqlite_name, db)
    return db


