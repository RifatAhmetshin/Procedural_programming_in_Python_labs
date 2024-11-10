# TODO решите задачу

def task() -> float:
    m = 0
    schform = 0
    summa = 0
    ch1 = 0
    ch2 = 0
    file = open("input.json", "r")
    m = file.readlines()
    for i in range(len(m)):
        if (m[i].find("weight")) != -1:
            ch2 = float(m[i][((m[i].find("weight"))+9):len(m[i])-1])


        elif m[i].find("score") != -1:
            ch1 = float(m[i][((m[i].find("score"))+8):len(m[i])-2])


        if(ch1 != 0) and (ch2 != 0):
            summa += ch1*ch2
            ch1, ch2 = 0, 0
    file.close()
    return round(summa, 3)

print(task())
