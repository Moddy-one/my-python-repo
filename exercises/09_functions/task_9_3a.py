# -*- coding: utf-8 -*-
"""
Задание 9.3a

Сделать копию функции get_int_vlan_map из задания 9.3.

Дополнить функцию:
    - добавить поддержку конфигурации, когда настройка access-порта выглядит так:
            interface FastEthernet0/20
                switchport mode access
                duplex auto
      То есть, порт находится в VLAN 1

В таком случае, в словарь портов должна добавляться информация, что порт в VLAN 1
      Пример словаря: {'FastEthernet0/12': 10,
                       'FastEthernet0/14': 11,
                       'FastEthernet0/20': 1 }

У функции должен быть один параметр config_filename, который ожидает как аргумент имя конфигурационного файла.

Проверить работу функции на примере файла config_sw2.txt


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
config_file = 'config_sw2.txt'

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
                dict_trunk[intf] = [(int(vl)) for vl in vlan.split(',')]
            elif 'switchport mode access' in line:
                dict_access[intf] = 1
            elif 'switchport access vlan' in line:
                vlan = line.split()[-1]
                dict_access[intf] = int(vlan)
    return tuple(result)

print(get_int_vlan_map(config_file))            
