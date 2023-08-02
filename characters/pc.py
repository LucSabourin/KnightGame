from knight_game import random, json, pandas
from knight_game.items import Item
from knight_game.items.consumables import Food, Scroll
from knight_game.items.equipment import Armour, Shield, Weapon


class Knight():
    """
    """


    increment_health = 25
    increment_damage = 10
    image = "knight"

    def __init__(self, name: str, gold: int, health: int, base_damage: float, weapon: Weapon, shield: Shield, armour: Armour, \
            inventory: list, followers: list = None, rank: int = 0):
        self.name = name
        self.gold = gold
        self.health = health
        self.max_health = health
        self.base_damage = base_damage
        self.weapon = weapon
        self.shield = shield
        self.armour = armour
        self.inventory = inventory
        self.followers = followers
        self.rank = rank

    def attack(self) -> float:
        """
        """


        attack_type = int(3 * random())
        damage = self.base_damage
        if self.weapon is not None and attack_type in [2, 3]:
            damage += self.weapon.attack()

        if self.shield is not None and attack_type in [1, 3]:
            damage += self.shield.attack()

        if self.armour is not None and attack_type in [0, 3]:
            damage += self.armour.attack()

        return damage
    
    def defend(self, damage: float) -> bool:
        """
        """


        if self.weapon is not None:
            damage -= self.weapon.defend()

        if self.shield is not None:
            damage -= self.shield.defend()

        if self.armour is not None:
            damage -= self.shield.defend()

        if damage >= 0:
            self.health -= damage
            if self.health <= 0:
                return True

        return False

    def flee(self, threat: float) -> bool:
        """
        """


        if self.weapon is not None:
            threat -= self.weapon.max_damage

        if self.shield is not None:
            threat -= self.shield.max_defence

        if self.armour is not None:
            threat -= self.armour.max_defence

        if threat > 0:
            return True
        else:
            return False

    def show_inventory(self):
        """
        """


        items = []
        for item in self.inventory:
            items.append(item.__dict__)
        
        print(pandas.read_json(json.dumps(items)))

    def buy_item(self, cost: int, item: Item) -> Item:
        """
        """


        if cost <= self.gold:
            self.gold -= cost
            self.add_item(item)
        else:
            return Item
    
    def sell_item(self, index: int) -> Item:
        """
        """


        item = self.inventory[index]
        self.inventory.remove(item)
        return item

    def add_gold(self, amount: int):
        """
        """


        self.gold += amount

    def add_item(self, item: Item):
        """
        """


        self.inventory.append(item)

    def equip_squire(self, index: int):
        """
        """


        item = self.inventory[index]
        self.inventory.remove(item)
        
        if type(item) == Weapon:

            if self.squire.weapon is not None:
                self.add_item(self.squire.weapon)

            self.squire.weapon = item
            return True
        
        elif type(item) == Shield:

            if self.squire.shield is not None:
                self.add_item(self.squire.shield)

            self.squire.shield = item
            return True

        elif type(item) == Armour:

            if self.squire.armour is not None:
                self.add_item(self.squire.armour)

            self.squire.armour = item
            return True

        else:
            self.add_item(item)
            raise IndexError

    def use_consumable(self, index) -> float:
        """
        """


        item = self.inventory[index]
        self.inventory.remove(item)

        if type(item) == Food:

            self.health += item.use()
            if self.health > self.max_health:
                self.health = self.max_health

        elif type(item) == Scroll:

            return item.use()

        else:
            self.add_item(item)
            raise IndexError

    def xp_up(self, xp: int):
        """
        """


        if self.xp_counter + xp > self.rank and self.rank < 10:
            self.xp_counter = self.xp_counter + xp - (self.rank + 1)
            self._rank_up()

        else:
            self.xp_counter += xp

    def _rank_up(self):
        """
        """


        self.health += self.increment_health
        self.max_health += self.increment_health
        self.base_damage += self.increment_damage
        self.rank += 1