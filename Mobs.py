class Enemy(object):
    def __init__(self, hp, atk, provocation, windpower, level):
        self.hp = hp
        self.max_hp = hp
        self.atk = atk
        self.cur_atk = atk
        self.provocation = provocation
        self.windpower = windpower
        self.level = level

    def take_damage(self, dmg):
        self.hp -= dmg

    def attack(self, target):
        for _ in range(self.windpower):
            target.take_damage(self.atk)


class SkeletW(object):
    def __init__(self):
        super().__init__(hp=75, atk=10, provocation=5, windpower=1, level=1)

    def lvl_up(self):
        if self.level % 3 == 0:
            self.windpower += 1
