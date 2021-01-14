# -*- coding: utf-8 -*-
"""
Задание 5.2b

Преобразовать скрипт из задания 5.2a таким образом,
чтобы сеть/маска не запрашивались у пользователя,
а передавались как аргумент скрипту.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
from sys import argv
inpstr = argv[1]
#inpstr = input('Введите ip-сеть: ')
#inpstr = '10.0.5.195/28'
inpstr = inpstr.split('/')
inpstr[0] = inpstr[0].split('.')
mask = int(inpstr[1])
maskbin = '1' * mask + '0' * (32 - mask)
maskdex = [int(maskbin[0:8],2),int(maskbin[8:16],2),int(maskbin[16:24],2),int(maskbin[24:],2)]
ip = inpstr[0]
ipbin = '''{0:08b}{1:08b}{2:08b}{3:08b}'''
ipbin = ipbin.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3]))
ipbin = ipbin[0:mask] + '0' * (32 - mask)
ip = [int(ipbin[0:8],2),int(ipbin[8:16],2),int(ipbin[16:24],2),int(ipbin[24:],2)]

prln1 = '''
        Network:
        {0:<8} {1:<8} {2:<8} {3:<8}
        {0:08b} {1:08b} {2:08b} {3:08b}'''
prln2 = '''
        Mask:
        /{4}
        {0:<8} {1:<8} {2:<8} {3:<8}
        {0:08b} {1:08b} {2:08b} {3:08b}'''

print(prln1.format(int(ip[0]),int(ip[1]),int(ip[2]),int(ip[3])))
print(prln2.format(maskdex[0],maskdex[1],maskdex[2],maskdex[3], mask))