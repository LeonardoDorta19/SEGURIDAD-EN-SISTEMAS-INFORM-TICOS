from a5 import A5

print("Input three seeds")
seed_one = input()
seed_two = input()
seed_three = input()
a5 = A5(seed_one,seed_two,seed_three)
print(a5.generate(6))