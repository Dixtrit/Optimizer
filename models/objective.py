from models.objective_type import ObjectiveType


class Objective:
    def __init__(self, name, type: ObjectiveType, vallues):
        self.name = name
        self.type = type
        self.vallues = vallues
