def cal(year, month=1, day=1):

    def if_leap_year(year):
        if year % 400 == 0:
            return True
        if year % 100 == 0:
            return False
        if year % 4 == 0:
            return True
    return False

#　西暦を入力してもらい、その年のカレンダーを表示
y = int(input('西暦(４桁)を入力してください：'))

leap = is_leap_year(y)

for m in range(1 ,12 +1):
    print(m, '月')
    print(" 日 月 火 水 木 金 土 ")
    first = cal(y, m)
    for d in range(1, 31 + 1):
        if m == 2:
            if m == 2 and (not leap and d > 28 or leap and d > 29):
                break
            elif m in (4, 6, 9,11) and d > 30:
                break

            if d == 1:
                print('    ' * first, end='')
            print(' ' * (1 - d // 10), d, end=' ')
            w += 1
            if w > 6:
                print()
                w = 0

        print('\n')

        print(' ' * d // 10, d, end=' ')

    print()