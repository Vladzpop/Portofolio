class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        self.exits = {}

    def add_exit(self, direction, room):
        self.exits[direction] = room

    def get_exit(self, direction):
        return self.exits.get(direction)


class Player:
    def __init__(self, name, current_room):
        self.name = name
        self.current_room = current_room

    def move(self, direction):
        next_room = self.current_room.get_exit(direction)
        if next_room:
            self.current_room = next_room
            print("Ai mers spre", direction)
            self.look_around()
        else:
            print("Nu poți merge acolo")

    def look_around(self):
        print(self.current_room.description)


# Create rooms
room1 = Room("Camera 1", "Te afli într-o cameră întunecată.")
room2 = Room("Camera 2", "Te afli într-o sală suspicioasă.")
room3 = Room("Camera 3", "Te afli într-o cameră îngustă.")

# Set up room exits
room1.add_exit("est", room2)
room2.add_exit("vest", room1)
room2.add_exit("nord", room3)
room3.add_exit("sud", room2)

# Create the player and place them in a starting room
player = Player("Ion", room1)

# Game loop
while True:
    command = input("Introdu comanda: ").lower()

    if command == "părăsește":
        print("La revedere!")
        break
    elif command == "privește":
        player.look_around()
    elif command in ["nord", "sud", "est", "vest"]:
        player.move(command)
    else:
        print("Comandă invalidă.")
