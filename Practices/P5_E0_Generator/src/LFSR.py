from xor import Xor

class Lfsr:
    def __init__(self,seed, feedback_polynomial):
        seed_list = []
        for i in seed:
            seed_list.append(ord(i)- 48 )
        self.seed = seed_list
        self.output = None
        self.feedback_polynomial = feedback_polynomial
        feedback_polynomial_for_xor = [self.seed[i] for i in range(len(feedback_polynomial))]
        self.xor = Xor(feedback_polynomial_for_xor)

    def shift_left(self):
        self.output = self.seed.pop(0)
        self.seed.append(self.xor.xor())
        return (self.output)

    def shift_right(self):
        self.output = self.seed.pop(-1)
        self.seed.insert(0,self.xor.xor())
        return (self.output)

    def __str__(self):
        listToStr = ' '.join([str(elem) for elem in self.seed])
        return (listToStr)

    def __getitem__(self, key):
        return self.seed[key]