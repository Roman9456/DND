import random
class Character:
    def __init__(self, name, race, char_class):
        self.name = name
        self.race = race
        self.char_class = char_class
        self.level = 1
        self.max_hp = 10
        self.current_hp = 10
        self.strength = 10
        self.dexterity = 10
        self.constitution = 10
        self.intelligence = 10
        self.wisdom = 10
        self.charisma = 10
        self.inventory = []
        self.spells = []

    def level_up(self):
        self.level += 1
        self.max_hp += 5
        self.current_hp += 5
        # Добавление новых способностей

    def add_to_inventory(self, item):
        self.inventory.append(item)

    def add_spell(self, spell):
        self.spells.append(spell)


class Bard:


 def __init__(self, level):
    self.level = level
    self.hit_dice = "1d8"
    self.hit_points = 8 + self.get_modifier("constitution")
    self.proficiency_bonus = self.get_proficiency_bonus(level)
    self.armor = "Light Armor"
    self.weapons = ["Simple weapons", "Longswords", "Shortswords", "Rapiers", "Hand Crossbows"]
    self.tools = ["Three musical instruments of your choice"]
    self.saving_throws = ["Dexterity", "Charisma"]
    self.skills = [
        "Choose three from Acrobatics, Animal Handling, Arcana, Athletics, Deception, History, Insight, Intimidation, Investigation, Medicine, Nature, Perception, Performance, Persuasion, Religion, Sleight of Hand, Stealth, and Survival"]
    self.equipment = ["Rapier", "Longsword or any simple weapon", "Diplomat's Pack or Entertainer's Pack",
                      "Lute or any other musical instrument", "Leather Armor and Dagger"]


def get_modifier(self, attribute):
    # метод для получения модификатора характеристики
    pass


def get_proficiency_bonus(self, level):
    # метод для получения бонуса мастерства
    pass


class Barbarian:
 def __init__(self, level):
    self.level = level
    self.hit_die = 12
    self.proficiencies = {
        "armor": ["light", "medium", "shields"],
        "weapons": ["simple", "martial"],
        "saving_throws": ["strength", "constitution"],
        "skills": ["athletics", "perception", "survival", "intimidation", "nature", "animal_handling"]
    }
    self.equipment = {
        "weapons": ["greataxe", "any martial melee weapon"],
        "secondary_weapons": ["two handaxes", "any simple weapon"],
        "armor": ["any light or medium armor", "shield"],
        "gear": ["explorer's pack", "four javelins"]
    }
    self.starting_gold = "2d4x10"


