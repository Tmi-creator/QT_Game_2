from Hunter_Summons_warlock import Warlock
from Rogue_Paladin import Rogue, Paladin
from Shaman_Druid_Priest import Druid, Priest
from Warrior_Mage import Warrior, Mage

units = {
    1: Warrior,
    2: Mage,
    3: Rogue,
    4: Paladin,
    # 5: Hunter,
    6: Warlock,
    # 7: Shaman,
    8: Druid,
    9: Priest

}


def pvp_all(list_all):
    p = {}
    number_all = sum(list_all)
    teams = []
    print(
        "Воин-1\nМаг-2\nРазбойник-3\nПаладин-4\nОхотник-5\nЧернокнижник-6\nШаман-7\nДруид-8\nЖрец-9\n")
    for i in range(number_all):
        choice1 = int(input())
        while choice1 not in units:
            print("Incorrect choice.")
            choice1 = int(input())
        p[i + 1] = units[choice1]()
    cnt = 1
    for i in range(len(list_all)):
        a = []
        for i2 in range(list_all[i]):
            a.append(p[cnt])
            cnt += 1
        teams.append(a)
    choice = True
    alive = [True] * len(teams)
    team_alive = 0
    print(teams)
    while choice:
        cnt = 0
        for i in range(1, 1 + len(teams)):
            print(f'team {i} : ', end='')
            for k in range(1, 1 + len(teams[i - 1])):
                print(
                    f'{k} - {teams[i - 1][k - 1].hp}hp, '
                    f'{teams[i - 1][k - 1].mana}mana, {teams[i - 1][k - 1].cur_atk}atk ',
                    end="")
            print()
        print("1 - обычная атака,\n2 - использование 1 способности,\n3 - использование второй "
              "способности, и\n4 - использование 3 способности")
        for i in range(len(p)):
            p1 = p[i + 1]
            if p1.hp > 0:
                choice = int(input(f'p{i + 1} turn, choose atk: '))
                while choice not in p1.skills:
                    print("Incorrect choice.")
                    choice = int(input())
                choice_n = int(input("А теперь выберите цель: "))
                while choice_n not in p or p[choice_n].hp <= 0:
                    print("Incorrect choice.")
                    choice_n = int(input())
                p1.skills[choice](p[choice_n])
        for i in range(len(teams)):
            if alive[i]:
                for j in range(len(teams[i])):
                    alive[i] = False
                    if teams[i][j].hp > 0:
                        alive[i] = True
                        break
            if alive[i]:
                team_alive = i
                cnt += 1
        if cnt == 1:
            choice = False
            print(f'team {team_alive + 1} wins! gg all!')
        if cnt == 0:
            choice = False
            print("That's a draw! Good game!")
