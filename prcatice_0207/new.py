# p = int(input('p?'))
# q = int(input('Q?'))

# print('// : ', p//q)
# print('% :', p%q)


# num = int(input('N?'))
# a = num % 2

# if (a == 1):
#     print('홀수')
# elif(a ==0):
#     print('짝수')
# else:
#     print('어케했노')

#----------------------------------

def mi(temp, type):
    if (type == 'sec' or type == 'second'):
        sec = temp
        mins = temp/60
        hour = temp/3600
    elif (type == 'min' or type == 'minute'):
        sec = temp * 60
        mins = temp
        hour = temp / 60

    elif (type == 'hour' or type == 'hours'):
        sec = temp / 3600
        mins = temp / 60
        hour = temp
    else:
        print('TypeError! - Undefined Function Type')
        return;
    
    print('초 : ', sec)
    print('분 : ', mins)
    print('시 : ', hour)

t = int(input('Time? : '))
type = input('Type? : ')
mi(t, type)

        
