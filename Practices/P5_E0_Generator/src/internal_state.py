class InternalState:

    def __init__(self):
        self.input = []
        self.output = []

    def execute(self, input):
        self.input = input
        self.output = input

    def t2_output(self):
        self.output[0], self.output[1] = self.output[1], (self.output[0] ^ self.output[1])
'''
i = InternalState([1,0])
i.execute([1,0])
i.t2_output()
print(i.output)
'''