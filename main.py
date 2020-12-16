from flask import request, jsonify
from ariadne import graphql_sync
from ariadne.constants import PLAYGROUND_HTML

from api import app
from schema import schema

from init_db import populate

populate()


@app.route("/graphql", methods=["GET"])
def graphql_playground():
    return PLAYGROUND_HTML, 200


@app.route("/graphql", methods=["POST"])
def graphql_server():
    data = request.get_json()
    print(data)
    success, result = graphql_sync(schema, data, context_value=request, debug=app.debug)

    status_code = 200 if success else 400
    return jsonify(result), status_code
