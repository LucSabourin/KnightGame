from knight_game import random, json, pandas
from knight_game.items import Item
from knight_game.items.equipment import Weapon, Shield, Armour
from knight_game.characters import Combatant
from knight_game.adventures.quest_builder import generate_item


class Vendor():
    """
    """


    def __init__(self, name: str, gold: int, inventory: list):
        self.name = name
        self.gold = gold
        self.inventory = inventory

    def show_inventory(self):
        """
        """


        items = []
        for item in self.inventory:
            items.append(item.__dict__)
        
        print(pandas.read_json(json.dumps(items)))

    def buy_item(self, item: Item) -> int:
        """
        """


        cost = int(item.value * 1.2)
        # Sale is completed
        if cost <= self.gold:
            self.inventory.append(item)
            self.gold -= cost
            return cost
        # Vendor doesn't have enough gold
        else:
            return 0
    
    def sell_item(self, index: int) -> tuple:
        """
        """


        item = self.inventory[index]
        cost = int(item.value * 0.8)
        if cost == 0:
            cost = 1
        
        self.inventory.remove(item)
        self.gold += cost
        return (cost, item)


class Monster(Combatant):
    """
    """


    def __init__(self, name: str, health: int, gold: int, base_damage: float, loot_chance: float, rank: int, \
            weapon: Weapon = None, shield: Shield = None, armour: Armour = None):
        self.name = name
        self.image = name
        self.health = health
        self.gold = gold
        self.base_damage = base_damage
        self.loot_chance = loot_chance
        self.rank = rank
        self.weapon = weapon
        self.shield = shield
        self.armour = armour

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

    def dies(self) -> tuple:
        """
        """


        items = []
        if self.weapon is not None:
            items.append(self.weapon)
        
        if self.shield is not None:
            items.append(self.shield)
        
        if self.armour is not None:
            items.append(self.armour)
        
        loot = None
        if random() * 100 <= self.loot_chance:
            loot = generate_item(self.rank)

        return (self.gold, items, loot)

    def flee(self, threat: float) -> bool:
        """
        """


        if self.weapon is not None or self.shield is not None or self.armour is not None:

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

        elif threat > 0.25 * (self.health + self.base_damage):
            return True

        else:
            return False


class Follower(Combatant):
    """
    """


    increment_health = 0
    increment_damage = 0
    xp_counter = 0
    
    def __init__(self, name: str, health: int, base_damage: float, rank: int, \
            weapon: Weapon = None, shield: Shield = None, armour: Armour = None):
        self.name = name
        self.health = health
        self.max_health = health
        self.base_damage = base_damage
        self.rank = rank
        self.weapon = weapon
        self.shield = shield
        self.armour = armour

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

    def dies(self) -> tuple:
        """
        """


        items = []
        if self.weapon is not None:
            items.append(self.weapon)
        
        if self.shield is not None:
            items.append(self.shield)
        
        if self.armour is not None:
            items.append(self.armour)
        
        return (0, items, False)

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

    def change_weapon(self, weapon: Weapon = None) -> Weapon:
        """
        """


        item = None
        if self.weapon is not None:
            item = self.weapon
        
        self.weapon = weapon
        return item

    def change_shield(self, shield: Shield = None) -> Shield:
        """
        """


        item = None
        if self.shield is not None:
            item = self.shield
        
        self.shield = shield
        return item
    
    def change_armour(self, armour: Armour = None) -> Armour:
        """
        """


        item = None
        if self.armour is not None:
            item = self.armour
        
        self.armour = armour
        return item


class Squire(Follower):
    """
    """


    increment_health = 15
    increment_damage = 7.5
    image = "squire"
    
    def __init__(self, name: str, health: int, base_damage: float, rank: int = 2, \
            weapon: Weapon = None, shield: Shield = None, armour: Armour = None):
        self.name = name
        self.health = health
        self.max_health = health
        self.base_damage = base_damage
        self.rank = rank
        self.weapon = weapon
        self.shield = shield
        self.armour = armour


class Priest(Follower):
    """
    """


    increment_health = 25
    increment_damage = 5
    image = "priest"
    
    def __init__(self, name: str, health: int, base_damage: float, rank: int = 6, \
            weapon: Weapon = None, shield: Shield = None, armour: Armour = None):
        self.name = name
        self.health = health
        self.max_health = health
        self.base_damage = base_damage
        self.rank = rank
        self.weapon = weapon
        self.shield = shield
        self.armour = armour


class Ranger(Follower):
    """
    """


    increment_health = 10
    increment_damage = 10
    image = "ranger"
    
    def __init__(self, name: str, health: int, base_damage: float, rank: int = 4, \
            weapon: Weapon = None, shield: Shield = None, armour: Armour = None):
        self.name = name
        self.health = health
        self.max_health = health
        self.base_damage = base_damage
        self.rank = rank
        self.weapon = weapon
        self.shield = shield
        self.armour = armour
