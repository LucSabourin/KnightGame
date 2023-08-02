from knight_game import random, choice
from knight_game.items import LootBag
from knight_game.adventures.quest_builder import generate_vendor, generate_follower, generate_item, generate_monster


class Location():
    """
    """


    def __init__(self, name: str, num_chars: int, rank: int, type: int):
        self.name = name
        self.type = type
        self.rank = rank
        self.num_chars = num_chars


class Town(Location):
    """
    """


    types = {'chef': 0, 'blacksmith': 2, 'mage': 4}

    def __init__(self, name: str, num_chars: int, rank: int, type: int = 1):
        self.name = name
        self.type = type
        self.rank = rank
        self.num_chars = num_chars
        self._setup()
        self._generate_chars()

    def _setup(self):
        """
        """


        remove = []
        for vendor, rank in self.types.items():
            if rank > self.rank:
                remove.append(vendor)

        for vendor in remove:
            self.types.pop(vendor)

    def _generate_chars(self):
        """
        """


        self.chars = []
        for _ in range(0, self.num_chars):
            while True:
                if len(self.types.keys()) > 0:
                    break

                else:
                    vendor = choice(self.types.keys())
                    if vendor not in self.chars:
                        self.chars.append(generate_vendor(self.rank, vendor))
                        self.types.pop(vendor)
                        break

    def special(self) -> tuple:
        """
        """


        if random() <= 0.25:
            reward = int(random() * 3)
            gold = 0
            follower = None
            item = None

            if reward in [0, 3]:
                gold = 25 * (self.rank + 1)

            if reward in [1, 3]:
                follower = generate_follower(self.rank)

            if reward in [2, 3]:
                item = generate_item(self.rank)

            return (gold, follower, item)


class Combat(Location):
    """
    """


    types = {'wolf': 0, 'bandit': 1, 'goblin': 2, 'spider': 3, 'skeleton': 4, 'centaur': 5, \
        'wraith': 6, 'minotaur': 7, 'demon': 8}
    
    def __init__(self, name: str, num_chars: int, rank: int, xp: int, type: int = 0):
        self.name = name
        self.num_chars = num_chars
        self.rank = rank
        self.combat = rank + xp
        self.type = type
        self._setup()
        self._generate_chars()
        self.loot_bag = LootBag()

    def _setup(self):
        """
        """


        remove = []
        for monster, rank in self.types.items():
            if self.rank == 0:
                if rank > 0:
                    remove.append(monster)
            
            else:
                if rank > self.rank + 1:
                    remove.append(monster)
                
                elif rank < self.rank - 1:
                    remove.append(monster)
        
        for monster in remove:
            self.types.pop(monster)

    def _generate_chars(self):
        """
        """


        self.chars = []
        for _ in range(0, self.num_chars):
            monster = choice(self.types.keys())
            self.chars.append(generate_monster(monster))
