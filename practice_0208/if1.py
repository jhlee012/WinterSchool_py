year = int(input('연도를 입력:'))

if (year % 4 == 0 and year % 100 != 0 ) or year % 400 == 0:
    print(year, '년은 윤년입니다.')
else:
    print(year, '년은 윤년이겠냐 ㅋㅋ')
