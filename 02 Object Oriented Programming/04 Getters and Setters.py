class Pikachu:
    type = 'electric'
    description = 'A yellow rat.'

    # the constructor
    def __init__(self):
        print('Constructor')
        self.nickname = input("What is the nickname? ")
        self.level = int(input("What is the level? "))
        self.hp = 10

    # Getters/Accessors
    @property
    def nickname(self):
        # really specify how you want it to return the nickname
        print('Getter/Accessor')
        return self._nickname

    @property
    def level(self):
        return self._level

    # Setters/Mutators

    @nickname.setter
    def nickname(self, new_nickname):
        # allows for range/value checking
        print('Setter/Mutator')
        if new_nickname in ['💩']:
            self._nickname = '****'
        else:
            self._nickname = new_nickname

    @level.setter
    def level(self, value):
        if value < 1:
            self._level = 1
        else:
            self._level = value


    # additional methods
    def level_up(self, message):
        print(message)
        self.level += 1

    def full_heal(self):
        self.hp = 10

    def __str__(self):
        result = ''
        result += f"Nickname: {self.nickname}"
        result += f"\nLevel: {self.level}"
        return result

pika1 = Pikachu('💩')
print(pika1.nickname)
pika1.nickname = 'Jordan'

print()
pika1.level = 10
print(pika1)
pika1.level = -10
print(pika1)

"""
pika1 = Pikachu()
print(pika1)
"""