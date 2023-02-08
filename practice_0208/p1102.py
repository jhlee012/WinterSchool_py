infile = open('phone.txt', 'a', encoding='UTF-8')
for i in range(4):
    infile.write('시발좆까')
    infile.write(str(i+1))
    infile.write('\n')
infile.close()
