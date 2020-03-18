from adder import Adder
from LFSR import Lfsr
from internal_state import InternalState
from register import Register
from xor import Xor
from iz import Iz

class E0Generator:
    def __init__(self):
        self.output = []
        self.shift_register1 = Lfsr(input("seed for the first RFSR:"),[8,12,20,25])
        self.shift_register2 = Lfsr(input("seed for the second RFSR:"),[21,16,24,31])
        self.shift_register3 = Lfsr(input("seed for the third RFSR:"),[4,24,28,33])
        self.shift_register4 = Lfsr(input("seed for the fourth RFSR:"),[4,28,36,39])
        self.r1 = Register(input("seed for the register R1:"))
        self.r2 = Register(self.r1.output)
        self.t1 = InternalState()
        self.t2 = InternalState()
        self.adder1 = Adder()
        self.adder2 = Adder()
        self.iz = Iz()
        self.xor_iz_t2 = Xor([self.t2.output,self.iz.output])
        self.xor_t1_xor = Xor([self.t1.output,self.xor_iz_t2.output])
        self.xor_zt = Xor([self.shift_register1.output,self.shift_register2.output,
                        self.shift_register3.output,self.shift_register4.output,self.r1.least_significant()])

    def execute(self,exit_bits_number):
        for i in range (exit_bits_number):
            self.t1.execute(self.r1.output)
            self.t2.execute(self.r2.output)
            self.t2.t2_output()
            self.adder1.execute([self.shift_register1.shift_right(),self.shift_register2.shift_right(),
                                  self.shift_register3.shift_right(),self.shift_register4.shift_right()])
            self.adder2.execute([self.adder1.output,self.r1.int_output()])
            self.iz.execute(self.adder2.output)
            self.xor_iz_t2.update_registers([self.t2.output, self.iz.output])
            self.xor_iz_t2.binary_xor()
            self.xor_t1_xor.update_registers([self.t1.output, self.xor_iz_t2.output])
            self.xor_t1_xor.binary_xor()
            self.xor_zt = Xor([self.shift_register1.output, self.shift_register2.output,
                               self.shift_register3.output, self.shift_register4.output, self.r1.least_significant()])
            self.output.append(self.xor_zt.xor())
            self.r1 = Register(self.xor_t1_xor.output)
            self.r2 = Register(self.r1.output)
