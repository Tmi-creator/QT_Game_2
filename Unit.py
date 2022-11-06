class Unit(object):
    def __init__(self, name, hp, atk, mana, range, move, first_skill_num, second_skill_num, third_skill_num,
                 description_of_atk, description_of_first, description_of_second, description_of_third, picture_atk,
                 picture_first, picture_second, picture_third):
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
        self.description_of_first = description_of_first
        self.description_of_second = description_of_second
        self.description_of_third = description_of_third
        self.description_of_atk = description_of_atk
        self.picture_atk = picture_atk
        self.picture_first = picture_first
        self.picture_second = picture_second
        self.picture_third = picture_third
        self.skills = {
            1: self.attack,
            2: self.first_skill,
            3: self.second_skill,
            4: self.third_skill
        }
        self.descriptions = {
            1: self.description_of_atk,
            2: self.description_of_first,
            3: self.description_of_second,
            4: self.description_of_third
        }
        self.pictures = {
            1: self.picture_atk,
            2: self.picture_first,
            3: self.picture_second,
            4: self.picture_third
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
