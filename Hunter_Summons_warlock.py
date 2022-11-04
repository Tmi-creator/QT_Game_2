from Unit import Unit


# class Hunter(Unit):  # summoner sniper (chto ya delayu voobche)
#     pass


# class Hunter_summons(Unit):
#     pass


class Warlock(Unit):  # мазохист dd (Много, очень очень много) (can heal himself)
    def __init__(self):
        super().__init__(hp=150, atk=20, mana=200, first_skill_num=1.1, second_skill_num=20, third_skill_num=30)

    # self.hp = 150
    # self.atk = 20
    # self.mana = 200
    # elf.first_skill_num = 1.1
    # self.second_skill_num = 20
    # self.third_skill_num = 30

    def first_skill(self, target):
        # def suicide_mission():
        if self.hp > 1 and self.mana >= 10:
            ch = int(input("Введите кол-во атаки на хп"))
            if ch > self.hp:
                target.hp -= self.hp * self.first_skill_num
                self.hp -= self.hp-1
            else:
                target.hp -= ch * self.first_skill_num
                self.hp -= ch
        else:
            print("No mana!")
            target.attack(0.5 * self.cur_atk)


def second_skill(self, target):
    # def masochism():
    if self.hp > 20 and self.mana >= 10:
        target.take_damage(20 + self.second_skill_num)
        self.hp -= 20
    else:
        print("no hp/mana")
        target.attack(0.5 * self.cur_atk)


def third_skill(self, target):
    # def take_hp():
    if self.mana >= 20:
        target.hp -= self.third_skill_num
        self.hp += self.third_skill_num - 10
        self.mana -= 20
    else:
        print("No mana!")
        target.attack(0.5 * self.cur_atk)
