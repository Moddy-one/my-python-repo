ip = input('Введите ip :')
ip_true = False
while not ip_true:
    ip = str(ip)
    ip = ip.split('.')
    if len(ip) != 4:
        ip = input('Введите ip снова:')
        ip_true = False
        break
    elif not (ip[0].isdigit() and ip[1].isdigit() and ip[2].isdigit() and ip[3].isdigit()):
        ip = input('Введите ip снова:')
        ip_true = False
        break
    else:
        ip_int = []
        for adr in ip:
            ip_int.append(int(adr))
            if int(adr) > 255 or int(adr) < 0:
                ip_true = False
                ip = input('Введите ip снова:')
                break
            else:
                ip_true = True

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