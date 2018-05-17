from grades import Student
import sys
from collections import defaultdict
GR =0
FL = ""
def grade(point="50"):
    range = round((100 - int(point)) / 7)

    if GR > 100 - range and GR <= 100:
        FL = "A+"
    elif GR > 100 - 2 * range and GR <= 100 - range:
        FL = "A"
    elif GR > 100 - 3 * range and GR <= 100 - 2 * range:
        FL = "A-"
    elif GR > 100 - 4 * range and GR <= 100 - 3 * range:
        FL = "B+"
    elif GR > 100 - 5 * range and GR <= 100 - 4 * range:
        FL = "B"
    elif GR > 100 - 6 * range and GR <= 100 - 5 * range:
        FL = "B-"
    elif GR > 100 - 7 * range and GR <= 100 - 6 * range:
        FL = "C"
    else:
        FL = "F"
    return FL
alldict = defaultdict(list)

for d in (Student.dict_data1 ,Student.dict_data3):
    for key, value in d.items():
            alldict[key].append(value)

for d in (Student.dict_data1,Student.dict_data2):
    for key ,value in d.items():
        if key not in Student.dict_data2:
            alldict[key].append("")

        else:
            if(value.isdigit()):
                alldict[key].append(value)

for d in (Student.dict_data1,Student.dict_data4):
    for key ,value in d.items():
        if key not in Student.dict_data4:
            alldict[key].append("")

        else:
            if(value.isdigit()):
                alldict[key].append(value)

for d in (Student.dict_data1, Student.dict_data5):
    for key, value in d.items():
        if key not in Student.dict_data5:
            alldict[key].append("")

        else:
            if (value.isdigit()):
                alldict[key].append(value)

for d in (Student.dict_data1, Student.dict_data6):
    for key, value in d.items():
        if key not in Student.dict_data6:
            alldict[key].append("")

        else:
            if (value.isdigit()):
                alldict[key].append(value)

for d in (Student.dict_data1, Student.dict_data7):
    for key, value in d.items():
        if key not in Student.dict_data7:
            alldict[key].append("")

        else:
            if (value.isdigit()):
                alldict[key].append(value)
'''     
alldict1 = defaultdict(list)
for d in (Student.dict_data1, Student.dict_data3):
    for key, value in d.items():
        alldict1[key].append(value)

for d in (Student.dict_data1, Student.dict_data2):
    for key, value in d.items():
        if key not in Student.dict_data2:
            alldict1[key].append("")

        else:
            if (value.isdigit()):
                alldict1[key].append(value)

for d in (Student.dict_data1, Student.dict_data4):
    for key, value in d.items():
        if key not in Student.dict_data4:
            alldict1[key].append("")

        else:
            if (value.isdigit()):
                alldict1[key].append(value)

for d in (Student.dict_data1, Student.dict_data5):
    for key, value in d.items():
        if key not in Student.dict_data5:
            alldict1[key].append("")

        else:
            if (value.isdigit()):
                alldict1[key].append(value)

for d in (Student.dict_data1, Student.dict_data6):
    for key, value in d.items():
        if key not in Student.dict_data6:
            alldict1[key].append("")

        else:
            if (value.isdigit()):
                alldict1[key].append(value)

for d in (Student.dict_data1, Student.dict_data7):
    for key, value in d.items():
        if key not in Student.dict_data7:
            alldict1[key].append("")

        else:
            if (value.isdigit()):
                alldict1[key].append(value)

'''
for key,value in alldict.items():
    A1 = 0
    A2 = 0
    PR = 0
    T1 = 0
    T2 = 0
    if (value[2] != ""):
        A1  = int(value[2])
    else:
        A1  = 0
    if (value[3] != ""):
        A2  = int(value[3])
    else:
        A2  = 0
    if (value[4] != ""):
        PR  = int(value[4])
    else:
        PR  = 0

    if (value[5] != ""):
        T1  = int(value[5])
    else:
        T1  = 0
    if (value[6] != ""):
        T2  = int(value[6])
    else:
        T2  = 0
    GR = round(7.5 * A1 / int(Student.firstline) + 7.5 * A2 / int(Student.firstline1) + 25 * PR / int(
        Student.firstline2) + 30 * T1 / int(Student.firstline3) + 30 * T2 / int(Student.firstline4))
    FL = grade()
    alldict[key].append(str(GR))
    alldict[key].append(FL)
    #print(('{:6}' + '{:6}' * len(value)).format(key, *value))
