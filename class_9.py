Предупредил возможность ошибки деления на 0
def step_doors(step, doors):
    '''метод цикл для каждого шага'''
    for i in range(k):
        try:
            if (i + 1) % step == 0 and doors[i] == 0:
                doors[i] = 1
            elif (i + 1) % step == 0 and doors[i] == 1:
                doors[i] = 0
        except:
            pass
    return doors

pp - TARGET_PAYBACK_PERIOD# использую константу, целевое значение периода окупаемости проекта
dpp - TARGET_DISCOUNT _PP#использую константу,  целевое значение дисконтированного периода окупаемости проекта
pi - TARGET_PI#использую константу,  целевое значение индекса прибыльности
x - is_in_list # более корректное название булевой переменной
flag - is_in_list # более корректное название булевой переменной
flag - number_is_four # более корректное название булевой переменной


- Избавляемся от магических чисел, используем константы 
'''если поменяли 2 буквы, то True'''
TWO_LETTERS = 2 # новая константа - две буквы
if len(i_list) == TWO_LETTERS: # if len(i_list) == 2:
    return True

- Избавляемся от магических чисел, используем константы 
'''если поменяли более 3х букв, и не по порядку то False'''
THREE_LETTERS = 3 # новая константа - три буквы
for index in range(len(i_list) - 1):
    if (i_list[index + 1] - i_list[index] != 1) \
    and len(i_list) > THREE_LETTERS: # and len(i_list) > 3:
        return False
        break


- Избавляемся от магических чисел, используем константы 
def check_sum(num_list):
    '''проверка сумм соседних чисел'''
    target_index = []
    ZOMBIE_TEMPERATURE = 10  # новая константа
    for i in range(len(num_list) - 1):
        if (num_list[i] + num_list[i + 1] == ZOMBIE_TEMPERATURE): # if (num_list[i] + num_list[i + 1] == 10):
            target_index += [[index_num[i], index_num[i + 1]]]
        else:
            pass
    return target_index

- Избавляемся от магических чисел, используем константы 
def count_walkers(target_index):
    '''подсчет ходоков'''
    THREE_ZOMBIES = 3   # новая константа
    for target_i in target_index:
        count_walk = 0
        for val in village[(target_i[0] + 1): (target_i[1])]:
            if val == "=":
                count_walk += 1
        if count_walk != THREE_ZOMBIES: # if count_walk != 3:
            return False
            break

- Избавляемся от магических чисел, используем константы 
    if count_walk == THREE_ZOMBIES:
        return True
    return

- Избавляемся от магических чисел, используем константы 
# запускаем методы
index_num, num_list = index_list(village)
ONLY_ONE_NUMBER = 1 # новая константа
if len(index_num) <= ONLY_ONE_NUMBER: # if len(index_num) < 2
    return False

- Избавляемся от магических чисел, используем константы 
ONLY_ONE_NUMBER = 1 # новая константа
if len(A) <= ONLY_ONE_NUMBER: # if len(A) <= 1:
    B = Transform_one(Transform_one(A))

- Избавляемся от магических чисел, используем константы 
CONDITION_IS_EVEN = 2 # новая константа
ZERO_REMAINDER = 0  # новая константа
if sum(B) % CONDITION_IS_EVEN == ZERO_REMAINDER:  # if sum(B) % 2 == 0:
    return True
else:
    return False
