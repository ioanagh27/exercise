from flask import Flask, request, jsonify
from flask_cors import CORS
from werkzeug import exceptions
from controllers import data

# for i in users:
#     print(jsonify(i))

app = Flask(__name__)
CORS(app)

@app.route('/')
def welcome():
    return 'Welcome to my flower shop'

@app.route('/flowers', methods = ['GET', 'POST'])
def flowers():
    fns = {
        'GET': data.index,
        'POST': data.create
    }
    resp, code = fns[request.method](request)
    return jsonify(resp), code

@app.route('/flowers/<int:flower_id>', methods = ['GET', 'PUT', 'DELETE'])
def flower_handler(flower_id):
    fns = {
        'GET': data.show,
        'PUT': data.update,
        'DELETE': data.destroy
    }
    resp, code = fns[request.method](request, flower_id)
    return jsonify(resp, code)

@app.errorhandler(exceptions.NotFound)
def handle_404(err):
    return jsonify({'message': f"Oops...{err}"}), 404

@app.errorhandler(exceptions.InternalServerError)
def handle_500(err):
    return jsonify({'message': f"It`s not you, it`s us"}), 500

if __name__ == '__main__':
    app.run(debug = True)