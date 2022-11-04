from random import randint

from pvp_all import pvp_all

words = {
    1: "Да будет Бой! Что же у нас по героям?",
    2: "Выбирайте персонажей на величайшую битву!",
    3: 'Ну, да начнется бой!',
    4: 'Это будет схваткой тысячелетия!'
}

choice_end = True
while choice_end:
    print("Приветствую тебя, странник! Если желаешь сыграть в пвп, жми 1, если против ИИ - 2.")
    choice1 = int(input())
    if choice1 == 1:
        print(words[randint(1, 4)])
        pvp_all(list(map(int, input('Введите количество человек в каждой команде: ').split())))
    elif choice1 == 2:
        pass
    else:
        print('Incorrect choice')
    if int(input('if you want to close\end press 0: ')) == 0:
        choice_end = False
print('Bye!')
