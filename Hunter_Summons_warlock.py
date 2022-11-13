from Unit import Unit


class Hunter(Unit):
    def __init__(self):
        super().__init__(name='Hunter', range=3, move=2, manacost_first=0, manacost_second=0, manacost_third=30,
                         hp=100, atk=20, mana=60, first_skill_num=30, second_skill_num=20, third_skill_num=40,
                         description_of_atk=f'atk, deals 20 damage',
                         description_of_first='', description_of_second='', description_of_third='',
                         picture_atk='img/Hunter.png', picture_first='img/one_arrow.png',
                         picture_second='img/two_arrows.png', picture_third='img/three_arrows.png', immortal=0)

    def attack(self, target):
        target.take_damage(self.atk)
        if target.hp <= 0:
            self.first_skill(target)

    def first_skill(self, target):
        self.mana += self.first_skill_num

    def second_skill(self, target):
        self.atk += self.second_skill_num
        self.hp -= self.second_skill_num * 2

    def third_skill(self, target):
        target.hp -= self.third_skill_num
        if target.hp <= 0:
            self.first_skill(target)
        self.hp += self.third_skill_num

    def make_it_good(self):
        self.descriptions[1] = f'atk, deals {self.atk} damage'
        self.descriptions[2] = f"passive, when kill unit mana+={self.first_skill_num},\nit's simple atk"
        self.descriptions[3] = f'self.atk+={self.second_skill_num}, costs {self.second_skill_num * 2} hp'
        self.descriptions[4] = f'atk, deals {self.third_skill_num}, self.hp+={self.third_skill_num}'


class Warlock(Unit):
    def __init__(self):
        super().__init__(name='Warlock', range=3, move=2, manacost_first=0, manacost_second=0, manacost_third=30,
                         hp=100, atk=20, mana=60, first_skill_num=30, second_skill_num=20, third_skill_num=40,
                         description_of_atk=f'atk, deals 20 damage',
                         description_of_first='', description_of_second='', description_of_third='',
                         picture_atk='img/Warlock.png', picture_first='img/death_mana.png',
                         picture_second='img/hp_into_atk.png', picture_third='img/take_hp.png', immortal=0)

    def attack(self, target):
        target.take_damage(self.atk)
        if target.hp <= 0:
            self.first_skill(target)

    def first_skill(self, target):
        self.mana += self.first_skill_num

    def second_skill(self, target):
        self.atk += self.second_skill_num
        self.hp -= self.second_skill_num * 2

    def third_skill(self, target):
        target.hp -= self.third_skill_num
        if target.hp <= 0:
            self.first_skill(target)
        self.hp += self.third_skill_num

    def make_it_good(self):
        self.descriptions[1] = f'atk, deals {self.atk} damage'
        self.descriptions[2] = f"passive, when kill unit mana+={self.first_skill_num},\nit's simple atk"
        self.descriptions[3] = f'self.atk+={self.second_skill_num}, costs {self.second_skill_num * 2} hp'
        self.descriptions[4] = f'atk, deals {self.third_skill_num}, self.hp+={self.third_skill_num}'
