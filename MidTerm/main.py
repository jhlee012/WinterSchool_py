#github@jhlee012
#If grade.txt exits => run based on txt | Else : Run UI
ccounter = -1
try:
    f = open('grade.txt', 'r', encoding='UTF-8')
    count = -3;

    namearr = [] #과목명
    posarr = [] #석차
    samearr = [] #동석차수
    allarr = [] #전체 이수자 수
    ctime = [] #시수 (단위수)

    for i in f.readlines():
        count = count + 1 #Line Number

        if count == -1 or count == -2:
            continue
        else:
            temparr = i.rsplit()
            namearr.append(temparr[0])
            posarr.append(temparr[1])
            samearr.append(temparr[2])
            allarr.append(temparr[3])
            ctime.append(temparr[4])


    resultarr= []
    resgradearr = []
    for i in range(count+1):

        perc = ((int(posarr[i]) + int(samearr[i]) - 1) / int(allarr[i])) * 100
        grade = 0;
        if perc <= 4:
            grade = 1;
        elif perc <= 11:
            grade = 2;
        elif perc <= 23:
            grade =3
        elif perc <= 40:
            grade = 4
        elif perc <= 60:
            grade = 5
        elif perc <= 77:
            grade = 6
        elif perc <= 89:
            grade = 7
        elif perc <= 96:
            grade = 8
        else:
            grade = 9

        resgradearr.append([grade, int(ctime[i])])
        resultarr.append('과목 : ' + namearr[i] + ' | 등급 : ' + str(grade))

    for i in range(count+1):
        print(resultarr[i])


    def sumarr(arr):
        res = 0;
        timesum = 0;
        for j in arr:
            res += j[0]*j[1]
            timesum += j[1]
        res = res / timesum
        return str(round(res, 2))

    print('\n\n' + '내신 평균 등급 : ' + sumarr(resgradearr) + ' 등급')

except FileNotFoundError:
    import time
    from tkinter import *

    root = Tk()

    root.geometry("800x600")
    root.title('고등학교 내신 등급 산출기')


    namelab = Label(root, text = '과목명', font=10, padx=20, pady=10)
    namelab.grid(row=0, column=0)

    nameEnt = Entry(root, show='과목명을 입력하세요', font=10)
    nameEnt.grid(row=0, column=1)


    placelab = Label(root, text='석차', font='10', padx=20, pady=10)
    placelab.grid(row=1, column=0)

    placeEnt = Entry(root, show='석차를 입력하세요', font=10)
    placeEnt.grid(row=1, column=1)

    samelab = Label(root, text='동석차', font='10', padx=20, pady=10)
    samelab.grid(row=2, column=0)

    sameEnt = Entry(root, show='동석차수를 입력하세요', font=10)
    sameEnt.grid(row=2, column=1)

    alllab = Label(root, text='수강자수', font='10', padx=20, pady=10)
    alllab.grid(row=3, column=0)

    allEnt = Entry(root, show='수강자수를 입력하세요', font=10)
    allEnt.grid(row=3, column=1)

    ctimelab = Label(root, text='단위 (시수)', font=10, padx=20, pady=10)
    ctimelab.grid(row=4, column=0)

    ctimeEnt = Entry(root, show='단위(시수)를 입력하세요', font=10)
    ctimeEnt.grid(row=4, column=1)

    resetBtn = Button(root, text='초기화', bg='darkgray', fg='white', padx=5, pady=0)
    resetBtn.grid(row=5, column=0)

    addBtn = Button(root, text='과목 추가', bg='gray', pady=10, padx=5)
    addBtn.grid(row=5,column=1)

    finBtn = Button(root, text='완료', bg='cyan', padx=20, pady=10)
    finBtn.grid(row=5, column=2)


    namearr = [] #과목명
    posarr = [] #석차
    samearr = [] #동석차수
    allarr = [] #전체 이수자 수
    ctime = [] #시수 (단위수)

    def ClearAll():
        nameEnt.delete(0, 'end')
        placeEnt.delete(0, 'end')
        sameEnt.delete(0, 'end')
        allEnt.delete(0, 'end')
        ctimeEnt.delete(0, 'end')

    def addRow():
        global ccounter;
        ccounter += 1
        namearr.append(nameEnt.get())
        posarr.append(placeEnt.get())
        samearr.append(sameEnt.get())
        allEnt.append(allEnt.get())
        ctime.append(ctimeEnt.get())
        ClearAll()

        if ccounter == -1:
            print('Error : Invalid')
            exit()
        else:
            currentlab = Label(root, text=('추가된 과목 : ' + namearr.join(', ')), font=10)
            currentlab.grid(row=6, column=0)





    root.mainloop()





