"""
This module takes care of starting the API Server, Loading the DB and Adding the endpoints
"""
import os
from flask import Flask, request, jsonify, url_for
from flask_cors import CORS
from utils import APIException, generate_sitemap
from datastructures import FamilyStructure
#from models import Person

app = Flask(__name__)
app.url_map.strict_slashes = False
CORS(app)

# create the jackson family object
jackson_family = FamilyStructure("Jackson")

# Handle/serialize errors like a JSON object
@app.errorhandler(APIException)
def handle_invalid_usage(error):
    return jsonify(error.to_dict()), error.status_code

# generate sitemap with all your endpoints
@app.route('/')
def sitemap():
    return generate_sitemap(app)

@app.route('/member', methods=['GET'])
def handle_get_22_id():

    # this is how you can use the datastructure by calling its methods
    member = jackson_family.get_member(22)
    response_body = member
    return jsonify(response_body), 200

@app.route('/members', methods=['GET'])
def handle_get():

    # this is how you can use the datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = members
    return jsonify(response_body), 200

@app.route('/member', methods=['POST'])
def handle_add():
    member = request.json

    # this is how you can use the Family datastructure by calling its methods
    jackson_family.add_member(member)
    return member

# @app.route('/members', methods=['POST'])
# def create_member():
#     member_data = request.json
#     jackson_family.add_member(member_data)
#     return {}, 200

# @app.route('/members', methods=['POST'])
# def add_member(member_id):
    
#     if not request.get_json()["id"]:
#        id = None

#     else:
#         id = request.get_json()["id"]

#         first_name = request.get_json()["first_name"]
#         if not first_name:
#             return jsonify({"error", "first name is required" }), 400
        
#         age = request.get_json()["age"]
#         if not age:
#             return jsonify({"error", "age is required" }), 400
        
#         lucky_numbers = request.get_json()["lucky_numbers"]
#         if not lucky_numbers:
#             return jsonify({"error", "lucky numbers is required" }), 400
        
#         member = {"id": id, "first_name": first_name, "age": age, "lucky_numbers": lucky_numbers}
#         jackson_family.add_member(member)

#         response_body = {
#             "member": member,
#             "msg": f"New member added to {jackson_family.last_name}"
#         }

#         return jsonify(response_body), 200
       


# @app.route('/members', methods=['GET'])
# def handle_get_member():

#     # this is how you can use the datastructure by calling its methods
#    member_id = request.args.get('id')
#    print(f"trying to get member id {member_id}")
# #    member = jackson_family.get_member(member_id)
#    return member_id

# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)
    
