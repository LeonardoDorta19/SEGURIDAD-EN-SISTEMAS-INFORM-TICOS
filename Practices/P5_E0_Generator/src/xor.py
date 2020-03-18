class Xor:
    def __init__(self,register_list):
        self.register_list = register_list
        self.output = []

    def xor(self):
        result = 0
        for i in self.register_list:
            result = result ^ i
        self.output = result
        return  result

    def binary_xor(self):
        self.output.append(self.register_list[0][0] ^ self.register_list[1][0])
        self.output.append(self.register_list[0][1] ^ self.register_list[1][1])


    def update_registers(self,register_list):
        self.register_list = register_list