#print(alldict)
'''
for key, value in alldict1.items():
    A1= 0
    A2 =0
    PR =0
    T1 =0
    T2 =0
    if(value[2]!=""):
        A1 =value[2]= int(value[2])
    else:
        A1  = value[2]= 0
    if (value[3] != ""):
        A2 =value[3]= int(value[3])
    else:
        A2=value[3] = 0
    if (value[4] != ""):
        PR =value[4]= int(value[4])
    else:
        PR = value[4] = 0

    if (value[5] != ""):
        T1 =value[5]= int(value[5])
    else:
        T1 = value[5] = 0
    if (value[6] != ""):
        T2 =value[6]= int(value[6])
    else:
        T2 = value[6] = 0
    GR = round(7.5*A1/int(Student.firstline)+7.5*A2/int(Student.firstline1)+25*PR/int(Student.firstline2)+30*T1/int(Student.firstline3)+30*T2/int(Student.firstline4))
    FL = grade()
    alldict1[key].append(GR)
    alldict1[key].append(FL)
print(alldict1)
'''
def option1():
    while True:
        nChoose = input("please enter course:")
        if nChoose == "a1" or nChoose ==  "A1":
            alldict = defaultdict(list)
            for d in (Student.dict_data1, Student.dict_data3):
                for key, value in d.items():
                    alldict[key].append(value)
            for d in (Student.dict_data1, Student.dict_data2):
                for key, value in d.items():
                    if key not in Student.dict_data2:
                        del alldict[key]
                    else:
                        if (value.isdigit()):
                            alldict[key].append(value)
            print("A1 grades (" + Student.firstline.strip() + ')')

            for key, value in alldict.items():
                fullname = value[0]+","+value[1]
                print('{:6} {:16} {:6}'.format(key, fullname, value[2]))
            break
        if nChoose == "a2" or nChoose == "A2":

            alldict = defaultdict(list)
            for d in (Student.dict_data1, Student.dict_data3):
                for key, value in d.items():
                    alldict[key].append(value)
            for d in (Student.dict_data1, Student.dict_data4):
                for key, value in d.items():
                    if key not in Student.dict_data4:
                        del alldict[key]
                    else:
                        if (value.isdigit()):
                            alldict[key].append(value)
            print("A2 grades (" + Student.firstline1.strip() + ')')
            for key, value in alldict.items():
                fullname = value[0] + "," + value[1]
                print('{:6} {:16} {:6}'.format(key, fullname, value[2]))
            break
        if nChoose.lower() == "pr" :

            alldict = defaultdict(list)
            for d in (Student.dict_data1, Student.dict_data3):
                for key, value in d.items():
                    alldict[key].append(value)
            for d in (Student.dict_data1, Student.dict_data5):
                for key, value in d.items():
                    if key not in Student.dict_data5:
                        del alldict[key]
                    else:
                        if (value.isdigit()):
                            alldict[key].append(value)
            print("PR grades (" + Student.firstline2.strip() + ')')
            for key, value in alldict.items():
                fullname = value[0] + "," + value[1]
                print('{:6} {:16} {:6}'.format(key, fullname, value[2]))
            break
        elif nChoose == "T1" or nChoose ==  "t1" :

            alldict = defaultdict(list)
            for d in (Student.dict_data1, Student.dict_data3):
                for key, value in d.items():
                    alldict[key].append(value)
            for d in (Student.dict_data1, Student.dict_data6):
                for key, value in d.items():
                    if key not in Student.dict_data6:
                        del alldict[key]
                    else:
                        if (value.isdigit()):
                            alldict[key].append(value)
            print("T1 grades (" + Student.firstline3.strip() + ')')
            for key, value in alldict.items():
                fullname = value[0] + "," + value[1]
                print('{:6} {:16} {:6}'.format(key, fullname, value[2]))
            break
        elif nChoose == "T2" or nChoose ==  "t2":

            alldict = defaultdict(list)
            for d in (Student.dict_data1, Student.dict_data3):
                for key, value in d.items():
                    alldict[key].append(value)
            for d in (Student.dict_data1, Student.dict_data7):
                for key, value in d.items():
                    if key not in Student.dict_data7:
                        del alldict[key]
                    else:
                        if (value.isdigit()):
                            alldict[key].append(value)
            print("T2 grades (" + Student.firstline4.strip() + ')')
            for key, value in alldict.items():
                fullname = value[0] + "," + value[1]
                print('{:6} {:16} {:6}'.format(key, fullname, value[2]))
            break
        else:
            print("error! pleace enter right course")

