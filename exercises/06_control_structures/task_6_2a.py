# -*- coding: utf-8 -*-
"""
Задание 6.2a

Сделать копию скрипта задания 6.2.

Добавить проверку введенного IP-адреса. Адрес считается корректно заданным, если он:
   - состоит из 4 чисел (а не букв или других символов)
   - числа разделенны точкой
   - каждое число в диапазоне от 0 до 255

Если адрес задан неправильно, выводить сообщение:
'Неправильный IP-адрес'

Сообщение должно выводиться только один раз.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
ip = input('Введите ip :')
ip = ip.split('.')
ip_true = True
if len(ip) == 4:
    ip_int = []
    for adr in ip:
        if adr.isdigit():
            ip_int.append(int(adr))
            if int(adr) > 255 or int(adr) < 0:
                ip_true = False
                break
        else:
            ip_true = False
            break
else:
    ip_true = False

if ip_true:
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
else:
    print('Неправильный IP-адрес')