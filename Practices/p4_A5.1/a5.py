from LFSP import Lfsp
from xor import Xor

import statistics
from statistics import mode

class A5:
    def __init__(self, seed_one, seed_two, seed_three):
        self.lfsp_one = Lfsp(seed_one)
        self.lfsp_two = Lfsp(seed_two)
        self.lfsp_three = Lfsp(seed_three)

        list_for_xor_register = [self.lfsp_one.seed[0],self.lfsp_one.seed[1],self.lfsp_one.seed[2],self.lfsp_one.seed[5]]
        self.xor_one = Xor(list_for_xor_register)

        list_for_xor_register = [self.lfsp_two.seed[0],self.lfsp_two.seed[1]]
        self.xor_two = Xor(list_for_xor_register)

        list_for_xor_register = [self.lfsp_three.seed[0], self.lfsp_three.seed[1], self.lfsp_three.seed[2],self.lfsp_three.seed[15]]
        self.xor_three = Xor(list_for_xor_register)

        list_for_xor_register.clear()
        list_for_xor_register = [self.lfsp_one[0], self.lfsp_two[0], self.lfsp_three[0]]
        self.xor_union = Xor(list_for_xor_register)

    def highest_function(self):
        register_list = self.lfsp_one[10], self.lfsp_two[11], self.lfsp_three[12]
        return mode(register_list)

    def generate(self,input_length):
        KeyStream = []
        highest_function_value = None
        for i in range(input_length):
            highest_function_value = self.highest_function()
            KeyStream.append(self.lfsp_one[0] ^ self.lfsp_two[0] ^ self.lfsp_three[0])
            if highest_function_value == self.lfsp_one[10]:
                self.lfsp_one.shift(self.xor_one.xor())
            if highest_function_value == self.lfsp_two[11]:
                self.lfsp_two.shift(self.xor_two.xor())
            if highest_function_value == self.lfsp_three[12]:
                self.lfsp_three.shift(self.xor_three.xor())
        return KeyStream


'''a5 = A5('10100000000000','000000000000111','0000000000000000000001')'''