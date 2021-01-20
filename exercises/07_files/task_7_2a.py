# -*- coding: utf-8 -*-
"""
Задание 7.2a

Сделать копию скрипта задания 7.2.

Дополнить скрипт:
  Скрипт не должен выводить команды, в которых содержатся слова,
  которые указаны в списке ignore.

Ограничение: Все задания надо выполнять используя только пройденные темы.

"""

ignore = ["duplex", "alias", "Current configuration"]

with open('config_sw1.txt') as f:
    for line in f:
        if line[0]=='!':
            continue
        #elif ignore[0] in line or ignore[1] in line or ignore[2] in line:
            #continue
        else:
            line_false = False
            for ign_word in ignore:
                if ign_word in line:
                    line_false = True
            if not line_false:
                print(line.rstrip())