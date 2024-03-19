
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
        "first_name": "John",
        "age": 33,
        "lucky_numbers": [7, 13, 22]
    },{
        "first_name": "Jane",
        "age": 35,
        "lucky_numbers": [10, 14, 3]
    },{
        "first_name": "Jimmy",
        "age": 5,
        "lucky_numbers": [1]
    }
]

class FamilyStructure:
    def __init__(self, last_name):
        self.last_name = last_name
        self._members = []

        for member in initial_members:
            member_with_id = {
                "id": self._generateId(),
                "first_name": member["first_name"],
                "last_name": last_name,
                "age": member["age"],
                "lucky_numbers": member["lucky_numbers"],
            }
            self._members.append(member_with_id)

        print("added members")
        pprint(self._members)
        

    # read-only: Use this method to generate random members ID's when adding members into the list
    def _generateId(self):
        return randint(0, 99999999)
        
# Method GET /member/<int:id> should exist

    def add_member(self, member):

        # member looks like:
        # {
        #     "first_name": "Michael",
        #     "age": 25,
        #     "lucky_numbers": [10,20]
        # }

        # need to add:
        # {
        #     "first_name": "Michael",
        #     "last_name": "jackson",
        #     "age": 25,
        #     "lucky_numbers": [10,20]
        #     "id": 120931
        # }

        #TODO - add id maybe

        member_with_id = {
            "first_name": member["first_name"],
            "last_name": self.last_name,
            "age": member["age"],
            "lucky_numbers": member["lucky_numbers"],
        }

        if "id" in member and isinstance(member["id"], int):
            member_with_id["id"] = member["id"]
        else:
            member_with_id["id"] = self._generateId()

        self._members.append(member_with_id)

    def delete_member(self, id):
        for member_idx, member in enumerate(self._members):
            if member["id"] == id:
                del self._members[member_idx]
                return id
        return None
    
    def get_member(self, id):
        #print(f"get member called with id {id}")
        #pprint(self._members)
        for member in self._members:
            if member["id"] == id:
                #print("member found")
                #pprint(member)
                return member
        #print("member not found")
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

if __name__ == "__main__":
    family = FamilyStructure("Jackson")
    family._members = initial_members
    # family.add_member(new_guy)
    pprint(initial_members)