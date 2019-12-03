from class_loto import Gamer
from class_loto import Leading
import sys
import random


while True:
    print('Кто будет играть? Игрок и компьютер, 2 игрока или 2 компьютера?')
    print('1. Игрок и компьютер')
    print('2. Два игрока')
    print('3. Два компьютера')
    print('4.Никто не будет играть. Я передумал(а)')
    choice = input('Выберите пункт меню: ')
    if choice == '1':
        name_of_gamer = input('Введите имя игрока ')
        gamer = Gamer(name_of_gamer, 0, False)
        name_of_computer = ['Амбрелла', 'Фокс', 'Скайнет', 'Людвиг', 'Белоснежка и семь гномов', 'Ганкер', 'Терминатор Т1000', 'Робокоп']
        name_of_computer = random.sample(name_of_computer, 1)
        print(f'Имя компьютера {name_of_computer[0]}')
        computer = Gamer(name_of_computer, 0, False)
        gamer.create_card()
        gamer.print_cards()
        computer.create_card()
        computer.print_cards()
        barrel_in_game = Leading()
        while True:
            gamer.check_count()
            computer.check_count()
            barrel_in_game.show_barrel()
            gamer.check_num_in_card(barrel_in_game.step)
            reply = input('Зачеркнуть цифру? да/нет/выход (д/н/в)')
            while reply not in ['д', 'н', 'в']:
                print("Неверный ввод")
                reply = input('Зачеркнуть цифру? да/нет/выход (д/н/в)')
            if reply == 'в':
                print('Вы вышли из игры. Вы так и не выиграли.')
                print('Информация по игре:')
                print(f'Компьютер набрал {computer.count} очков')
                print(f'Вы набрали {gamer.count} очков')
                sys.exit()
            elif reply == 'д':
                if gamer.test:
                    gamer.print_using_cards()
                    gamer.test = False
                else:
                    print('Плохой выбор. Игра окончена!!!')
                    print('Информация по игре:')
                    print(f'Компьютер набрал {computer.count} очков')
                    print(f'Вы набрали {gamer.count} очков')
                    sys.exit()
            elif reply == 'н':
                if gamer.test:
                    print('Плохой выбор. Игра окончена!!!')
                    print('Информация по игре:')
                    print(f'Компьютер набрал {computer.count} очков')
                    print(f'Вы набрали {gamer.count} очков')
                    sys.exit()
                else:
                    gamer.print_using_cards()
                    gamer.test = False

            computer.check_num_in_card(barrel_in_game.step)
            computer.print_using_cards()

    elif choice == '2':
        name_of_gamer_01 = input('Введите имя игрока ')
        gamer_01 = Gamer(name_of_gamer_01, 0, False)
        name_of_gamer_02 = input('Введите имя игрока ')
        gamer_02 = Gamer(name_of_gamer_02, 0, False)
        gamer_01.create_card()
        gamer_01.print_cards()
        gamer_02.create_card()
        gamer_02.print_cards()
        barrel_in_game = Leading()
        while True:
            gamer_01.check_count()
            gamer_02.check_count()
            barrel_in_game.show_barrel()
            gamer_01.check_num_in_card(barrel_in_game.step)
            reply = input('Зачеркнуть цифру? да/нет/выход (д/н/в)')
            while reply not in ['д', 'н', 'в']:
                print("Неверный ввод")
                reply = input('Зачеркнуть цифру? да/нет/выход (д/н/в)')
            if reply == 'в':
                print(f'Игрок {gamer_01.name} вышел из игры. Выиграл {gamer_02.name}')
                print('Информация по игре:')
                print(f'{gamer_02.name} набрал {gamer_02.count} очков')
                print(f'{gamer_01.name}] набрал {gamer_01.count} очков')
                sys.exit()
            elif reply == 'д':
                if gamer_01.test:
                    gamer_01.print_using_cards()
                    gamer_01.test = False
                else:
                    print(f'Плохой выбор. Выиграл {gamer_02.name} Игра окончена!!!')
                    print('Информация по игре:')
                    print(f'{gamer_02.name} набрал {gamer_02.count} очков')
                    print(f'{gamer_01.name} набрал {gamer_01.count} очков')
                    sys.exit()
            elif reply == 'н':
                if gamer_01.test:
                    print(f'Плохой выбор. Выиграл {gamer_01.name} Игра окончена!!!')
                    print('Информация по игре:')
                    print(f'Игрок {gamer_01.name} набрал {gamer_01.count} очков')
                    print(f'{gamer_02.name} набрал {gamer_02.count} очков')
                    sys.exit()
                else:
                    gamer_02.print_using_cards()
                    gamer_01.test = False
            else:
                print('Неверный ввод')
            reply = input('Зачеркнуть цифру? да/нет/выход (д/н/в)')
            while reply not in ['д', 'н', 'в']:
                print("Неверный ввод")
                reply = input('Зачеркнуть цифру? да/нет/выход (д/н/в)')
            if reply == 'в':
                print(f'Игрок {gamer_02.name} вышел из игры. Выиграл {gamer_01.name}')
                print('Информация по игре:')
                print(f'{gamer_01.name} набрал {gamer_01.count} очков')
                print(f'{gamer_02.name}] набрал {gamer_02.count} очков')
                sys.exit()
            elif reply == 'д':
                if gamer_02.test:
                    gamer_02.print_using_cards()
                    gamer_02.test = False
                else:
                    print(f'Плохой выбор. Выиграл {gamer_01.name} Игра окончена!!!')
                    print('Информация по игре:')
                    print(f'{gamer_01.name} набрал {gamer_01.count} очков')
                    print(f'{gamer_02.name} набрал {gamer_02.count} очков')
                    sys.exit()
            elif reply == 'н':
                if gamer_02.test:
                    print(f'Плохой выбор. Выиграл {gamer_01.name} Игра окончена!!!')
                    print('Информация по игре:')
                    print(f'Игрок {gamer_01.name} набрал {gamer_01.count} очков')
                    print(f'{gamer_02.name} набрал {gamer_02.count} очков')
                    sys.exit()
                else:
                    gamer_02.print_using_cards()
                    gamer_02.test = False
            else:
                print('Неверный ввод')

    elif choice == '3':
        name_of_computer_01 = ['Амбрелла', 'Фокс', 'Скайнет', 'Людвиг', 'Белоснежка и семь гномов', 'Ганкер',
                               'Терминатор Т1000', 'Робокоп']
        name_of_computer_01 = random.sample(name_of_computer_01, 1)
        print(f'Имя компьютера {name_of_computer_01[0]}')
        computer_01 = Gamer(name_of_computer_01, 0, False)
        name_of_computer_02 = ['Амбрелла', 'Фокс', 'Скайнет', 'Людвиг', 'Белоснежка и семь гномов', 'Ганкер',
                               'Терминатор Т1000', 'Робокоп']
        name_of_computer_02 = random.sample(name_of_computer_02, 1)
        print(f'Имя компьютера {name_of_computer_02[0]}')
        computer_02 = Gamer(name_of_computer_02, 0, False)
        computer_01.create_card()
        computer_01.print_cards()
        computer_02.create_card()
        computer_02.print_cards()
        barrel_in_game = Leading()
        while True:
            computer_01.check_count()
            computer_02.check_count()
            barrel_in_game.show_barrel()
            computer_01.check_num_in_card(barrel_in_game.step)
            computer_02.check_num_in_card(barrel_in_game.step)
            computer_01.print_using_cards()
            computer_02.print_using_cards()

    elif choice == '4':
        sys.exit()

    else:
        print('Неверный ввод. Нужно ввести 1, 2, 3 или 4. Подумайте хорошенько и выберите еще раз')