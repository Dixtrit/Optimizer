class Constraint:
    def __init__(self, upper_bound = None, lower_bound = None, name, vallues = []):
        self.upper_bound = upper_bound
        self.name = name
        self.lower_bound = lower_bound
        self.vallues = vallues