class Adder:

    def __init__(self):
        self.inputs = []
        self.output = 0

    def execute(self,inputs):
        self.inputs = inputs
        self.output = 0
        for i in self.inputs:
            self.output += i