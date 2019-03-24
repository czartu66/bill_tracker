###############################################################
# I've taken this code from here: http://flask.pocoo.org/docs/0.12/quickstart/#a-minimal-application
###############################################################
# app.py #
###############################################################

from flask import Flask, render_template
from database import db_users
from api_call import ApiCall

app = Flask(__name__)


@app.route('/')
def main():
    return render_template('index.html')

@app.route('/id/<person_id>')
def api_id(person_id):
    users_parser = ApiCall(db_users, person_id)
    return users_parser.call(db_users, person_id)

if __name__ == '__main__':
    app.run()