from types import MethodDescriptorType
from flask import Blueprint, request, jsonify
from pymongo import MongoClient

cart = Blueprint("cart", __name__)

@cart.route('/', methods=['GET', 'POST'])
def manage_cart():
    if request.method == 'GET':
        ordenes_collection = create_mongo_connection()['chatita']['ordenes']
        result = ordenes_collection.find({})
        ordenes = []
        for orden in result:
            #del(orden['_id'])
            orden['_id'] = str(orden['_id'])
            if 'ciudad' in orden.keys():
                del(orden['ciudad'])
            if 'name' in orden.keys() or 'nombre' in orden.keys():
                ordenes.append(orden)
        return jsonify(ordenes)
    if request.method == 'POST':
        if 'authorization' in request.headers:
            if request.data:
                json_data = request.get_json()
                if isinstance(json_data, dict):
                    ordenes_collection = create_mongo_connection()['chatita']['ordenes']
                    result = ordenes_collection.insert_one(json_data)
                    return jsonify({"mensaje": "cart creado"})
                else:
                    return jsonify({"mensaje": "eso no sirve"})
            else:
                return jsonify({"mensaje": "mandame algo"})
        else:
            return jsonify({"mensaje": "no tienes llaves"})


def create_mongo_connection():
    client = MongoClient("mongodb://localhost:27017/")
    return client