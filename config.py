from knight_game import os, json, choice

root_dir = os.path.dirname(os.path.abspath(__file__)) + '/library/'

armours = json.load(root_dir + 'armour.json')
foods = json.load(root_dir + 'food.json')
scrolls = json.load(root_dir + 'scrolls.json')
shields = json.load(root_dir + 'shields.json')
weapons = json.load(root_dir + 'weapons.json')

followers = json.load(root_dir + 'followers.json')
monsters = json.load(root_dir + 'monsters.json')
vendors = json.load(root_dir + 'vendors.json')

def generate_arena_name() -> str:
    """
    """


    file = root_dir + 'arena_names.txt'
    with open(file, 'r+') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return choice(lines)

def generate_character_name() -> str:
    """
    """


    file = root_dir + 'character_names.txt'
    with open(file, 'r+') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return choice(lines)

def generate_town_name() -> str:
    """
    """


    file = root_dir + 'town_names.txt'
    with open(file, 'r+') as f:
        lines = f.readlines()

    lines = [line.strip() for line in lines]

    return choice(lines)

