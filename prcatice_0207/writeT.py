import time
import turtle as t

t.shape('turtle')

s = t.textinput("어쩌라고", "이름을 입력하십시오 : ")

n = t.textinput("아니시발어쩌라고", "몇각형인데요 : ")
nn = t.textinput("어쩌라고", "한변의길이? : ")

try:
    int(n)
    int(nn)
except ValueError:
    t.write('숫자도못세냐'+s+'아')
    time.sleep(10)
    exit()


if s == '시발련' or s == '씨발련':
    t.write('씨발련은받지않습니다')
    time.sleep(10)
else:
    n = int(n)
    nn = int(nn)
    for i in range(n):
        t.write('안녕하세요 ' + s + '아')
        t.forward(nn)
        t.left(360//n)



