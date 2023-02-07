
f = open('C:/Users/buddy/Desktop/winter/price.txt', 'r')


a_price = int(f.readline().split(' : ')[1])
c_price = int(f.readline().split(' : ')[1])
ca_price = int(f.readline().split(' : ')[1])

am_s = int(input('아메리카노? : '))
ca_s = int(input('카페라떼? : '))
capu_s = int(input('카푸치노? :'))



sales =  a_price*am_s + ca_s*c_price *capu_s + capu_s*ca_price

print('총매출 : ', sales)