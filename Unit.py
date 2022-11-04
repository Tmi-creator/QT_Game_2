class Unit(object):
    def __init__(self, name, hp, atk, mana, range, move, first_skill_num, second_skill_num, third_skill_num):
        self.name = name
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.cur_atk = atk
        self.mana = mana
        self.range = range
        self.move = move
        self.first_skill_num = first_skill_num
        self.second_skill_num = second_skill_num
        self.third_skill_num = third_skill_num
        self.skills = {
            1: self.attack,
            2: self.first_skill,
            3: self.second_skill,
            4: self.third_skill
        }

    def take_damage(self, dmg):
        self.hp -= dmg

    def attack(self, target):
        target.take_damage(self.atk)

    def first_skill(self, target):
        raise Exception("Override me")

    def second_skill(self, target):
        raise Exception("Override me")

    def third_skill(self, target):
        raise Exception("Override me")
