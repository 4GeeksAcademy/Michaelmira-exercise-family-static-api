
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
        "id": 3433,
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
        
# Method GET /member/<int:id> should exist

    def add_member(self, member):
        member["id"] = self._generateId()
        self._members.append(member)
        

    def delete_member(self, id):
        # fill this method and update the return
        #TODO -fill this in
        pass

    def get_member(self, member_id):
        for member in self._members:
            if member["id"] == member_id:
                return member
        return None

    # this method is done, it returns a list with all the family members
    def get_all_members(self):
        return self._members

if __name__ == "__main__":
    family = FamilyStructure("Jackson")
    family._members = initial_members
    # family.add_member(new_guy)
    pprint(initial_members)