def get_hit_points(self, constitution_modifier):
    hit_points = 12 + constitution_modifier
    for level in range(2, self.level + 1):
        hit_points += max(1, self.hit_die // 2 + 1) + constitution_modifier
    return hit_points


class Warrior(Character):
    def __init__(self, level, strength_mod, constitution_mod):
        self.level = level
        self.hit_dice = 10
        self.hit_points = 10 + constitution_mod

        for i in range(2, level + 1):
            roll = random.randint(1, self.hit_dice)
            self.hit_points += max(roll + constitution_mod, 1)

        self.proficiencies = {
            "armor": ["light", "medium", "heavy", "shield"],
            "weapons": ["simple", "martial"],
            "tools": [],
            "saving_throws": ["strength", "constitution"],
            "skills": []
        }

        self.equipment = {
            "armor": "",
            "weapons": "",
            "tools": "",
            "other": ""
        }

        self.starting_equipment = [
            ["chain mail", "leather armor and longbow with 20 arrows"],
            ["a martial weapon and a shield", "two martial weapons"],
            ["a light crossbow and 20 bolts", "two handaxes"],
            ["a dungeoneer's pack", "an explorer's pack"]
        ]

    def __repr__(self):
        return "Warrior(level={}, hit_dice={}, hit_points={}, proficiencies={}, equipment={})".format(
            self.level, self.hit_dice, self.hit_points, self.proficiencies, self.equipment)
        warrior = Warrior(1, 2, 1)
        print(warrior)


class Wizard:
    def modifier(score):
        return (score - 10) // 2

    def choose(items, count):
        return random.sample(items, count)

    def __init__(self):
        self.hit_die = 6
        self.hit_points = 6 + modifier(CON)
        self.saving_throws = [INT, WIS]
        self.proficiencies = {
            "armor": [],
            "weapons": ["dagger", "dart", "sling", "quarterstaff", "light crossbow"],
            "tools": [],
            "skills": choose(2, ["arcana", "history", "medicine", "perception", "investigation", "religion"]),
        }
        self.equipment = [
            choose(1, ["quarterstaff", "dagger"]),
            choose(1, ["component pouch", "arcane focus"]),
            choose(1, ["scholar's pack", "explorer's pack"]),
            "spellbook"
        ]


class Druid:
    def __init__(self, level, strength, dexterity, constitution, intelligence, wisdom, charisma):
        self.level = level
        self.strength = strength
        self.dexterity = dexterity
        self.constitution = constitution
        self.intelligence = intelligence
        self.wisdom = wisdom
        self.charisma = charisma
        self.hit_die = 8
        self.hit_points = 8 + self.modifier(self.constitution)
        self.armor_proficiencies = ["light armor", "medium armor"]
        self.weapon_proficiencies = ["clubs", "darts", "javelins", "maces", "quarterstaffs", "scimitars", "sickles",
                                     "slings", "spears"]
        self.tool_proficiencies = ["herbalism kit"]
        self.saving_throw_proficiencies = ["intelligence", "wisdom"]
        self.skill_proficiencies = ["perception", "survival"]
        self.equipment = []

    def modifier(self, ability_score):
        return (ability_score - 10) // 2

    def __str__(self):
        return f"Druid (Level {self.level})"

class Cleric:
    def __init__(self, level, wisdom_mod):
        self.level = level
        self.hit_dice = 8
        self.max_hp = self.hit_dice + (self.level - 1) * (random.randint(1, self.hit_dice) + wisdom_mod)
        self.current_hp = self.max_hp
        self.proficiencies = {
            "armor": ["light", "medium", "shield"],
            "weapons": ["simple"],
            "tools": [],
            "saving_throws": ["wisdom", "charisma"],
            "skills": ["history", "medicine", "insight", "religion", "persuasion"]
        }
        self.equipment = {
            "weapon": ["mace", "warhammer"][random.randint(0, 1)],
            "armor": ["scale_mail", "leather_armor", "chain_mail"][random.randint(0, 2)],
            "shield": True,
            "ranged_weapon": ["light_crossbow", "simple_weapon"][random.randint(0, 1)],
            "quiver": 20,
            "pack": ["priest_pack", "explorer_pack"][random.randint(0, 1)],
            "holy_symbol": True
        }
        cleric = Cleric(3, 3)
        print(cleric.max_hp)  # output: 24
        print(cleric.proficiencies["armor"])  # output: ['light', 'medium', 'shield']
        print(cleric.equipment["weapon"])  # output: 'warhammer'
class Artificer:
    def __init__(self, level, ability_scores):
        self.level = level
        self.hit_dice = "1d8"
        self.hit_points = 8 + ability_scores["Constitution"]
        self.proficiencies = {
            "armor": ["light", "medium", "shields"],
            "weapons": ["simple"],
            "tools": ["thieves' tools", "tinker's tools", "one type of artisan's tools"],
            "saving_throws": ["Constitution", "Intelligence"],
            "skills": ["Perception", "History", "Sleight of Hand", "Arcana", "Medicine", "Nature", "Investigation"]
        }
        self.equipment = {
            "weapons": ["simple melee weapon", "simple ranged weapon"],
            "armor": ["leather armor", "scale mail armor"],
            "tools": ["thieves' tools", "dungeoneer's pack"],
            "misc": ["10 gold pieces"]
        }

        for i in range(2, self.level+1):
            self.hit_points += max(1, int((1/2)*self.hit_dice[0]) + ability_scores["Constitution"])
            self.hit_dice = f"{i}d8"

        if "firearms proficiency" in self.proficiencies["tools"]:
            self.proficiencies["weapons"].append("firearms")

    def __str__(self):
        return f"Artificer (Level {self.level})"

class Warlock:
    def __init__(self, level, ability_scores):
        self.level = level
        self.hit_dice = "1d8"
        self.hit_points = 8 + ability_scores["Constitution"]
        self.proficiencies = {
            "armor": ["light"],
            "weapons": ["simple"],
            "tools": [],
            "saving_throws": ["Wisdom", "Charisma"],
            "skills": ["Choose two skills from Intimidation, History, Arcana, Deception, Nature, Investigation, or Religion"]
        }
        self.equipment = {
            "weapons": ["a light crossbow and 20 bolts", "any simple weapon"],
            "armor": ["leather armor"],
            "tools": ["a component pouch or a arcane focus"],
            "misc": ["a scholar's pack or a dungeoneer's pack"]
        }

        for i in range(2, self.level+1):
            self.hit_points += max(1, int((1/2)*self.hit_dice[0]) + ability_scores["Constitution"])
            self.hit_dice = f"{i}d8"

    def __str__(self):
        return f"Warlock (Level {self.level})"

