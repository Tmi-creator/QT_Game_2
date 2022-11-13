from random import randint

from Unit import Unit


class Warrior(Unit):  # armor dd
    def __init__(self):
        super().__init__(name="Warrior", hp=300, atk=30, mana=60, manacost_first=0, manacost_second=20,
                         manacost_third=60, range=1.5, move=92, first_skill_num=15,
                         second_skill_num=20, third_skill_num=990, description_of_atk='atk, deals 30 damage',
                         description_of_first='armor 15, this is simple atk', description_of_second='self.atk += 20',
                         description_of_third='atk', picture_atk='img/Warrior.png',
                         picture_first='img/armor.png', picture_second='img/clean_sword.png',
                         picture_third='img/ultra_attack.png', immortal=0)

    def first_skill(self, target):
        self.attack(target)

    def take_damage(self, dmg):
        if dmg > self.first_skill_num:
            self.hp -= dmg - self.first_skill_num

    def second_skill(self, target):
        self.atk += self.second_skill_num

    def third_skill(self, target):
        target.take_damage(self.third_skill_num)

    def make_it_good(self):
        self.descriptions[1] = f'atk, deals {self.atk} damage'
        self.descriptions[2] = f'armor {self.first_skill_num}, this is simple atk'
        self.descriptions[3] = f'self.atk += {self.second_skill_num}, costs {self.manacost_second} mana'
        self.descriptions[4] = f'atk, deals {self.third_skill_num} damage, costs {self.manacost_third} mana'


class Mage(Unit):  # super dd
    def __init__(self):
        super().__init__(name="Mage", hp=150, atk=40, mana=120, range=3, move=2, manacost_first=20, manacost_second=50,
                         manacost_third=10, first_skill_num=200, second_skill_num=5, third_skill_num=20,
                         description_of_atk='atk, deals 40 damage', description_of_first='1d4 to deal 200 damage',
                         description_of_second='give 4 turns immortal', description_of_third='+20 mana to target',
                         picture_atk='img/Mage.png', picture_first='img/magic_rain.png',
                         picture_second='img/immortal.png', picture_third='img/mana_up.png', immortal=0)

    def first_skill(self, target):
        target.take_damage(self.first_skill_num * randint(0, 1) * randint(0, 1))

    def second_skill(self, target):
        target.immortal += self.second_skill_num

    def third_skill(self, target):
        target.mana += self.third_skill_num

    def make_it_good(self):
        self.descriptions[1] = f'atk, deals {self.atk} damage'
        self.descriptions[2] = f'1d4 to deal {self.first_skill_num} damage, costs {self.manacost_first} mana'
        self.descriptions[3] = f'give {self.second_skill_num} turns immortal, costs {self.manacost_second} mana'
        self.descriptions[4] = f'+{self.third_skill_num} mana to target, costs {self.manacost_third} mana'
