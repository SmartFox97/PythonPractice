_data = 0
player = 0
while True:
    try:
        _temp = int(input('请玩家' + str(player % 2 + 1) + '输入：'))
        if _temp not in [1, 2, 3]:
            raise Exception
    except Exception as e:
        print('输入错误！重新输入')
        continue

    _data += _temp

    if _data > 17:
        print('玩家' + str(1 if player % 2 else 2) + '获胜')
        break
    elif _data == 17:
        print('玩家' + str(player % 2 + 1) + '获胜')
        break
    player += 1
    print('现在数值为：', _data)
