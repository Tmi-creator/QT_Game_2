from random import randint

from Unit import Unit


class Warrior(Unit):  # armor dd
    def __init__(self):
        super().__init__(name="Warrior", hp=300, atk=30, mana=60, manacost_first=0, manacost_second=20,
                         manacost_third=60, range=1.5, move=92, first_skill_num=15,
                         second_skill_num=20, third_skill_num=990, description_of_atk='atk, deals 20 damage',
                         description_of_first='armor 15, this is simple atk', description_of_second='self.atk += 20', description_of_third='', picture_atk='',
                         picture_first='', picture_second='', picture_third='', immortal=0)

    def first_skill(self, target):
        self.attack(target)

    def take_damage(self, dmg):
        if dmg > self.first_skill_num:
            self.hp -= dmg - self.first_skill_num

    def second_skill(self, target):
        self.atk += self.second_skill_num

    def third_skill(self, target):
        target.take_damage(self.third_skill_num + self.atk * 0.5)


class Mage(Unit):  # super dd
    def __init__(self):
        super().__init__(name="Mage", hp=150, atk=40, mana=120, range=3, move=2, manacost_first=20, manacost_second=50,
                         manacost_third=10, first_skill_num=200, second_skill_num=2, third_skill_num=20,
                         description_of_atk='atk, deals 40 damage', description_of_first='1d4 to deal 200 damage',
                         description_of_second='give 2 turns immortal', description_of_third='+20 mana to target',
                         picture_atk='img/Mage.png', picture_first='img/Mage.png',
                         picture_second='img/Mage.png', picture_third='img/Mage.png')

    def first_skill(self, target):
        target.take_damage(self.first_skill_num * randint(0, 1) * randint(0, 1))

    def second_skill(self, target):
        target.immortal += self.second_skill_num

    def third_skill(self, target):
        target.mana += self.third_skill_num
