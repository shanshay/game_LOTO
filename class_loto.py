import random
import sys
from termcolor import colored


class Gamer:

    def __init__(self, name, count, test):
        self.name = name
        self.count = 0
        self.new_card = []
        self.test = False

    def create_card(self):  # функция которая создает индивидуальную карточку
        nums = random.sample(range(1, 91), 15)
        list_of_cards = [sorted(nums[0:5]), sorted(nums[5:10]), sorted(nums[10:15])]
        for i in list_of_cards:
            j = 0
            place_numeric = random.sample(range(0, 10), 10)
            for place in place_numeric:
                if place > 5:
                    i.insert(j, 0)
                    j = j + 1
                else:
                    j = j + 1
        for i in list_of_cards:
            for j in i:
                self.new_card.append(j)
        return self.new_card

    def print_cards(self):  # распечатка карты без запятых и скобочек
        # вызывать только 1 раз в начале игры
        print(colored(f"{self.name}s card: ", 'red'))
        temp_list = [self.new_card[0:9], self.new_card[9:18], self.new_card[18:27]]
        print('--------------------------')
        for i in temp_list:
            line_str = ''
            for num in i:
                if num == 0:
                    line_str = f'{line_str} '
                elif num > 10:
                    line_str = f'{line_str} {num} '
                else:
                    line_str = f'{line_str}{num} '
            print(line_str.rstrip())
        print('--------------------------')

    def print_using_cards(self):  # вывести на экран измененную карту во время игры
        # вызывать только эту функцию во время игры
        print(colored(f"{self.name}s card: ", 'red'))
        temp_list = [self.new_card[0:9], self.new_card[9:18], self.new_card[18:27]]
        print('--------------------------')
        for i in temp_list:
            line_str = ''
            for num in i:
                if num == 0:
                    line_str = f'{line_str} '
                elif num == 95:
                    line_str = f'{line_str} - '
                elif num > 10:
                    line_str = f'{line_str} {num} '
                else:
                    line_str = f'{line_str}{num} '
            print(line_str.rstrip())
        print('--------------------------')

    def check_num_in_card(self, step):
        for i in range(len(self.new_card)):
            if step == self.new_card[i]:
                self.new_card[i] = 95
                self.count = self.count + 1
                self.test = True
            else:
                test = False
        return self.new_card, self.test, self.count

    def check_count(self):
        if self.count >= 15:
            print(f'Игра окончена! {self.name} выиграл! У {self.name} все цифры зачеркнуты!')
            sys.exit()

    def computer_plays(self, step):
        for i in range(len(self.new_card)):
            if step == self.new_card[i]:
                self.new_card[i] = 95
                self.count = self.count + 1
                self.test = True
            # else:
            #     test = False
        return self.new_card, self.test, self.count


class Leading:

    def __init__(self):
        self.step = 0
        self.barrel = random.sample(range(1, 91), 90)

    def show_barrel(self):  # показать номер бочонка
        self.step = self.barrel[0]
        print(colored(f'Бочонок № {self.step}','blue'))
        del (self.barrel[0])
        print(colored(f'Осталось бочонков {len(self.barrel)}', 'yellow'))
        return self.barrel, self.step
