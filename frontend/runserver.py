from flask import *
import urllib2

app = Flask(__name__)

@app.route("/")
def index():
	return render_template('home.html')

@app.route('/<path:path>')
def frontend(path):
	return urllib2.urlopen('http://127.0.0.1:5000/' + path).read()

if __name__ == "__main__":
    app.debug = True
    app.run(port=8001)

