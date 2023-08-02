class Item():
    """
    """


    def __init__(self, name: str, min_stat: float, max_stat: float, crit_chance: float, value: int, item_type: int):
        self.name = name
        self.min_stat = min_stat
        self.max_stat = max_stat
        self.crit_chance = crit_chance
        self.value = value
        self.item_type = item_type


class LootBag():
    """
    """


    def __init__(self, gold: int = 0, inventory: list = None):
        self.gold = gold
        if inventory is None:
            self.inventory = []
        else:
            self.inventory = inventory

    def add_gold(self, amount: int):
        """
        """


        self.gold += amount
    
    def add_item(self, item: Item):
        """
        """


        self.inventory.append(item)
