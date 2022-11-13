from random import randint

from Unit import Unit


class Rogue(Unit):
    def __init__(self):
        super().__init__(name='Rogue', hp=100, atk=60, mana=50, first_skill_num=50, range=1.5, move=3,
                         second_skill_num=60, third_skill_num=20,
                         manacost_first=0, manacost_second=15, manacost_third=15,
                         description_of_atk='atk, deals 60 damage',
                         description_of_first='dodge atk with 50% chance, -5mana;\nThis is simple atk',
                         description_of_second='double atk with 60% chance', description_of_third='target.atk-=1d20',
                         picture_atk='img/Rogue.png',
                         picture_first='img/Blink.png', picture_second='img/double_atk.png',
                         picture_third='img/decrease_damage.png', immortal=0)

    def first_skill(self, target):
        self.attack(target)

    def take_damage(self, dmg):
        if self.mana > 5:
            if randint(1, 100) > self.first_skill_num:
                self.hp -= dmg
            self.mana -= 5
        else:
            self.take_damaged(dmg)

    def take_damaged(self, dmg):
        if randint(1, 100) > self.first_skill_num // 5:
            self.hp -= dmg

    def second_skill(self, target):
        if randint(1, 100) > self.second_skill_num:
            self.attack(target)
            self.attack(target)
        else:
            self.attack(target)

    def third_skill(self, target):
        target.cur_atk -= randint(1, self.third_skill_num)

    def make_it_good(self):
        self.descriptions[1] = f'atk, deals {self.atk} damage'
        self.descriptions[
            2] = f'dodge atk with {self.first_skill_num}% chance,cost {self.manacost_first};\nThis is simple atk'
        self.descriptions[
            3] = f'double atk with {self.second_skill_num}% chance,\ncosts {self.manacost_second + 5} mana'
        self.descriptions[4] = f'target.atk-=1d{self.third_skill_num}, costs {self.manacost_third} mana'


class Paladin(Unit):  # armor healer
    def __init__(self):
        super().__init__(name='Paladin', range=1.5, move=2, hp=400, atk=15, mana=75, first_skill_num=10,
                         second_skill_num=40, third_skill_num=10,
                         manacost_first=0, manacost_second=15, manacost_third=30,
                         description_of_atk='atk, deals 15 damage', description_of_first='armor 10, this is simple atk',
                         description_of_second='heal to 40hp',
                         description_of_third='first and second skills += 10', picture_atk='img/Paladin.png',
                         picture_first='img/armor.png', picture_second='img/paladin_heal.png',
                         picture_third='img/god_light.png', immortal=0)

    def first_skill(self, dmg):
        if dmg > self.first_skill_num:
            self.hp -= dmg - self.first_skill_num

    def second_skill(self, target):
        target.hp += self.second_skill_num
        if target.hp > target.max_hp:
            target.hp = target.max_hp

    def third_skill(self, target):
        target.first_skill_num += self.third_skill_num
        target.second_skill_num += self.third_skill_num

    def make_it_good(self):
        self.descriptions[1] = f'atk, deals {self.atk} damage'
        self.descriptions[2] = f'armor {self.first_skill_num}, this is simple atk'
        self.descriptions[3] = f'heal +{self.second_skill_num}hp to target,\ncosts {self.manacost_second} mana'
        self.descriptions[
            4] = f'target.first and second skill+={self.third_skill_num},\ncosts {self.manacost_third} mana'
