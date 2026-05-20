# Ramdom Module
# used for randomness
import random

print(random.randint(1,100))

cards = ["ACE-1", "Heart-A", "ACE-10"]
print(random.choice(cards))

number = [1, 2, 3, 4, 5]
random.shuffle(number)
print(number)