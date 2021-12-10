class Pikachu:
    type = 'electric'
    description = 'A yellow rat.'

    # the constructor
    def __init__(self, nickname):
        self.nickname = nickname
        self.level = 1
        self.hp = 10

    # (instance) methods
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

    # class methods - apply to the class as a whole, class is an implicit argument
    @classmethod
    def set_description(cls, new_description):
        cls.description = new_description

    # static method - no implicit arguments
    @staticmethod
    def weak_against(type):
        return type in ['ground']
    


pika1 = Pikachu('Gauss')
print(pika1.level)
pika1.level_up('🎉')    
print(pika1.level)
print(pika1)                # same as next line
print(pika1.__str__())

Pikachu.set_description('An electric yellow rat')
        
print(Pikachu.weak_against('flying'))
print(Pikachu.weak_against('ground'))