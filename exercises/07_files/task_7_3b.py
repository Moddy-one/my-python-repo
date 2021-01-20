# -*- coding: utf-8 -*-
"""
Задание 7.3b

Сделать копию скрипта задания 7.3a.

Переделать скрипт:
- Запросить у пользователя ввод номера VLAN.
- Выводить информацию только по указанному VLAN.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
input_vlan = int(input('ВВедите номер vlan :'))
println ='{:<6} {:<17}{:>7}'
with open('CAM_table.txt') as f:
    mac_list = []
    for line in f:
        if 'DYNAMIC' in line:
            line_list = line.split()
            line_list[0] = int(line_list[0])
            mac_list.append(line_list)
    mac_list.sort()
    for list_one in mac_list:
        if input_vlan == list_one[0]:
            print(println.format(list_one[0],list_one[1],list_one[3]))