# -*- coding: utf-8 -*-
"""
Задание 7.1

Обработать строки из файла ospf.txt и вывести информацию по каждой строке в таком виде:

Prefix                10.0.24.0/24
AD/Metric             110/41
Next-Hop              10.0.13.3
Last update           3d18h
Outbound Interface    FastEthernet0/0

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""
println = '''
Prefix                {}
AD/Metric             {}
Next-Hop              {}
Last update           {}
Outbound Interface    {}'''

with open('ospf.txt') as f:
    for line in f:
        line = line.replace(',', '').replace('via ','').rstrip()
        line_list = line.split()
        #print(line_list)
        print(println.format(line_list[1],line_list[2].strip('[]'),line_list[3],line_list[4],line_list[5]))