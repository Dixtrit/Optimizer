from objective_type import Objective_type


class Objective:
    def __init__(self, name, type: Objective_type, vallues):
        self.name = name
        self.type = type
        self.vallues = vallues
