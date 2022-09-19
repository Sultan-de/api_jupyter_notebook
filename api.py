from flask import Flask
from flask_restful import Api, Resource, reqparse
import random
app = Flask('api')
api = Api(app)



@app.route('/get_notebook_html')
def get():

    return 'Success', 200

@app.route('/add_notebook')
def post():
    parser = reqparse.RequestParser()
    params = parser.parse_args()

    return params, 201

@app.route('/update_notebook')
def put():
    parser = reqparse.RequestParser()
    params = parser.parse_args()

    return params, 201

@app.route('/delete_notebook')
def delete():

    return f"Quote with id is deleted.", 200


if __name__ == '__main__':
    app.run(debug=True)