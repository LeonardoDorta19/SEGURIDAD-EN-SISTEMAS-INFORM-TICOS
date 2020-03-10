class Xor:
    def __init__(self,register_list):
        self.register_list = register_list

    def xor(self):
        result = 0

        """        
        if self.register_list[0] == 0:
                    result = 0
                elif self.register_list[0] == 1:
                    result = 0
                result = not(self.register_list[0])
        """

        for i in self.register_list:
            result = result ^ i

        return  result

    def update_registers(self,register_list):
        self.register_list = register_list


'''ejemplo = [1,1,0]
xor = Xor(ejemplo)
print(xor.register_list)
print(xor.xor())
'''