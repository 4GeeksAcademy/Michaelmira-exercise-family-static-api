
"""
update this file to implement the following already declared methods:
- add_member: Should add a member to the self._members list
- delete_member: Should delete a member from the self._members list
- update_member: Should update a member from the self._members list
- get_member: Should return a member from the self._members list
"""
from random import randint
from pprint import pprint

initial_members = [{ 
        "id": 22,
        "name": "John",
        "age": 33,
        "lucky_numbers": [7, 13, 22]
    },{
        "id": 33,
        "name": "Jane",
        "age": 35,
        "lucky_numbers": [7, 13, 22]
    },{
        "id": 33,
        "name": "Jimmy",
        "age": 5,
        "lucky_numbers": [1]
    }
]

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name

        #list of members
        self._members = initial_members

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
    
    def get_member_id(self, placement):
        if 1 <= placement <= len(initial_members):
            print(self._members[placement - 1]["id"])
            return self._members[placement - 1]["id"]
        else:
            print("was not able to return a memeber id by placement")
            return None

    def add_member(self, member):
        member["id"] = self._generateId()
        self._members.append(member)

    def delete_member(self, id):
        # fill this method and update the return
        #TODO -fill this in
        pass

    def get_member(self, id):
        response_body = jackson_family.get_all_members()
        return jsonify(response_body), 200

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members


if __name__ == "__main__":
    family = FamilyStructure("Jackson")
    family._members = initial_members
    new_guy = {
        "name""name": "Rob" ,
        "age": 36 ,
        "lucky_numbers": [9,10,11]
    }
    family.add_member(new_guy)
    family.get_member
    pprint(initial_members)
    print("\n")
    family.get_member_id(1)