def option2():
    while True:
        nChoose = input("please enter course:")
        if nChoose == "a1" or nChoose == "A1":
            print("A1 average: " + str(round(sum(Student.stulist)/Student.lines,2))+"/"+str(Student.firstline))
            break
        elif nChoose == "a2" or nChoose == "A2":
            print("A2 average: " + str(round(sum(Student.stulist1)/Student.lines1,2))+"/"+str(Student.firstline1))
            break
        elif nChoose == "PR" or nChoose == "Pr" or nChoose == "pr" or nChoose == "pR":
            print("PR average: " + str(round(sum(Student.stulist2) / Student.lines2,2)) + "/" + str(Student.firstline2))
            break
        elif nChoose == "T1" or nChoose == "t1":
            print("T1 average: " + str(round(sum(Student.stulist3) / Student.lines3,2)) + "/" + str(Student.firstline3))
            break
        elif nChoose == "T2" or nChoose =='t2':
            print("T2 average: " + str(round(sum(Student.stulist4) / Student.lines4,2)) + "/" + str(Student.firstline4))
            break
        else:
            print("error! pleace enter right course")
def option3():
    print('ID'.ljust(6) + "LN".ljust(6) + "FN".ljust(6) + "A1".ljust(6) + "A2".ljust(6) + "PR".ljust(6) + "T1".ljust(
        6) + "T2".ljust(6) + "GR".ljust(6) + "FL".ljust(6))
    for key, value in alldict.items():

        print(('{:6}' + '{:6}' * len(value)).format(key, *value))

def option4():
    def sortDic(Dict, valuePostion):
        return sorted(Dict.items(), key=lambda e: e[1][valuePostion], reverse=False)
    def sortDic1(Dict, valuePostion):
        return sorted(Dict.items(), key=lambda e: e[1][valuePostion], reverse=True)


    while True:
        nChoose = input("please enter sorted component: LN OR GR")
        if nChoose == "GR":
            alldict2 = sortDic1(alldict, 7)
            print('ID'.ljust(6) + "LN".ljust(6) + "FN".ljust(6) + "A1".ljust(6) + "A2".ljust(6) + "PR".ljust(
                6) + "T1".ljust(
                6) + "T2".ljust(6) + "GR".ljust(6) + "FL".ljust(6))
            for key, value in alldict2:
                print(('{:6}' + '{:6}' * len(value)).format(key, *value))
            break
        if nChoose == "LN":
            alldict2 = sortDic(alldict, 0)
            print('ID'.ljust(6) + "LN".ljust(6) + "FN".ljust(6) + "A1".ljust(6) + "A2".ljust(6) + "PR".ljust(
                6) + "T1".ljust(
                6) + "T2".ljust(6) + "GR".ljust(6) + "FL".ljust(6))
            for key, value in alldict2:

                print(('{:6}' + '{:6}' * len(value)).format(key, *value))
            break
