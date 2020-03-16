from LFSR import Lfsr
from xor import Xor

import statistics
from statistics import mode

class A5:
    def __init__(self, seed_one, seed_two, seed_three):
        self.Lfsr_one = Lfsr(seed_one)
        self.Lfsr_two = Lfsr(seed_two)
        self.Lfsr_three = Lfsr(seed_three)

        list_for_xor_register = [self.Lfsr_one.seed[0],self.Lfsr_one.seed[1],self.Lfsr_one.seed[2],self.Lfsr_one.seed[5]]
        self.xor_one = Xor(list_for_xor_register)

        list_for_xor_register = [self.Lfsr_two.seed[0],self.Lfsr_two.seed[1]]
        self.xor_two = Xor(list_for_xor_register)

        list_for_xor_register = [self.Lfsr_three.seed[0], self.Lfsr_three.seed[1], self.Lfsr_three.seed[2],self.Lfsr_three.seed[15]]
        self.xor_three = Xor(list_for_xor_register)

        list_for_xor_register.clear()
        list_for_xor_register = [self.Lfsr_one[0], self.Lfsr_two[0], self.Lfsr_three[0]]
        self.xor_union = Xor(list_for_xor_register)

    def highest_function(self):
        register_list = self.Lfsr_one[10], self.Lfsr_two[11], self.Lfsr_three[12]
        return mode(register_list)

    def generate(self,input_length):
        KeyStream = []
        highest_function_value = None
        for i in range(input_length):
            highest_function_value = self.highest_function()
            KeyStream.append(self.Lfsr_one[0] ^ self.Lfsr_two[0] ^ self.Lfsr_three[0])
            if highest_function_value == self.Lfsr_one[10]:
                self.Lfsr_one.shift(self.xor_one.xor())
            if highest_function_value == self.Lfsr_two[11]:
                self.Lfsr_two.shift(self.xor_two.xor())
            if highest_function_value == self.Lfsr_three[12]:
                self.Lfsr_three.shift(self.xor_three.xor())
        return KeyStream


'''a5 = A5('10100000000000','000000000000111','0000000000000000000001')'''