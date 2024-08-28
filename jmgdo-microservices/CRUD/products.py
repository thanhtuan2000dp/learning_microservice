from flask import Flask, jsonify, request
import json
from flask_cors import CORS

app = Flask("Product Server")
CORS(app)


products = [
    {'id': 143, 'name': 'Notebook', 'price': 5.49},
    {'id': 144, 'name': 'Black Marker', 'price': 1.99}
]

#
# Add all the REST API end-points here
#


@app.route('/products')
def get_products():
    return jsonify(products)


@app.route('/products', methods=['POST'])
def add_product():
    product = request.get_json()
    products.append(product)
    return product, 201


@app.route('/products/<int:id>')
def get_product_by_id(id):
    product = [x for x in products if x.get('id') == id][0]
    return jsonify(product)


@app.route('/products/<int:id>', methods=['PUT'])
def update_product(id):
    updated_product = json.loads(request.data)
    product = [x for x in products if x.get('id') == id][0]
    for key, value in updated_product.items():
        product[key] = value
    return updated_product, 204


@app.route('/products/<int:id>', methods=['DELETE'])
def delete_product(id):
    deleted_product = [x for x in products if x.get('id') == id][0]
    products.remove(deleted_product)
    return deleted_product, 204


app.run(port=5000, debug=True)
