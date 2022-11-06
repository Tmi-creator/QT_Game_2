from random import randint

from Unit import Unit


class Warrior(Unit):  # armor dd
    def __init__(self):
        super().__init__(name="Warrior", hp=200, atk=20, mana=50, range=1.5, move=92, first_skill_num=10,
                         second_skill_num=40, third_skill_num=990, description_of_atk=f'atk, deals 20 damage',
                         description_of_first='', description_of_second='', description_of_third='', picture_atk='',
                         picture_first='', picture_second='', picture_third='')
        # self.hp = 200
        # self.atk = 20
        # self.mana = 50
        # self.first_skill_num = -10
        # self.second_skill_num = 40
        # self.third_skill_num = 15

    def first_skill(self, target):
        self.attack(target)

    def take_damage(self, dmg):
        if dmg >= self.first_skill_num:
            self.hp -= dmg - self.first_skill_num

    def second_skill(self, target):
        if self.mana >= 10:
            target.take_damage(self.second_skill_num + self.atk * 0.5)
            self.mana -= 10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)

    def third_skill(self, target):
        # def throw_sword():
        if self.mana >= 10:
            target.take_damage(self.third_skill_num + self.atk * 0.5)
            self.atk -= 10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)


class Mage(Unit):  # super dd
    def __init__(self):
        super().__init__(name="Mage", hp=100, atk=40, mana=100, range=3, move=2, first_skill_num=2048,
                         second_skill_num=10, third_skill_num=15, description_of_atk=f'atk, deals 40 damage',
                         description_of_first='', description_of_second='', description_of_third='', picture_atk='',
                         picture_first='', picture_second='', picture_third='')

    # self.hp = 100
    # self.atk = 40
    # self.mana = 100
    # self.first_skill_num = 2048
    # self.second_skill_num = 10
    # self.third_skill_num = 15

    def first_skill(self, target):
        # def total_annihilation():
        if self.mana >= 10:
            target.take_damage(
                self.first_skill_num * randint(0, 1) * randint(0, 1) * randint(0, 1) * randint(0, 1))
            self.mana -= 10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)

    def second_skill(self, target):
        # def buff():
        if self.mana >= 10:
            target.atk += self.second_skill_num
            self.mana -= 10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)

    def third_skill(self, target):
        # def mana_up():
        if self.mana >= 10:
            target.mana += self.third_skill_num
            self.mana -= 10
        else:
            print('No mana!')
            target.take_damage(self.atk * 0.5)
