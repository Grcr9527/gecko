import pandas as pd
import numpy as np

'''
使用说明:通过NMAP弱口令端口扫描,产生的文件 XXX.gnmap,改名为6.txt,与此脚本存放同一目录下,通过python3 运行
注:需要有pandas,numpy模块
'''


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
        if "21/open/tcp//ftp///" in D[X][Y]:
            with open("21端口ftp" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "22/open/tcp//ssh///" in D[X][Y]:
            with open("22端口ssh" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "23/open/tcp//telnet///" in D[X][Y]:
            with open("23端口telnet" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "25/open/tcp//smtp///" in D[X][Y]:
            with open("25端口smtp" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "110/open/tcp//pop3///" in D[X][Y]:
            with open("110端口pop3" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "143/open/tcp//imap///" in D[X][Y]:
            with open("143端口imap" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "445/open/tcp//microsoft-ds///" in D[X][Y]:
            #print("IP ：%s\t" % D[X][0])
            with open("445端口SMB"+ ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "465/open/tcp//smtps///" in D[X][Y]:
            with open("465端口smtps" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "993/open/tcp//imaps///" in D[X][Y]:
            with open("993端口imaps" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "995/open/tcp//pop3s///" in D[X][Y]:
            with open("995端口pop3s" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "1433/open/tcp//ms-sql-s///" in D[X][Y]:
            with open("1433端口ms-sql-s" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "1521/open/tcp//oracle///" in D[X][Y]:
            with open("1521端口oracle" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "3306/open/tcp//mysql///" in D[X][Y]:
            with open("3306端口mysql" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "3389/open/tcp//ms-wbt-server///" in D[X][Y]:
            with open("3389端口RDP" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "5432/open/tcp//postgresql///" in D[X][Y]:
            with open("5432端口postgresql" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "5900/open/tcp//vnc///" in D[X][Y]:
            with open("5900端口vnc" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "6379/open/tcp//redis///" in D[X][Y]:
            with open("6379端口redis" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "11211/open/tcp//memcache///" in D[X][Y]:
            with open("11211端口memcache" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        elif "27017/open/tcp//mongod///" in D[X][Y]:
            with open("27017端口mongod" + ".txt", "a") as IP:
                IP.write(''.join(D[X][0]).strip())
                IP.write('\n')
        '''else:
            print("所有端口均已关闭\t" )'''

