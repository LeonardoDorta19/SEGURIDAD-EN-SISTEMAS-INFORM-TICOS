class Lfsr:
    def __init__(self,seed):
        seed_list = []
        for i in seed:
            seed_list.append(ord(i)- 48 )
        self.seed = seed_list
        self.output = None

    def shift(self,input):
        self.output = self.seed.pop(0)
        self.seed.append(input)

    def __str__(self):
        listToStr = ' '.join([str(elem) for elem in self.seed])
        return (listToStr)

    def __getitem__(self, key):
        return self.seed[key]

