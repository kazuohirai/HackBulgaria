from orc import Orc
from hero import Hero
from fight import Fight
from weapon import Weapon


class Dungeon:
    spawnlist = {}

    def __init__(self, filepath):
        self.filepath = filepath

    def print_map(self):
        f = open(self.filepath, "r+")
        output = f.read()
        f.close
        return output

    def get_player_indicator(self, player):
        if isinstance(player, Orc):
            return "O"
        if isinstance(player, Hero):
            return "H"

    def spawn(self, player_name, entity):
        #opens map and populates it with Player indicators (if possible)
        for item in self.spawnlist:
            if self.spawnlist[item] == entity:
                return "Character is already spawned."

        if player_name in self.spawnlist:
            return "Character is already spawned."
        else:
            output = []
            f = open(self.filepath, "r+")
            output += f.read()
            f.close()
            #if character is not already spawned, and there is free spawn slot, spawn it
            if "S" in "".join(output):
                for n, i in enumerate(output):
                    if i == 'S':
                        self.spawnlist[player_name] = entity
                        output[n] = self.get_player_indicator(entity)
                        break

            else:
                return "No free spawn slot."

            f = open(self.filepath, "w+")
            f.write("".join(output))
            f.close

    def get_coordinates(self, matrix, player):
        #gets current position of player
        badge = self.get_player_indicator(self.spawnlist[player])
        for row, item in enumerate(matrix):
            for col, i in enumerate(item):
                if badge == i:
                    return [row, col]

    def modify_indexes(self, GPSTuple, direction):
        #Returns coordinates of where the player wants to go
        if direction == "up":
            GPSTuple[0] -= 1
        if direction == "down":
            GPSTuple[0] += 1
        if direction == "left":
            GPSTuple[1] -= 1
        if direction == "right":
            GPSTuple[1] += 1
        return GPSTuple

    def get_value_from_single_element_dict(self, testdict):
        for key in testdict:
            value = testdict[key]
            return (value)

    def move(self, player_name, direction):
        #If wrong direction is given, do nothing
        directions = ['left', 'right', 'up', 'down']
        if direction not in directions:
            return "Wrong direction given."

        #Read map from file
        output = ""
        f = open(self.filepath, "r+")
        output += f.read()
        f.close()

        #converts output to list of lists of single-character strings (easier to work with)
        getGPS = output = [list(x) for x in output.split('\n')]
        #current coordinates
        location = self.get_coordinates(getGPS, player_name)
        #destination coordinates
        destination = self.modify_indexes(self.get_coordinates(getGPS, player_name), direction)

        #if coordinate tuple exceeds the map boundaries - terminate
        if (destination[0] < 0 or destination[1] < 0 or
                destination[0] > len(output) or
                destination[1] > len(output[0])):
            return "Out of Bounds."

        #What is the ASCI character in the given map location
        target = output[destination[0]][destination[1]]
        #Gets indicator of player who wants to execute a move on the board
        indicator = self.get_player_indicator(self.spawnlist[player_name])
        #enemy is opposite indicator
        enemy = "OH".replace(indicator, "")
        if target == "#":
            return "You will hit the wall."
        elif target == ".":
            #swap the "." and current moving player indicator in map
            output[location[0]][location[1]], output[destination[0]][destination[1]] = output[
                destination[0]][destination[1]], output[location[0]][location[1]]
        elif target == enemy:
            #tokill is opposite object of currently-moving player
            enemyElem = {i: self.spawnlist[i] for i in self.spawnlist if i != player_name}
            ToKill = self.get_value_from_single_element_dict(enemyElem)
            #creates fight and simulates it, leaving only winning player on map
            #if winner attacked, its indicator overwrites the fallen enemy's one
            #if winner was attacked, the fallen enemy one's is changed wiht "." on map
            bitka = Fight(self.spawnlist[player_name], ToKill)
            battle_result = bitka.simulate_fight()
            output[location[0]][location[1]] = "."
            output[destination[0]][destination[1]] = self.get_player_indicator(battle_result)
            for item in self.spawnlist:
                if self.spawnlist[item] == battle_result:
                    print ("{} wins!".format(item))

        #saves information to the dungeon map text file
        f = open(self.filepath, "w+")
        for i in range(0, len(output)):
            if i != (len(output) - 1):
                f.write("".join(output[i]) + "\n")
            else:
                f.write("".join(output[i]))
        f.close()


# orc = Orc("Orc", 100, 1.4)
# weapon1 = Weapon("Axe", 15, 0.4)
# orc.equip_weapon(weapon1)

# hero = Hero("Hero", 100, "Heroic")
# weapon2 = Weapon("Sword", 14, 0.6)
# hero.equip_weapon(weapon2)

# peshtera = Dungeon("basic-dungeon.txt")
# peshtera.spawn("Player One", orc)
# peshtera.spawn("Player Two", hero)
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "down")
# peshtera.move("Player One", "down")
# peshtera.move("Player One", "down")
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "right")
# peshtera.move("Player One", "up")
# peshtera.move("Player Two", "up")
# peshtera.move("Player Two", "up")
# peshtera.move("Player Two", "up")
# peshtera.move("Player Two", "up")
# peshtera.move("Player Two", "left")
# peshtera.move("Player Two", "left")
# peshtera.move("Player Two", "left")
# peshtera.move("Player Two", "left")
# peshtera.move("Player Two", "down")
# print(peshtera.move("Player One", "up"))
# print (peshtera.print_map())
