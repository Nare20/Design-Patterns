
import copy


class GameCharacter:
    def __init__(self, name, health, level):
        self.name = name
        self.health = health
        self.level = level

    def clone(self):
        return copy.deepcopy(self)


character1 = GameCharacter("Knight", 100, 5)

character2 = character1.clone()
character2.name = "Warrior"

print(character1.name, character1.health, character1.level)
print(character2.name, character2.health, character2.level)
print(character1 is character2)

