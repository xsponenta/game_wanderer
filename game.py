"""
The game module
"""

class Room:
    """
    Class for the ROOM
    """
    def __init__(self, name: str):
        """
        The Init method
        """
        self.name = name
        self.directions = {}
        self.description = "Hah! What should i write here?"
        self.character = None
        self.item = None

    def link_room(self, room: "Room", direction: str):
        """
        The Link method for room
        """
        self.directions[direction] = room

    def set_description(self, description: str):
        """
        Setting description for the game
        """
        self.description = description

    def set_character(self, char):
        """
        Seting for the character
        """
        self.character = char

    def set_item(self, item):
        """
        Seting for the item
        """
        self.item = item

    def get_item(self) -> "Item | None":
        """
        Gettind the item
        """
        return self.item

    def get_character(self) -> "Enemy | None":
        """
        Getting the character
        """
        return self.character

    def move(self, direction: str) -> "Room":
        """
        Moving to the another one room
        """
        return self.directions[direction]

    def get_details(self):
        """
        Describing the room
        """
        print(self.name)
        print('-'*20)
        print(self.description)
        for key, val in self.directions.items():
            print(f"The {val.name} is {key}")


class Enemy:
    """
    Class for the Enemy
    """

    defeated = 0

    def __init__(self, name: str, description: str):
        """
        The Init method for enemy
        """
        self.name = name
        self.description = description
        self.converastion = "What?"
        self.weakness = None

    def talk(self):
        """
        Talking with the enemy
        """
        print(self.converastion)

    def describe(self):
        """
        Describing inhabitant
        """
        print(self.description)

    def set_conversation(self, convo: str):
        """
        Setting the caracter's conversation line
        """
        self.converastion = convo

    def set_weakness(self, weak: str):
        """
        Setting the character's weakness
        """
        self.weakness = weak

    def fight(self, item: str):
        """
        Checking weakness to the item
        """
        if self.weakness is not None and item == self.weakness:
            Enemy.defeated += 1
            return True
        return False

    def get_defeated(self) -> int:
        """
        Getting number defeated enemies
        """
        return self.defeated


class Item:
    """
    Class for the Item
    """

    def __init__(self, name: str):
        """
        Init for the Item
        """
        self.name = name
        self.description = "description"

    def get_name(self) -> str:
        """
        Getting the item's name
        """
        return self.name

    def describe(self):
        """
        Getting description for the item
        """
        print(self.description)

    def set_description(self, descript: str):
        """
        Setting description for the item
        """
        self.description = descript
