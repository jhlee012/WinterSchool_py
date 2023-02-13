#github@jhlee012
#If grade.txt exits => run based on txt | Else : Run UI
from typing import List

ccounter = -1
try:
    f = open('grade.txt', 'r', encoding='UTF-8')
    count = -3

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
        grade = 0
        if perc <= 4:
            grade = 1
        elif perc <= 11:
            grade = 2
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
        res = 0
        timesum = 0
        for j in arr:
            res += j[0]*j[1]
            timesum += j[1]
        res = res / timesum
        return str(round(res, 2))

    print('\n\n' + '내신 평균 등급 : ' + sumarr(resgradearr) + ' 등급')

except FileNotFoundError:
    import time
    from tkinter import *  
    import tkinter.font as tkfont
    import tkinter.messagebox as msg
    root = Tk()
    defont = tkfont.Font(family='맑은 고딕', size=20, weight='normal' )
    defontBing = tkfont.Font(family='고딕', size=25, weight='bold')

    root.geometry("1200x800")
    root.resizable = True
    root.title('고등학교 내신 등급 산출기')
    

    root.grid_columnconfigure(0, weight=1)
    root.grid_columnconfigure(3, weight=1)

    TitleLab = Label(root, text='               고등학교 내신성적계산기', font=defontBing, padx=20, pady=10)
    TitleLab.grid(row=0, column=1, columnspan=2)

    namelab = Label(root, text = '과목명', font=defont, padx=20, pady=10)
    namelab.grid(row=1, column=1)

    nameEnt = Entry(root, font=defont)
    nameEnt.grid(row=1, column=2)


    placelab = Label(root, text='석차', font=defont, padx=20, pady=10)
    placelab.grid(row=2, column=1)


    placeEnt = Entry(root, font=defont)
    placeEnt.grid(row=2, column=2)

    samelab = Label(root, text='동석차', font=defont, padx=20, pady=10)
    samelab.grid(row=3, column=1)

    sameEnt = Entry(root, font=defont)
    sameEnt.grid(row=3, column=2)

    alllab = Label(root, text='수강자수', font=defont, padx=20, pady=10)
    alllab.grid(row=4, column=1)

    allEnt = Entry(root, font=defont)
    allEnt.grid(row=4, column=2)

    ctimelab = Label(root, text='단위 (시수)', font=defont, padx=20, pady=10)
    ctimelab.grid(row=5, column=1)

    ctimeEnt = Entry(root, font=defont)
    ctimeEnt.grid(row=5, column=2)

    currentlab = Label(root, text='추가된 과목이 없습니다.', font=defont)
    currentlab.grid(row=7, column=1)


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

    def ClearNeed():
        nameEnt.delete(0, 'end')
        placeEnt.delete(0, 'end')
        sameEnt.delete(0, 'end')
        ctimeEnt.delete(0, 'end')
        sameEnt.insert(0, '1')
        if __name__ == '__main__':
            if 'endl' in globals():
                global endl
                endl.destroy()


    def typecheck():
        try:
            int(placeEnt.get())
            int(sameEnt.get())
            int(allEnt.get())
            int(ctimeEnt.get())
        except ValueError:
            msg.showwarning('과목 없음', '올바른 형식이 아닙니다. \n다시 입력해주세요.')
            ClearAll()
            return False
        if (int (placeEnt.get()) + int(sameEnt.get())) -1 > int(allEnt.get()):
            msg.showwarning('과목 없음', '올바른 형식이 아닙니다. \n다시 입력해주세요.\n(올바르지 않은 형식 : 수강자수가 석차보다 많아야 합니다.)')
            ClearAll()
            return False
        return True

    

    def addRow():
        if typecheck():
            global ccounter
            ccounter += 1
            namearr.append(nameEnt.get())
            posarr.append(int(placeEnt.get()))
            samearr.append(int(sameEnt.get()))
            allarr.append(int(allEnt.get()))
            ctime.append(int(ctimeEnt.get()))
            ClearNeed()

            if ccounter == -1:
                print('Error : Invalid')
                exit()
            else:
                global currentlab
                currentlab.destroy()
                currentlab = Label(root, text=('추가된 과목 : ' + ', '.join(namearr)), font=defont)
                currentlab.grid(row=7, column=1)
        
    global endl
    def getRes():
        ClearAll()
        global currentlab
        currentlab.destroy()
        global namearr, posarr, samearr, allarr, ctime
        if ccounter == -1:
            msg.showwarning('과목 없음', '과목별 성적이 입력되지 않았습니다.\n성적 입력 후 다시 시도해주세요. ')
            return
        resultarr: list[str]= []
        resgradearr = []
        for i in range(ccounter+1):

            perc = ((int(posarr[i]) + int(samearr[i]) - 1) / int(allarr[i])) * 100
            grade = 0
            if perc <= 4:
                grade = 1
            elif perc <= 11:
                grade = 2
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
            resultarr.append('과목 : ' + namearr[i] + ' (' + str(ctime[i]) +')' +' | 백분위 : ' + str(100-round(perc)) +' | 등급 : ' + str(grade))

        pres = '\n'.join(resultarr)
        currentlab = Label(root, text=pres, font=defont, justify=LEFT)
        currentlab.grid(row=7, column=1)


        def sumarr(arr):
            res = 0
            timesum = 0
            for j in arr:
                res += j[0]*j[1]
                timesum += j[1]
            res = res / timesum
            return round(res, 2)

        bc = 'green'
        if sumarr(resgradearr) < 2:
            bc = 'cyan'
        elif 4 > sumarr(resgradearr) >= 3:
            bc='yellow'
        elif sumarr(resgradearr) >= 4:
            bc = 'red'
        global endl
        endl = Label(root, text=('평균등급 : ' + str(sumarr(resgradearr)) + ' 등급'),  fg='black', bg=bc,font=defontBing, borderwidth='3', relief='solid')
        endl.grid(row=7, column=2, rowspan=2, padx=60)

    def resetAll():
        ClearAll()
        global namearr, posarr, samearr, allarr, ctime, ccounter, endl
        ccounter = -1
        namearr.clear()
        posarr.clear()
        samearr.clear()
        allarr.clear()
        ctime.clear()
        currentlab.destroy()
        if __name__ =='__main__':
            if 'endl' in globals():
                endl.destroy()

                
    resetBtn = Button(root, text='초기화', font=defont, bg='darkgray', fg='black', command=resetAll)
    resetBtn.grid(row=6, column=1, padx=10, pady=10)

    addBtn = Button(root, text='과목 추가', font=defont, bg='gray', command=addRow)
    addBtn.grid(row=6,column=2)

    finBtn = Button(root, text='완료' ,font=defont, bg='cyan', command=getRes)
    finBtn.grid(row=6, column=3, columnspan=2)




    root.mainloop()







