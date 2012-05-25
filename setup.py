from distutils.core import setup

setup(
    name='Wikiki',
    version='0.0.1',
    author='Leah Xue',
    author_email='fallgesetz@gmail.com',
    package_dir={'wikiki' : 'src/wikiki'},
    packages=['wikiki'],
    scripts=['bin/wikiki.py'], 
    package_data={'wikiki':['BUGS', 'DESIGN', 'README']},
    # todo missing some shit
    install_requires=[
        "flask",
        "sqlite3dbm",
        "python-magic",
        ],
)
