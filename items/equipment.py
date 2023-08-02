from items import Item
from knight_game import random


class Equipment(Item):
    """
    """

    def __init__(self, name: str, min_stat: float, max_stat: float, crit_chance: float, value: int, item_type: int):
        self.name = name
        self.min_stat = min_stat
        self.max_stat = max_stat
        self.crit_chance = crit_chance
        self.value = value
        self.item_type = item_type

    def attack(self) -> float:
        """
        """

        crit = random() * 100
        
        if self.item_type == 1:
            if crit <= self.crit_chance:
                return (2.5 * self.max_stat, 1)
            elif crit >= self.crit_chance + 75:
                return (0, -1)
            else:
                return ((self.max_stat - self.min_stat) * random() + self.min_stat, 0)
        
        elif self.item_type == -1:
            if crit * 2 <= self.crit_chance:
                return (self.max_stat, 1)
            elif crit * 2 >= self.crit_chance + 75:
                return (0, -1)
            else:
                return (self.min_stat * random(), 0)

    def defend(self) -> float:
        """
        """


        crit = random() * 100
        
        if self.item_type == -1:
            if crit <= self.crit_chance:
                return (2.5 * self.max_stat, 1)
            elif crit >= self.crit_chance + 75:
                return (0, -1)
            else:
                return ((self.max_stat - self.min_stat) * random() + self.min_stat, 0)
        
        elif self.item_type == 1:
            if crit * 2 <= self.crit_chance:
                return (self.max_stat, 1)
            elif crit * 2 >= self.crit_chance + 75:
                return (0, -1)
            else:
                return (self.min_stat * random(), 0)


class Weapon(Equipment):
    """
    """


    def __init__(self, name: str, min_stat: float, max_stat: float, crit_chance: float, value: int, item_type: int = 1):
        self.name = name
        self.min_stat = min_stat
        self.max_stat = max_stat
        self.crit_chance = crit_chance
        self.value = value
        self.type = item_type


class Shield(Equipment):
    """
    """


    def __init__(self, name: str, min_stat: float, max_stat: float, crit_chance: float, value : int, item_type: int = -1):
        self.name = name
        self.min_stat = min_stat
        self.max_stat = max_stat
        self.crit_chance = crit_chance
        self.value = value
        self.item_type = item_type


class Armour(Equipment):
    """
    """


    def __init__(self, name: str, min_stat: float, max_stat: float, crit_chance: float, value: int, item_type: int = -1):
        self.name = name
        self.min_stat = min_stat
        self.max_stat = max_stat
        self.crit_chance = crit_chance
        self.value = value
        self.item_type = item_type
