'''Насколько я понял суть урока, переход от использования массивов к другим структурам данных снижает вероятность ошибок. Поскольку непосредственно с array  я не работал, рассмотрим возможность замены списков на хэш-таблицы. 
 В качестве варианта попробую рассмотреть,  замену списков в представленных методах на хэш-функции или двунаправленные списки.'''

# https://github.com/NikLaz25/Game-Loto/blob/master/8.result.py

'''Правила игры в лото.
Игра ведется с помощью спе циальных карточек, на которых отмечены числа,
и фишек (бочонков) с цифрами.
Количество бочонков — 90 штук (с цифрами от 1 до 90).
Каждая карточка содержит 3 строки по 9 клеток. В каждой строке по 5 случайных цифр,
расположенных по возрастанию. Все цифры в карточке уникальны. Пример карточки:
--------------------------
    9 43 62          74 90
 2    27    75 78    82
   41 56 63     76      86
--------------------------
В игре 2 игрока: пользователь и компьютер. Каждому в начале выдается
случайная карточка.
Каждый ход выбирается один случайный бочонок и выводится на экран.
Также выводятся карточка игрока и карточка компьютера.
Пользователю предлагается зачеркнуть цифру на карточке или продолжить.
Если игрок выбрал "зачеркнуть":
Если цифра есть на карточке - она зачеркивается и игра продолжается.
Если цифры на карточке нет - игрок проигрывает и игра завершается.
Если игрок выбрал "продолжить":
Если цифра есть на карточке - игрок проигрывает и игра завершается.
Если цифры на карточке нет - игра продолжается.
Побеждает тот, кто первый закроет все числа на своей карточке.'''

from random import randint

class Cards:
    def __init__(self, name, count_name):
        self.name = name
        self.count_name = count_name
        self.result = []
        self.finish = 0
        self.count = 0
    def creat_card(self):# метод создания карточки
        for x in range(3):
            n = 0
            a1 = randint(0, 2)
            a2 = randint(3, 4)
            a3 = randint(5, 6)
            a4 = randint(7, 8)
            for i in range(10):
                if i < 9 and i != a1 and i != a2 and i != a3 and i != a4:
                    self.result.append("%2.f" % randint(n, n + 18))
                    n += 18
                elif i == a1 or i == a2 or i == a3 or i == a4:
                    self.result.append('__')
        return self.result
    def save_card(self):#сохраняем карточку
        return self.result
    def change_card(self, number2):# зачеркиваем число,используем метод только при ответе "д"
        n=0
        for k, el in enumerate(self.result):
            if el == number2:
                self.result[k] = '><'
                print('\n', 'Такое число есть')
                n += 1
                self.count += 1
        if n == 0:
            print('\n', 'Ответ неверный')
            self.finish += 1
        return self.result
    def change_card2(self, number2):# используем метод, при ответе н
        n1 = 0
        for k, el in enumerate(self.result):
            if el == number2:
                n1 += 1
                print('\n', 'Ответ неверный')
                self.finish += 1
        if n1 == 0:
            print('\n', 'Действительно, такого числа в карточке нет')
    def check_comp_card(self, number2):#проверяем карточку компьютера
        for k, el in enumerate(self.result):
            if el == number2:
                self.result[k] = '><'
                print('\n', 'Такое число есть карточке компьютера')
                self.count += 1
        return self.result
    def print_card(self):# выводим карточку на экран
        result2 = [self.result[0:9], self.result[9:18], self.result[18:27]]
        print(f'---{self.name}----')
        print('\n'.join(' '.join(str(j) for j in line) for line in result2))
        print('--------------------------', '\n')
    def save_finish(self):
        return self.finish
    def save_count(self):#сохраняем и выводим значение счёта
        print(f'{self.count_name} {self.count}')
        return self.count

class Number:
    def __init__(self, max):
        self.max = max
        self.memory_nym = []
    def my_num(self):#Генерим новый бочонок
        nn = 0
        while nn == 0:
            self.number1 = "%2.f" % randint(0, self.max)
            if self.number1 in self.memory_nym:
                x = 1 #если число уже есть в списке, то проходим цикл заново. В этой строке ничего не происходит.
            else:
                nn = 1
                print('Выпал бочонок с числом: ', self.number1)
                print('Числа, которые уже выпадали:', self.memory_nym)
                print(f'Ранее выпадало {len(self.memory_nym)} знач. Ещё осталось {self.max - len(self.memory_nym)}')
                self.memory_nym.append(self.number1)
        return self.number1

    def save_num(self):#Сохраняем значение бочонка
        return str(self.number1)
class Game(Cards, Number):
    def __init__(self):
        return
    def question(self):#запрашиваем ответ
        self.answer = input('Зачеркиваем выпавшее число в карточке? д/н ')
        return self.answer
    def save_answer(self):#сохраняем ответ
        return self.answer


#создаём экземпляры 2х карточек
my_card = Cards('---Ваша карточка---', 'Ваш счёт:')
comp_card = Cards('-Карточка компьютера-', 'Счёт компьютера:')
#создаём экземпляр для бочонка
num1 = Number(90)
#экземпляр для класса Game
game1 = Game()

#Формирую карточки
my_card.creat_card()
comp_card.creat_card()
#Вывожу на экран информацию
my_card.print_card()
comp_card.print_card()
#ну и основной метод
def find():
    num1.my_num()#вывожу номер
    game1.question()#задаю вопрос
    if game1.save_answer() == 'д':
        my_card.change_card(num1.save_num())
    else:
        my_card.change_card2(num1.save_num())
    my_card.print_card()
    comp_card.check_comp_card(num1.save_num())
    comp_card.print_card()
#цикл для основного метода
while 1:
    find()
    if my_card.save_count() == 15:
        print('Вы победили')
        break
    elif my_card.save_finish() != 0:
        break
    elif comp_card.save_count() == 15:
        print('Победил компьютер')
        break
print('GAME OVER')
