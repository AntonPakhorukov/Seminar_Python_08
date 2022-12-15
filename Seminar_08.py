# Sample Input
# ['eat', 'tea', 'tan', 'ate', 'nat', “bat']
# Sample Output
# [ ['ate', 'eat', 'tea'], ['nat', 'tan'], ['bat'] ]
# Т.е. сгруппировать слова по 'общим буквам '.

some_list = ['eat', 'tea', 'tan', 'ate', 'nat', 'bat']
res_list = []
temp_list = []
char_list = list(some_list[0])
# print(char_list)
add_words = set() # делаем множество для быстрого пробега по используемым словам
for i in range(len(some_list)):
    if some_list[i] not in add_words:
        temp_list = [some_list[i]]
        add_words.add(some_list[i])
        # if some_list[i + 1] not in add_words:
        for j in range(i, len(some_list)):
            if some_list[j] not in add_words:
                if len(some_list[i]) == len(some_list[j]):
                    for item in some_list[i]:
                        if item not in set(some_list[j]): # Множество будет только здесь
                            break
                    else:
                        temp_list.append(some_list[j])
                        add_words.add(some_list[j])
        res_list.append(sorted(temp_list))
print(res_list)

# Волшебник, сидящий справа, что-то пробормотал себе под нос и 
# метнул заклинание вдоль столешницы. Оно проделало в лаковом 
# покрытии дымящуюся борозду и примерно на полпути встретилось 
# с серебряными змеями заклинания Эффективного Гадосейства, 
# выпущенного волшебником слева.
# Волшебники обменялись долгими, медленными взглядами – такими 
# взглядами можно спокойно жарить каштаны.

# Напишите программу, определяющую более сильные заклинания, 
# то есть числа, большие первого в строке и имеющие четную сумму 
# последних трех разрядов.

# Формат ввода
# Вводятся строки, в которых числа записаны через %%.
# 13250%%20190
# 1632%%21031%%4391%%10053%%5553
# 23958%%24074%%25637%%25737

# Формат вывода
# Из каждой строки вывести подходящие числа через v в порядке ввода.
# 20190
# 21031v10053
# 25637

file = open('file.txt', 'r', encoding='utf-8')
res_list = []
while True:
    line = file.readline().strip()
    if not line:
        break
    line_list = list(map(int, line.split('%%')))
    temp_list = []
    for i in range(1, len(line_list)):
        if line_list[i] > line_list[0]:
            sum = 0
            a = line_list[i]
            for j in range(3):
                sum += a % 10
                a //= 10
            if not sum % 2:
                temp_list.append(line_list[i])
    res_list.append(temp_list)
for el in res_list:
    if len(el) != 0:
        print(*el, sep='v')
    else:
        print()
file.close()
