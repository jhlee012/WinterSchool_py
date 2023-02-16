def getGrade(counter, resultarr, resgradearr, namearr, posarr, samearr, allarr, ctime):
    for i in range(counter+1):
        perc = ((int(posarr[i]) + int(samearr[i]) - 1) / int(allarr[i])) * 100
        grade = 0
        if perc <= 4:
            grade = 1
        elif perc <= 11:
            grade = 2
        elif perc <= 23:
            grade = 3
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
        resultarr.append(
            '과목 : ' + namearr[i] + ' (' + str(ctime[i]) + ')' + ' | 백분위 : ' + str(100 - round(perc)) + ' | 등급 : ' + str(
                grade))