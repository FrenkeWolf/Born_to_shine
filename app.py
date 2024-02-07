from flask import Flask

app = Flask(__name__)


@app.route('/')
@app.route('/index')
def index():
    return "<p>Born to shine</p>"


@app.route('/about')
def about():
    return "<p>о нас</p>"

#bmgtl;m;lngm


if __name__ == '__main__':
    app.run(debug=True)
