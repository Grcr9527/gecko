import pandas as pd
import numpy as np

with open('6.txt', 'r', encoding='utf-8') as f:
    A = f.readlines()
    B = []
    C = 0

    del A[0], A[-1]
    C = int(len(A) / 2)

    # print(type(A))
    '''
    for row in A:
        list = row.split("\t")
    '''
    if len(A) <= 2:
        print('所有端口未开放\n!')
    else:
        for i, val in enumerate(A):
            if i % 2 == 1:
                list1 = val.split("\t")
                listA = list1[0].split(":")
                listB = listA[1].split("(")
                B.append(listB[0])
                list2 = list1[1].split(":")
                list3 = list2[1].split(",")
                F=len(list3)
                for num in range(len(list3)):
                    B.append(list3[num])
                # B.append(list3[1])


    #E= [22,3389,445,3306,1433,1521,21,27017,11211,5432,23,25,465,110,995,143,993,5900,6379]
    D = np.array(B).reshape(C, F+1)
    #print("格式 ：%s\t" % D[X][Y])

for X in range(C):
    #print("格式 ：%s\t" % D[X][-1])
    for Y in range(F+1):
        if "21/open" in D[X][Y]:
            with open("21端口-IP"+ ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "22/open" in D[X][Y]:
            with open("22端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "23/open" in D[X][Y]:
            with open("23端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "25/open" in D[X][Y]:
            with open("25端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "110/open" in D[X][Y]:
            with open("110端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "143/open" in D[X][Y]:
            with open("143端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "445/open" in D[X][Y]:
            #print("IP ：%s\t" % D[X][0])
            with open("445端口-IP"+ ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "465/open" in D[X][Y]:
            with open("465端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "993/open" in D[X][Y]:
            with open("993端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "995/open" in D[X][Y]:
            with open("995端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "1433/open" in D[X][Y]:
            with open("1433端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "1521/open" in D[X][Y]:
            with open("1521端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "3306/open" in D[X][Y]:
            with open("3306端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "3389/open" in D[X][Y]:
            with open("3389端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "5432/open" in D[X][Y]:
            with open("5432端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "5900/open" in D[X][Y]:
            with open("5900端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "6379/open" in D[X][Y]:
            with open("6379端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "11211/open" in D[X][Y]:
            with open("11211端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        elif "27017/open" in D[X][Y]:
            with open("27017端口-IP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]))
                IP.write('\n')
        '''else:
            print("所有端口均已关闭\t" )'''

