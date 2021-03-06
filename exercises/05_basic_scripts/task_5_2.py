# -*- coding: utf-8 -*-
"""
Задание 5.2

Запросить у пользователя ввод IP-сети в формате: 10.1.1.0/24

Затем вывести информацию о сети и маске в таком формате:

Network:
10        1         1         0
00001010  00000001  00000001  00000000

Mask:
/24
255       255       255       0
11111111  11111111  11111111  00000000

Проверить работу скрипта на разных комбинациях сеть/маска.

Подсказка: Получить маску в двоичном формате можно так:
In [1]: "1" * 28 + "0" * 4
Out[1]: '11111111111111111111111111110000'


Ограничение: Все задания надо выполнять используя только пройденные темы.
"""
inpstr = input('Введите ip-сеть: ')
#inpstr = '10.7.1.0/28'
inpstr = inpstr.split('/')
inpstr[0] = inpstr[0].split('.')
mask = int(inpstr[1])
maskbin = '1' * mask + '0' * (32 - mask)
maskdex = [int(maskbin[0:8],2),int(maskbin[8:16],2),int(maskbin[16:24],2),int(maskbin[24:],2)]

ip = inpstr[0]
prln1 = '''
        Network:
        {0:<8} {1:<8} {2:<8} {3:<8}
        {0:08b} {1:08b} {2:08b} {3:08b}
        '''
prln2 = '''
        Mask:
        /{4}
        {0:<8} {1:<8} {2:<8} {3:<8}
        {0:08b} {1:08b} {2:08b} {3:08b}
        '''

print(prln1.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
print(prln2.format(maskdex[0],maskdex[1],maskdex[2],maskdex[3], mask))