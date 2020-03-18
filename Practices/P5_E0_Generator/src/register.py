import types

class Register:

    def __init__(self,seed):
        self.input = []
        self.output = []
        if isinstance(seed[0],str):
            for i in seed:
                self.input.append(ord(i)- 48 )
        else:
            self.input = seed
        self.output.append(self.input[1])
        self.output.append(self.input[0])

    def int_output(self):
        binary_string = ''
        for i in self.output:
            binary_string += str(i)
        return (int(binary_string,2))

    def least_significant(self):
        return (self.output[-1])

