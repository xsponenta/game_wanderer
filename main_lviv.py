import game_lviv

kozelnytska = game_lviv.Street("Kozelnytska")
kozelnytska.set_description("Streat where is UCU.")
some_item = game_lviv.Item("wallet")
some_item.set_description("Could be money here.")
kozelnytska.set_item(some_item)
cavalier = game_lviv.Cavalier()
kozelnytska.set_character(cavalier)

stryiska = game_lviv.Street("Stryiska")
stryiska.set_description("So..long street")
item_that_not_help = game_lviv.Item("milk")
item_that_not_help.set_description("U can use it for coffe with chokolate.")
stryiska.set_item(item_that_not_help)
zbuy = game_lviv.Zbuy()
stryiska.set_character(zbuy)

franka = game_lviv.Street("Franka")
franka.set_description("So beatiful street, a way from UCU to the centre and back.")
knife = game_lviv.Item("knife")
knife.set_description("Maybe so sharp!")
franka.set_item(knife)
lotr = game_lviv.Lotr()
franka.set_character(lotr)

shevchenka = game_lviv.Street("Shevchenka")
shevchenka.set_description("Opera is here!!!")
batyar = game_lviv.Batyar()
shevchenka.set_character(batyar)

krakivska = game_lviv.Street("Krakivska")
krakivska.set_description("Finally, now for the track back")
some_item = game_lviv.Item("some_item")
some_item.set_description("Gotta have some money around here")
kozelnytska.set_item(some_item)

stryiska.link_room(franka, "west")
franka.link_room(stryiska, "east")

kozelnytska.link_room(franka, "south")
franka.link_room(kozelnytska, "north")

franka.link_room(shevchenka, "west")
shevchenka.link_room(franka, "east")

shevchenka.link_room(krakivska, "north")
krakivska.link_room(shevchenka, "south")

current_room = kozelnytska

backpack = []

dead = False

while dead == False:
    print("\n")
    enemy_dealt_with = False
    current_room.get_details()

    inhabitant = current_room.get_character()
    if inhabitant is not None:
        inhabitant.describe()

    item = current_room.get_item()
    if item is not None:
        item.describe()

    command = input("> ")

    if (
        command in ["north", "south", "east", "west"]
        and current_room.character is None
    ):
        # Move in the given direction
        current_room = current_room.move(command)
    if (
        command in ["north", "south", "east", "west"]
        and not current_room.character is not None
    ):
        print("Deal with the person first, you rude harlot!")
    elif command == "talk":
        # Talk to the inhabitant - check whether there is one!
        if inhabitant is not None:
            inhabitant.talk()
            # Fight with the inhabitant, if there is one
            print("What will you deal with the person with?")
            fight_with = input()

            # Do I have this item?
            if fight_with in backpack:
                if inhabitant.fight(fight_with) == True:
                    # What happens if you win?
                    print("Hooray, you won the fight!")
                    current_room.character = None
                else:
                    # What happens if you lose?
                    print("Oh dear, you lost.")
                    print("That's the end of the game.")
                    dead = True
            else:
                print("You don't have a " + fight_with)
        else:
            print("There is no one here to deal with")
    elif command == "take":
        if item is not None:
            print("You put the " + item.get_name() + " in your backpack")
            backpack.append(item.get_name())
            current_room.set_item(None)
        else:
            print("There's nothing here to take!")
    else:
        print("I don't know how to " + command)