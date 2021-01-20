# -*- coding: utf-8 -*-
"""
Задание 7.2c

Переделать скрипт из задания 7.2b:
* передавать как аргументы скрипту:
 * имя исходного файла конфигурации
 * имя итогового файла конфигурации

Внутри, скрипт должен отфильтровать те строки, в исходном файле конфигурации,
в которых содержатся слова из списка ignore.
И записать остальные строки в итоговый файл.

Проверить работу скрипта на примере файла config_sw1.txt.

Ограничение: Все задания надо выполнять используя только пройденные темы.
"""

from sys import argv

ignore = ["duplex", "alias", "Current configuration"]
readfile = argv[1]
writefile = argv[2]
with open(readfile) as f, open(writefile, 'w') as f2:
    for line in f:
        line_false = False
        for ign_word in ignore:
            if ign_word in line:
                line_false = True
        if not line_false:
            f2.write(line)