def option5():
    FL1 =""
    while True:
        nChoose = input("please enter Pass/Fail Point: ")

        def grade(point="50"):
            range = round((100 - int(point)) / 7)

            if GR > 100 - range and GR <= 100:
                FL1 = "A+"
            elif GR > 100 - 2 * range and GR <= 100 - range:
                FL1= "A"
            elif GR > 100 - 3 * range and GR <= 100 - 2 * range:
                FL1 = "A-"
            elif GR > 100 - 4 * range and GR <= 100 - 3 * range:
                FL1 = "B+"
            elif GR > 100 - 5 * range and GR <= 100 - 4 * range:
                FL1 = "B"
            elif GR > 100 - 6 * range and GR <= 100 - 5 * range:
                FL1 = "B-"
            elif GR > 100 - 7 * range and GR <= 100 - 6 * range:
                FL1 = "C"
            else:
                FL1 = "F"
            return FL1
        alldict3 = defaultdict(list)
        for d in (Student.dict_data1, Student.dict_data3):
            for key, value in d.items():
                alldict3[key].append(value)

        for d in (Student.dict_data1, Student.dict_data2):
            for key, value in d.items():
                if key not in Student.dict_data2:
                    alldict3[key].append("")

                else:
                    if (value.isdigit()):
                        alldict3[key].append(value)

        for d in (Student.dict_data1, Student.dict_data4):
            for key, value in d.items():
                if key not in Student.dict_data4:
                    alldict3[key].append("")

                else:
                    if (value.isdigit()):
                        alldict3[key].append(value)

        for d in (Student.dict_data1, Student.dict_data5):
            for key, value in d.items():
                if key not in Student.dict_data5:
                    alldict3[key].append("")

                else:
                    if (value.isdigit()):
                        alldict3[key].append(value)

        for d in (Student.dict_data1, Student.dict_data6):
            for key, value in d.items():
                if key not in Student.dict_data6:
                    alldict3[key].append("")

                else:
                    if (value.isdigit()):
                        alldict3[key].append(value)

        for d in (Student.dict_data1, Student.dict_data7):
            for key, value in d.items():
                if key not in Student.dict_data7:
                    alldict3[key].append("")

                else:
                    if (value.isdigit()):
                        alldict3[key].append(value)
        print(
            'ID'.ljust(6) + "LN".ljust(6) + "FN".ljust(6) + "A1".ljust(6) + "A2".ljust(6) + "PR".ljust(6) + "T1".ljust(
                6) + "T2".ljust(6) + "GR".ljust(6) + "FL".ljust(6))
        for key, value in alldict3.items():
            A1 = 0
            A2 = 0
            PR = 0
            T1 = 0
            T2 = 0
            if (value[2] != ""):
                A1 = int(value[2])
            else:
                A1 = 0
            if (value[3] != ""):
                A2 = int(value[3])
            else:
                A2 = 0
            if (value[4] != ""):
                PR = int(value[4])
            else:
                PR = 0

            if (value[5] != ""):
                T1 = int(value[5])
            else:
                T1 = 0
            if (value[6] != ""):
                T2 = int(value[6])
            else:
                T2 = 0
            GR = round(7.5 * A1 / int(Student.firstline) + 7.5 * A2 / int(Student.firstline1) + 25 * PR / int(
                Student.firstline2) + 30 * T1 / int(Student.firstline3) + 30 * T2 / int(Student.firstline4))
            FL1 = grade(nChoose)

            alldict3[key].append(str(GR))
            alldict3[key].append(FL1)
            print(('{:6}' + '{:6}' * len(value)).format(key, *value))

        break
def option6():
    print("Good Bye")
    sys.exit()

