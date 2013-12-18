__author__ = 'b543840'

class Node():

    def __init__(self, number, direct_rel, indirect_rel):
        self.number = number
        self.direct_rel = direct_rel
        self.indirect_rel = indirect_rel
        self.visited_as = 0

    def set_visited_as(self, visited_as):
        self.visited_as = visited_as

    def get_visited_as(self):
        return self.visited_as

    def get_number(self):
        return self.number

    def get_direct_rel(self):
        return self.direct_rel

    def get_indirect_rel(self):
        return self.indirect_rel