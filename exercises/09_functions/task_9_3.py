# -*- coding: utf-8 -*-
"""
Задание 9.3

Создать функцию get_int_vlan_map, которая обрабатывает конфигурационный файл коммутатора
и возвращает кортеж из двух словарей:
* словарь портов в режиме access, где ключи номера портов, а значения access VLAN (числа):
{'FastEthernet0/12': 10,
 'FastEthernet0/14': 11,
 'FastEthernet0/16': 17}

* словарь портов в режиме trunk, где ключи номера портов, а значения список разрешенных VLAN (список чисел):
{'FastEthernet0/1': [10, 20],
 'FastEthernet0/2': [11, 30],
 'FastEthernet0/4': [17]}

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw1.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
config_file = 'config_sw1.txt'

def get_int_vlan_map(config_filename):
    dict_trunk = {}
    dict_access = {}
    result = [dict_access, dict_trunk]
    with open(config_filename) as src:
        for line in src:
            if line.startswith('interface '):
                intf = line.split()[-1]
            elif 'switchport trunk allowed vlan' in line:
                vlan = line.split()[-1]
                vlan_list = [(int(vl)) for vl in vlan.split(',')]
                #for vl in vlan.split(','):
                   # vlan_list.append(int(vl))
                dict_trunk[intf] = vlan_list
            elif 'switchport access vlan' in line:
                vlan = line.split()[-1]
                dict_access[intf] = int(vlan)
    return tuple(result)

print(get_int_vlan_map(config_file))                

        
