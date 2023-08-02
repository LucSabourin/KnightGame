from knight_game import choice
from knight_game.items import Item
from knight_game.items.equipment import Weapon, Shield, Armour
from knight_game.items.consumables import Scroll, Food
from knight_game.characters.npcs import Monster, Follower, Vendor, Squire, Ranger, Priest
from knight_game.config import weapons, shields, armours, foods, scrolls, followers, vendors, monsters, \
    generate_character_name

def generate_item(rank: int) -> Item:
    """
    """


    rand = choice([0, 1])
    if rand == 1:
        rand = choice([0, 1, 2])

        if rand == 0:
            return generate_weapon(rank)
        elif rand == 1:
            return generate_shield(rank)      
        elif rand == 2:
            return generate_shield(rank)
    
    elif rand == 0:
        rand = choice([0, 1])

        if rand == 0:
            return generate_food(rank)
        elif rand == 1:
            return generate_scroll(rank)

def generate_weapon(rank: int, name: str = "") -> Weapon:
    """
    """


    if name == "":
        keep = []
        for weapon in weapons:
            if rank + 1 <= weapon['rank'] and rank + 1 >= weapon['rank']:
                keep.append(weapon.pop('rank'))

        item = choice(keep)

    else:
        for weapon in weapons:
            if weapon['name'] == name:
                item = weapon
                return

    item = item.pop('rank')
    return Weapon(**item)

def generate_shield(rank: int, name: str = "") -> Shield:
    """
    """


    if name == "":
        keep = []
        for shield in shields:
            if rank + 1 <= shield['rank'] and rank + 1 >= shield['rank']:
                keep.append(shield.pop('rank'))

        item = choice(keep)

    else:
        for shield in shields:
            if shield['name'] == name:
                item = shield
                return

    item = item.pop('rank')
    return Shield(**item)

def generate_armour(rank: int, name: str = "") -> Armour:
    """
    """


    if name == "":
        keep = []
        for armour in armours:
            if rank + 1 <= armour['rank'] and rank + 1 >= armour['rank']:
                keep.append(armour.pop('rank'))

        item = choice(keep)

    else:
        for armour in armours:
            if armour['name'] == name:
                item = armour
                return

    item = item.pop('rank')
    return Armour(**item)

def generate_scroll(rank: int) -> Scroll:
    """
    """


    keep = []
    for scroll in scrolls:
        if rank + 1 <= scroll['rank'] and rank + 1 >= scroll['rank']:
            keep.append(scroll.pop('rank'))

    item = choice(keep).pop('rank')
    return Scroll(**item)

def generate_food(rank: int) -> Food:
    """
    """


    keep = []
    for food in foods:
        if rank + 1 <= food['rank'] and rank + 1 >= food['rank']:
            keep.append(food.pop('rank'))

    item = choice(keep).pop('rank')
    return Food(**item)

def generate_follower(rank: int) -> Follower:
    """
    """


    if rank >= 6:
        rand = choice([0, 1, 2])

    elif rank >= 4:
        rand = choice([0, 1])

    elif rank >= 2:
        rand = 0

    else:
        return None

    follower = followers[rand]
    follower['name'] = generate_character_name()
    follower['weapon'] = generate_weapon(rank, follower['weapon'])
    follower['shield'] = generate_shield(rank, follower['shield'])
    follower['armour'] = generate_shield(rank, follower['armour'])

    if rand == 0:
        return Squire(**follower)

    elif rand == 1:
        return Ranger(**follower)

    elif rand == 2:
        return Priest(**follower)

def generate_vendor(rank: int, name: str) -> Vendor:
    """
    """


    for character in vendors:
        if character['type'] == name:
            vendor = character

    character_name = generate_character_name()
    inventory = []
    if vendor['type'] == 'chef':
        for _ in range(10):
            inventory.append(generate_food(rank))

    elif vendor['type'] == 'blacksmith':
        for _ in range(5):
            inventory.append(generate_weapon(rank))

        for _ in range(5):
            inventory.append(generate_shield(rank))

        for _ in range(5):
            inventory.append(generate_armour(rank))

    elif vendor['type'] == 'mage':
        for _ in range(5):
            inventory.append(generate_scroll(rank))

    return Vendor(name=character_name, gold=vendor['gold'] + 25 * rank, inventory=inventory)

def generate_monster(name: str) -> Monster:
    """
    """


    for character in monsters:
        if character['name'] == name:
            monster = character
            break
    
    if monster['weapon'] is not None:
        monster['weapon'] = generate_weapon(monster['rank'], monster['weapon'])

    if monster['shield'] is not None:
        monster['shield'] = generate_shield(monster['rank'], monster['shield'])

    if monster['armour'] is not None:
        monster['armour'] = generate_armour(monster['rank'], monster['armour'])

    return Monster(**monster)
