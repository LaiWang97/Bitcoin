import csv
import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
import math

def getlist(openfile):
    with open(openfile) as csvFile:
        rows = csv.reader(csvFile)
        list_list=[]

        for row in rows:
            list_list.append(row)
    data = pd.DataFrame({
        "1 '0'": list_list[0],
        "2 '0'": list_list[1],
        "3 '0'": list_list[2],
        "4 '0'": list_list[3],
        "5 '0'": list_list[4],
        "6 '0'": list_list[5],
    })
    return data

def sub_box():
    OpenFilepwd1 = "/Users/apple/Sites/data/md5/FileAll.csv"
    data1 = getlist(OpenFilepwd1)
    OpenFilepwd2 = "/Users/apple/Sites/data/sha1/FileAll.csv"
    data2 = getlist(OpenFilepwd2)
    OpenFilepwd3 = "/Users/apple/Sites/data/sha256/FileAll.csv"
    data3 = getlist(OpenFilepwd3)
    OpenFilepwd4 = "/Users/apple/Sites/data/sha3_256/FileAll.csv"
    data4 = getlist(OpenFilepwd4)
    plt.subplot(2, 2, 1)
    sns.boxplot(data=data2,fliersize=4)
    plt.ylabel("time/ms")
    plt.xlabel("MD5")
    plt.subplot(2, 2, 2)
    sns.boxplot(data=data1,fliersize=4)
    plt.ylabel("time/ms")
    plt.xlabel("SHA1")
    plt.subplot(2, 2, 3)
    sns.boxplot(data=data3,fliersize=4)
    plt.ylabel("time/ms")
    plt.xlabel("SHA2_256")
    plt.subplot(2, 2, 4)
    sns.boxplot(data=data4,fliersize=4)
    plt.ylabel("time/ms")
    plt.xlabel("SHA3_256")
    plt.show()

if __name__ == "__main__":
    # generate 4 lists to draw
    lable = []
    md5 = []
    sha1 = []
    sha2 = []
    sha3 = []

    with open('/Users/apple/Sites/ava.csv', 'r') as file:
        # 用csv去读文件 有关csv文件的格式请自行科谱
        # csv去读取文件并不只是读取以.csv结尾的文件，它只要满足是分隔数据格式就可以了，以逗号进行分隔的数据
        plots = csv.reader(file, delimiter=',')
        for row in plots:
            lable.append(row[0])
            md5.append(float(row[1]))
            sha1.append(float(row[2]))
            sha2.append(float(row[3]))
            sha3.append(float(row[4]))

    x = list(range(len(lable)))
    total_width, n = 0.8, 4
    width = total_width / n
    plt.subplot(1, 2, 1)
    plt.bar(x, sha1, width=width, label='MD5', tick_label=lable, fc='green')
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, md5, width=width, label='SHA1', fc='red')
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, sha2, width=width, label='SHA2_256', fc='skyblue')
    for i in range(len(x)):
        x[i] = x[i] + width
    plt.bar(x, sha3, width=width, label='SHA3_256', fc='black')
    plt.legend()
    plt.xlabel('number of zeros')
    plt.ylabel('average time/ms')

    lable = []
    md5 = []
    sha1 = []
    sha2 = []
    sha3 = []

    # 打开example.txt 并且以读的方式打开
    with open('/Users/apple/Sites/ava.csv', 'r') as file:
        # 用csv去读文件 有关csv文件的格式请自行科谱
        # csv去读取文件并不只是读取以.csv结尾的文件，它只要满足是分隔数据格式就可以了，以逗号进行分隔的数据
        plots = csv.reader(file, delimiter=',')
        for row in plots:
            lable.append(row[0])
            md5.append(float(row[1]))
            sha1.append(float(row[2]))
            sha2.append(float(row[3]))
            sha3.append(float(row[4]))

    plt.subplot(1, 2, 2)
    plt.plot(lable, sha1, color='green', label="MD5")
    plt.plot(lable, sha1, "o", color='green')
    plt.plot(lable, md5, color='red', label="SHA1")
    plt.plot(lable, md5, "o", color='red')
    plt.plot(lable, sha2, color='skyblue', label="SHA2_256")
    plt.plot(lable, sha2, "o", color='skyblue')
    plt.plot(lable, sha3, color='black', label="SHA3_256")
    plt.plot(lable, sha3, "o", color='black')

    plt.legend()
    plt.xlabel('number of zeros')
    plt.ylabel('average time/ms')
    plt.show()


