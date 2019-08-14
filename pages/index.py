from flask import Flask, render_template, request, url_for
from blueprints.base import base


app = Flask(__name__, template_folder='templates')
app.register_blueprint(base)


@app.route('/test')
def index():
    return render_template('base_home.html')


def main():
    app.env = 'development'
    app.secret_key = 'A chave secreta e: batata'
    app.run(debug=True, port=8000)

if __name__ == "__main__":
    main()