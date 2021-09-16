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

@app.route('/members', methods=['GET'])
def get_family_members():

    # this is how you can use the Family datastructure by calling its methods
    members = jackson_family.get_all_members()
    response_body = members
    


    return jsonify(response_body), 200

@app.route('/member/<int:id>', methods=['GET'])
def get_member(id):

    # this is how you can use the Family datastructure by calling its methods
    member = jackson_family.get_member(id)
    response_body = {
        "member": member
    }

    if member is not None:
        return jsonify(response_body), 200
    else:
        return "Member Not FOUND", 400

# ### 3) Add (POST) new member

# Which adds a new member to the family data structure.

# ```md
# POST /member

# REQUEST BODY (content_type: application/json):

# {
#     first_name: String,
#     age: Int,
#     lucky_numbers: [],
#     id: Int *optional
# }

# RESPONSE (content_type: application/json):

# status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

# body: empty
# ```

# Keep in mind that POST request data dictionary may contain a key and a value for this new member `id`.
# - If it does not, your API should randomly generate one when adding as a family members.
# - If it does include it, then that is the value to be used for such end.


 
        
# this only runs if `$ python src/app.py` is executed
if __name__ == '__main__':
    PORT = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=PORT, debug=True)



# @
# @
# @


# ### 2) Retrieve one member

# Which returns the member of the family where `id == member_id`.

# ```md
# GET /member/<int:member_id>

# RESPONSE (content_type: application/json):

# status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

# body: //the member's json object

# {
#     "id": Int,
#     "first_name": String,
#     "age": Int,
#     "lucky_numbers": List
# }

# ```

# ### 3) Add (POST) new member

# Which adds a new member to the family data structure.

# ```md
# POST /member

# REQUEST BODY (content_type: application/json):

# {
#     first_name: String,
#     age: Int,
#     lucky_numbers: [],
#     id: Int *optional
# }

# RESPONSE (content_type: application/json):

# status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

# body: empty
# ```

# Keep in mind that POST request data dictionary may contain a key and a value for this new member `id`.
# - If it does not, your API should randomly generate one when adding as a family members.
# - If it does include it, then that is the value to be used for such end.

# ### 4) DELETE one member

# Which deletes a family member with `id == member_id`

# ```md
# DELETE /member/<int:member_id>

# RESPONSE (content_type: application/json):

# status_code: 200 if success. 400 if bad request (wrong info) screw up, 500 if the server encounter an error

# body: {
#     done: True
# }    

# ```