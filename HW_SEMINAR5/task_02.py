# Создайте программу для игры с конфетами человек против человека.

# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга.
#  Первый ход определяется жеребьёвкой. За один ход можно забрать не более чем 28 конфет.
# Все конфеты оппонента достаются сделавшему последний ход. Сколько конфет нужно взять первому игроку,
# чтобы забрать все конфеты у своего конкурента?

# a) Добавьте игру против бота

# b) Подумайте как наделить бота "интеллектом"
import random

  

program = True
operator = {1: 'играть вдвоем',
            2: 'играть с ботом',
            3: 'игра с умным ботом',
            4: 'выход из игры'}
while program == True:
    for key, value in operator.items():
        print(f'{key} - {value}')
    userOperationText = int(input('введите № операции '))
        
    if userOperationText == 1:
        bonbons = 2021
        player1 = input('Пожалуйста, введите имя Первого игрока ')
        player2 = input('Пожалуйста, введите имя Второго игрока ')
        turn = player1

        if random.randint(1, 101) % 2 == 0:
            print(f'в жеребьевке победил {player1}, он ходит первым')
        else:
            print(f'в жеребьевке победил {player2}, он ходит первым')
            turn = player2
            wait = player1

        while bonbons >= 0:
            if bonbons == 0:
                print(f'игрок {turn} проиграл! поздравляем с победой {wait}! это была великая битва умов!')
                print()
                break
            if turn == player1:
                while True:
                    num = int(input(f'{turn}, есть {bonbons} конфет. ты можешь взять от 1 до 28 конфет, сколько возьмешь? '))
                    if 0 < num < 29:
                        bonbons -= num
                        turn = player2
                        wait = player1
                        break
                    else:
                        print('введено неверное число, попробуй снова {player1}!')
            if turn == player2:
                    while True:
                        num = int(input(f'{turn}, есть {bonbons} конфет. ты можешь взять от 1 до 28 конфет, сколько возьмешь? '))
                        if 0 < num < 29:
                            bonbons -= num
                            turn = player1
                            wait = player2
                            break
                        else:
                            print('введено неверное число, попробуй снова {player2}!')
    

    if userOperationText == 2:
        bonbons = 100
        player1 = input('Пожалуйста, введите имя Игрока ')
        player2 = 'bot'
        print(f'{player1}, против тебя будет играть  {player2}')
        turn = player1

        if random.randint(1, 101) % 2 == 0:
            print(f'в жеребьевке победил {player1}, он ходит первым')
        else:
            print(f'в жеребьевке победил {player2}, он ходит первым')
            turn = player2
            wait = player1

        while bonbons >= 0:
            if bonbons == 0:
                print(f'игрок {turn} проиграл! поздравляем с победой {wait}! это была великая битва умов!')
                print()
                break
            if turn == player1:
                while True:
                    num = int(input(f'{turn}, есть {bonbons} конфет. ты можешь взять от 1 до 28 конфет, сколько возьмешь? '))
                    if 0 < num < 29:
                        bonbons -= num
                        turn = player2
                        wait = player1
                        break
                    else:
                        print('введено неверное число, попробуй снова {player1}!')
            if turn == player2:
                    while True:
                        if bonbons <=28:
                            num = bonbons
                            print(f'{player2} взял {num} конфет')
                            bonbons -= num
                            turn = player1
                            wait = player2
                            break
                        else:
                            num = random.randint(1, 29)
                            print(f'{player2} взял {num} конфет')
                            bonbons -= num
                            turn = player1
                            wait = player2
                            break
    if userOperationText == 3:
        win_numbers = [x for x in range(29, 2021, 28)]
        bonbons = 100
        player1 = input('Пожалуйста, введите имя Игрока ')
        player2 = 'Mr.bot'
        print(f'{player1}, против тебя будет играть  {player2}')
        turn = player1

        if random.randint(1, 101) % 2 == 0:
            print(f'в жеребьевке победил {player1}, он ходит первым')
        else:
            print(f'в жеребьевке победил {player2}, он ходит первым')
            turn = player2
            wait = player1

        while bonbons >= 0:
            if bonbons == 0:
                print(f'игрок {turn} проиграл! поздравляем с победой {wait}! это была великая битва умов!')
                print()
                break
            if turn == player1:
                while True:
                    num = int(input(f'{turn}, есть {bonbons} конфет. ты можешь взять от 1 до 28 конфет, сколько возьмешь? '))
                    if 0 < num < 29:
                        bonbons -= num
                        turn = player2
                        wait = player1
                        break
                    else:
                        print('введено неверное число, попробуй снова {player1}!')
            if turn == player2:
                    while True:
                        if bonbons <=28:
                            num = bonbons
                            print(f'{player2} взял {num} конфет')
                            bonbons -= num
                            turn = player1
                            wait = player2
                            break
                        else:
                            win_numbers = [x for x in range(29, bonbons, 28)]
                            num = bonbons - win_numbers[-1]
                            print(f'{player2} взял {num} конфет')
                            bonbons -= num
                            turn = player1
                            wait = player2
                            break


    if userOperationText == 4:  
        program = False                        