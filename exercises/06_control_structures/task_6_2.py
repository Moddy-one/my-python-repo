# -*- coding: utf-8 -*-
"""
Задание 6.2

1. Запросить у пользователя ввод IP-адреса в формате 10.0.1.1
2. В зависимости от типа адреса (описаны ниже), вывести на стандартный поток вывода:
   'unicast' - если первый байт в диапазоне 1-223
   'multicast' - если первый байт в диапазоне 224-239
   'local broadcast' - если IP-адрес равен 255.255.255.255
   'unassigned' - если IP-адрес равен 0.0.0.0
   'unused' - во всех остальных случаях


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

ip = input('Введите ip :')
ip = ip.split('.')
ip_int = []
for adr in ip:
    ip_int.append(int(adr))
if ip_int[0] > 0 and ip_int[0] < 224:
    print('unicast')
elif ip_int[0] > 223 and ip_int[0] < 240:
    print('multicast')
elif ip_int[0] == 255 and ip_int[0]==ip_int[1]==ip_int[2]==ip_int[3]:
    print ('local broadcast')
elif ip_int[0] == 0 and ip_int[0]==ip_int[1]==ip_int[2]==ip_int[3]:
    print ('unassigned')
else:
    print('unused')