import datetime
from modules.execute import execute_notebook
import asyncio
from flask import Flask
from flask_restful import Api, request
import nbconvert
from insert import \
    insert_to_db, \
    read_from_db, \
    update_file_in_db, \
    read_from_db_by_id, \
    delete_from_db
from flask_cors import CORS, cross_origin
# from healthcheck import HealthCheck

app = Flask('api')
cors = CORS(app, resource={
    r"/*": {
        "origins": "*"
    }
})
# health = HealthCheck(api)


async def func1(file_path):
    nb = await execute_notebook(input_path=file_path, output_path='', kernel_name='python')
    return nb


@cross_origin()
@app.route('/get_notebook_html')
def get():
    html_exporter = nbconvert.HTMLExporter()
    file_path = request.args.get('file_path')
    nb = asyncio.run(func1(file_path))
    body, _ = html_exporter.from_notebook_node(nb, resources={})
    return body, 200


@cross_origin()
@app.route('/add_notebook', methods=["POST"])
def post():
    file = request.files['file']
    file_name = file.filename.split('.')[0]

    if read_from_db(file_name):
        return 'file_already_exists', 422

    file_path = '/notebooks/' + file.filename
    created_date = datetime.datetime.now()
    updated_time = datetime.datetime.now()
    insert_to_db(file_name, file_path, created_date, updated_time)
    return f'file - \'{file_name}\' written to database', 200


@cross_origin()
@app.route('/update_notebook', methods=["PUT"])
def put():
    file = request.files['file']
    file_name = file.filename.split('.')[0]
    file_from_db = read_from_db(file_name)
    if file_from_db:
        update_time = datetime.datetime.now()
        result = update_file_in_db(file_from_db, update_time, file_name)
        if result:
            return f'file - \'{file_name}\' updated', 200
        else:
            return 'There is some problems', 422
    return f'There is no \'{file_name}\' in database', 422


@cross_origin()
@app.route('/delete_notebook', methods=["DELETE"])
def delete():
    file_id = request.args.get('file_id')
    file_from_db = read_from_db_by_id(file_id)
    if file_from_db:
        result = delete_from_db(file_id)
        if result:
            return f"file {file_id} was deleted"
    return f"file {file_id} not exist", 200


@cross_origin()
@app.route('/healthcheck')
def get_health():
    result = request.headers
    # health_check = health.run()
    # return health_check[0], 200
    return result.get('Host'), 200


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)



