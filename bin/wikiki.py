#!/usr/bin/env python
import argparse
import sys
import inspect
import os
import sqlite3dbm
import tempfile
import subprocess

def _current_path():
    return os.path.dirname(inspect.getfile(inspect.currentframe()))

store = "%s/../store.sqlite3" % _current_path()
store_db = sqlite3dbm.sshelve.open(store)

def dash_modify(topic, content):
    """
    makes a new topic
    """
    store_db[topic] = content

def dash_append(topic, content):
    """
    appends to an existing topic (creates new topic if existing topic doesn't exist).

    Default option
    """
    if not topic in store_db:
        store_db[topic] = ""
    store_db[topic] += content

def main():
    parser = argparse.ArgumentParser("Command line wiki access")
    # creation behavior
    group = parser.add_mutually_exclusive_group()
    group.add_argument('-m', '--modify', help = "Make/Override a new topic", action="store_true")
    group.add_argument('-a', '--append',
        help = "Append to an existing topic, or creates a new topic if the existing topic doesn't exist",
        action = "store_true")
    group.add_argument('-e','--editor', action="store_true", help="open key in text editor")
    parser.add_argument("key")
    parser.add_argument("value", nargs="?", help="Optional in editor mode")

    results = parser.parse_args()
    if results.editor:
        handle, path = tempfile.mkstemp()
        print store_db
        with open(path, 'w') as f:
            f.write(store_db.get(results.key))
        subprocess.check_call(['vim', path])
        with open(path, 'r') as f:
            contents = f.read()
            dash_modify(results.key, contents)
    elif results.append:
        dash_append(results.key, results.value)
    elif results.modify:
        dash_modify(results.key, results.value)
    else:
        pass

if __name__ == '__main__':
    main()
