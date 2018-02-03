#Help U Recite English
#               ---by satori

def main():
    flag = 0
    while flag != 1 and flag != 2:
        flag = int(input("请输入你想要的功能对应的数字 1.记录 2.背诵\n"))
    if flag == 1:
        record()
    if flag == 2:
        recite()

def record():
    print("——————这是记录功能——————\n")
    file = open('recite.txt','w')
    str_c = input("请输入单词的中文\n")
    file.write('c'+str_c+'\n')
    while str_c != 'owari':
        str_e = input("请输入单词的英文\n")
        file.write('e'+str_e+'\n')
        str_c = input("请输入单词的中文\n")
        file.write('c'+str_c+'\n')
    file.close()

def recite():
    flag = True
    print("——————这是背诵功能——————\n")
    file = open('recite.txt','r')
    if flag:
        while 1:
            str_c = file.readline()
            if not str_c:
                input("词典到此结束")
            elif str_c[1] == 'e' or str_c == 'cowari':
                continue
            else:
                print(str_c[1:])
                i = 0
                answer = next(file).strip()
                while i < 3:
                    str_e = input("请拼写对应的英文\n").strip()
                    if str_e == answer[1:]:
                        print("正确\n")
                        break
                    elif str_e == 'owari':
                        break
                    else:
                        print("错误\n")
                        i = i+1
                print("答案是：",answer[1:])                
    file.close()


main()
