from Unit import Unit


# class Hunter(Unit):  # summoner sniper (chto ya delayu voobche)
#     pass


class Warlock(Unit):
    def __init__(self):
        super().__init__(hp=100, atk=20, mana=60, first_skill_num=30, second_skill_num=20, third_skill_num=40,
                         description_of_atk=f'atk, deals 20 damage',
                         description_of_first='', description_of_second='', description_of_third='', picture_atk='',
                         picture_first='', picture_second='', picture_third='')

    def first_skill(self, target):
        self.mana += self.first_skill_num


    def second_skill(self, target):
        self.atk += self.second_skill_num
        self.hp -= self.second_skill_num * 2


    def third_skill(self, target):
        target.hp -= self.third_skill_num
        self.hp += self.third_skill_num
