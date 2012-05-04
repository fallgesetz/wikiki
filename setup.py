from distutils.core import setup

setup(
    name='Wikiki',,
    version='0.0.1',
    author='Leah Xue',
    author_email='fallgesetz@gmail.com',
    packages=['wikiki'],
    scripts=['bin/wikiki.py'],
    # todo missing some shit
    install_requires=[
        "flask",
        "sqlite3dbm"
        ],
)
