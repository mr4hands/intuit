class MissingParamsError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)

class CantAggragateError(Exception):
    def __init__(self, value):
        self.value = value
    def __str__(self):
        return repr(self.value)