# class names are UpperCamelCase

class Pikachu:
    # class variables - for all objects in the class
    type = 'electric'


    # the constructor
    def __init__(self, nickname):
        # instance variables go here
        self.nickname = nickname
        self.smile = '😀'


# Instatiation
pika_1 = Pikachu("Brad")
pika_2 = Pikachu("Rat")


print(pika_1.nickname)
print(pika_2.nickname)  # call on instance variables
print(Pikachu.type)     # call on class variables
print(pika_1.type)
print()

Pikachu.type = 'elec'
pika_2.nickname = "Rodent"
print(Pikachu.type)
print(pika_2.type)
print(pika_2.nickname)

"""
pika_2.type = "abc"
print(pika_2.type)
print(Pikachu.type)
"""
print(pika_2.smile)