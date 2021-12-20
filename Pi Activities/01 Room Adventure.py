from time import sleep

# Room Class
class Room:

    # constructor
    def __init__(self, name):
        self.name = name
        self.exit_directions = []       # north, south, east, west
        self.exit_destinations = []     # Rooms themselves
        self.items = []
        self.item_descriptions = []
        self.grabbables = []
    
    # getters/setters
    @property                   # name
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value 

    @property                   # exit_directions
    def exit_directions(self):
        return self._exit_directions
    
    @exit_directions.setter
    def exit_directions(self, value):
        self._exit_directions = value 

    @property                   # exit_destinations
    def exit_destinations(self):
        return self._exit_destinations
    
    @exit_destinations.setter
    def exit_destinations(self, value):
        self._exit_destinations = value 

    @property                   # items
    def items(self):
        return self._items
    
    @items.setter
    def items(self, value):
        self._items = value 

    @property                   # item_descriptions
    def item_descriptions(self):
        return self._item_descriptions
    
    @item_descriptions.setter
    def item_descriptions(self, value):
        self._item_descriptions = value 

    @property                   # grabbables
    def grabbables(self):
        return self._grabbables
    
    @grabbables.setter
    def grabbables(self, value):
        self._grabbables = value 


    # additional methods
    def add_exit(self, exit_direction, exit_destination):
        self.exit_directions.append(exit_direction)
        self.exit_destinations.append(exit_destination)

    def add_item(self, item_name, item_description):
        self.items.append(item_name)
        self.item_descriptions.append(item_description)

    def add_grabbable(self, new_grabbable):
        self.grabbables.append(new_grabbable)

    def delete_grabbable(self, existing_grabbable):
        if existing_grabbable in self.grabbables:
            self.grabbables.remove(existing_grabbable)


    # __str__ method
    def __str__(self):
        result = ''

        # Where we are
        result += f"Location: {self.name}\n"

        # What we see
        if len(self.items) != 0:
            result += "You see:"
            for item in self.items:
                result += f" {item}"
            result += "\n"

        # Where we can go
        if len(self.exit_directions) != 0:
            result += "Exits:"
            for direction in self.exit_directions:
                result += f" {direction}"
            
        return result

# Create Rooms Function
def create_rooms(starting_room=1):
    
    # create rooms
    r1 = Room("Room 1")
    r2 = Room("Room 2")
    r3 = Room("Room 3")
    r4 = Room("Room 4")
    rooms = [r1, r2, r3, r4]

    # add exits to rooms
    r1.add_exit("east", r2)
    r1.add_exit("south", r3)

    r2.add_exit("south", r4)
    r2.add_exit("west", r1)

    r3.add_exit("east", r4)
    r3.add_exit("north", r1)

    r4.add_exit("north", r2)
    r4.add_exit("west", r3)
    r4.add_exit("south", None)

    # add items
    # Room 1 - chair, table
    r1.add_item("chair", "It only has three legs. I'm not going to sit there.")
    r1.add_item("table", "There is a key sitting on it. Maybe I should take it.")
    # Room 2 - rug, fireplace
    r2.add_item("rug", "It's shaggy. Could use a vacuuming.")
    r2.add_item("fireplace", "It's already lit. Was someone just here?")
    # Room 3 - bookshelves, statue
    r3.add_item("bookshelves", "They're full. But they only contain copies of one book. The Stewart calculus book.")
    r3.add_item("statue", "It's a replica of 'Aspire, the spire'")
    # Room 4 - oven
    r4.add_item("oven", "Its in the middle of the room. There's fresh bread on top! 🥖")

    # add grabbables
    # Room 1 - Key
    r1.add_grabbable('key')
    # Room 2 - none
    # Room 3 - book
    r3.add_grabbable('book')
    # Room 4 - bread
    r4.add_grabbable('bread')

    return rooms[starting_room-1]


# Death Function
def death():
    print("You fell out the window and died from embarassment.")
    print("💀")

# Main Program 
inventory = []
current_room = create_rooms()

while True:
    # kill the game if the player dies
    if current_room == None:
        death()
        break

    # status base
    status = "\n" + str(current_room)

    # build status
    if len(inventory) != 0:
        status += f"\nYou are carrying: "
        status += ', '.join(inventory)
    else:
        status += "\nYou have no items in your inventory."

    # inform user of status
    print(status)

    # set default response
    response = "Invalid input. Try the format [verb] [noun]. I only understand the verbs 'go', 'take', and 'look'.\nType 'q' to quit."

    action = input("What would you to do? ").lower()

    if action in ['q']:
        break

    words = action.split()
    if len(words) == 2:
        verb = words[0]
        noun = words[1]

        if verb == "go":
            response = "I can't go there."
            if noun in current_room.exit_directions:
                index = current_room.exit_directions.index(noun)
                current_room = current_room.exit_destinations[index]
                response = "Room Changed."

        elif verb == "look":
            response = "That item doesn't exist."
            if noun in current_room.items:
                index = current_room.items.index(noun)
                response = current_room.item_descriptions[index]

        elif verb == "take":
            response = "That is not something I can take."
            if noun in current_room.grabbables:
                inventory.append(noun)
                current_room.delete_grabbable(noun)
                response = f"Grabbed {noun}"

    print(f"\n{response}")
    sleep(1)


