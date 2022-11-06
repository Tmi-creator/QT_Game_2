from random import randint
from Unit import Unit


class Rogue(Unit):
    def __init__(self):
        super().__init__(hp=50, atk=60, mana=50, first_skill_num=75, second_skill_num=50, third_skill_num=10,
                         description_of_atk=f'atk, deals {self.atk} damage',
                         description_of_first='', description_of_second='', description_of_third='', picture_atk='',
                         picture_first='', picture_second='', picture_third='')

    # self.hp = 50
    # self.atk = 60
    # self.mana = 50
    # self.first_skill_num = 75
    # self.second_skill_num = 50
    # self.third_skill_num = 10

    def take_damage(self, dmg):
        if randint(1, 100) > self.first_skill_num:
            self.hp -= dmg
        else:
            print('Dodged:)')

    def take_damaged(self, dmg):
        if randint(1, 100) > self.first_skill_num // 3:
            self.hp -= dmg
        else:
            print('Dodged :)')

    def second_skill(self, target):
        # def blades_of_death():
        if self.mana >= 10:
            if randint(1, 100) > self.second_skill_num:
                self.attack(target)
                self.attack(target)
            else:
                self.attack(target)
            self.mana -= 10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)

    def third_skill(self, target):
        # def no_weapon():
        if self.mana >= 10:
            target.cur_atk -= randint(1, self.third_skill_num)
            self.mana -= 10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)


class Paladin(Unit):  # armor healer
    def __init__(self):
        super().__init__(hp=150, atk=15, mana=75, first_skill_num=5, second_skill_num=40, third_skill_num=10,
                         description_of_atk=f'atk, deals {self.atk} damage',
                         description_of_first='', description_of_second='', description_of_third='', picture_atk='',
                         picture_first='', picture_second='', picture_third='')

    # self.hp = 150
    # self.atk = 15
    # self.mana = 75
    # self.first_skill_num = -5
    # self.second_skill_num = 40
    # self.third_skill_num = 10

    def first_skill(self, dmg):
        # def take_damage():
        if dmg >= self.first_skill_num:
            self.hp -= dmg - self.first_skill_num

    def second_skill(self, target):
        # def heal():
        if self.mana >= 10:
            target.hp += self.second_skill_num
            if (target.hp > target.max_hp):
                target.hp = target.max_hp
            self.mana -= 10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)

    def third_skill(self, target):
        # def help_of_god():
        if self.mana >= 30:
            target.first_skill_num += self.third_skill_num
            target.second_skill_num += self.third_skill_num
            self.mana -= 10 * 3
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)
