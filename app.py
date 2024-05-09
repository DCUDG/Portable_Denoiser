from flask import Flask
from views import homepage

app = Flask(__name__)
app.register_blueprint(homepage, url_prefix="/")

if __name__ == '__main__':
    app.run(debug=True, port=8000)