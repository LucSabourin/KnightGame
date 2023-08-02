from items import Item
from knight_game import random


class Consumable(Item):
    """
    """


    def __init__(self, name: str, min_stat: float, max_stat: float, crit_chance: float, value: int, item_type: int = 0):
        self.name = name
        self.min_stat = min_stat
        self.max_stat = max_stat
        self.crit_chance = crit_chance
        self.value = value
        self.item_type = item_type

    def use(self) -> float:
        """
        """


        crit = random() * 100
        if crit <= 3 * self.crit_chance:
            return (2.5 * self.max_stat, 1)
        elif crit >= self.crit_chance + 85:
            return (0, -1)
        else:
            return ((self.max_stat - self.min_stat) * random() + self.min_stat, 0)

class Food(Consumable):
    """
    """


    def __init__(self, name: str, min_stat: float, max_stat: float, crit_chance: float, value: int, item_type: int = 0):
        self.name = name
        self.min_stat = min_stat
        self.max_stat = max_stat
        self.crit_chance = crit_chance
        self.value = value
        self.item_type = item_type


class Scroll(Consumable):
    """
    """


    def __init__(self, name: str, min_stat: float, max_stat: float, crit_chance: float, value: int, item_type: int = 0):
        self.name = name
        self.min_stat = min_stat
        self.max_stat = max_stat
        self.crit_chance = crit_chance
        self.value = value
        self.item_type = item_type
