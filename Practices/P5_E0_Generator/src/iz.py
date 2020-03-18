class Iz:
    def __init__(self):
        self.output = []
        self.input = 0

    def execute(self, input):
        '''self.output = []'''
        self.input = input
        binary_string = "{0:b}".format(self.input)
        for i in binary_string:
            self.output.append(ord(i) - 48)
        self.output = self.output[0:2]