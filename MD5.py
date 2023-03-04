import hashlib
import time

print("m                     #                             本程序仅作学习，切勿用于违法用途\n"
      "m                #    #\n"                    
      "#        mmm   mm#mm  # mmm   mmm\n"
      "#       #\"  #    #    #\"  #  #\"  #\n"
      "#       #\"\"\"\"    #    #   #  #\"\"\"\"\n"
      "#mmmmm  \"#mm\"    \"mm  #   #  \"#mm\"\n")


a = 0
b = 0
Judge_MD5_16bit = 0
Judge_MD5_32bit = 0
Witer_MD5 = 0
qwe = "=                     =                        ="

while True:                                         #判断MD5是否为16位或者为32位
    Original_MD5 = input("输入需要破解的MD5值：")
    if Original_MD5.islower() == True:              #判断小写MD5
        a = 1
        if len(Original_MD5) == 16:                 #判断小写MD5是不是16位
            Judge_MD5_16bit = 1
            break
        if len(Original_MD5) == 32:                 #判断小写MD5是不是32位
            Judge_MD5_32bit = 1
            break
    elif Original_MD5.isupper() == True:            #判断大写MD5
        b = 1
        print("请输入正确的36位或16位MD5值:")
        if len(Original_MD5) == 16:                 #判断大写MD5是不是16位
            Judge_MD5_16bit = 1
            break
        if len(Original_MD5) == 32:                 #判断大写MD5是不是32位
            Judge_MD5_32bit = 1
            break


while True:                                         #生成彩虹表
    MD5_Write = input("是否生成彩虹表(Y/N):")
    if MD5_Write == "Y":
        MD5_Write = 1
        break
    if MD5_Write == "N":
        break

Dict = input("输入字典绝对路径:")

tme = time.perf_counter()


if a == 1:                                          #小写MD5
    if Judge_MD5_16bit == 1:                        #再判断小写16位MD5
        with open(f"{Dict}", encoding="utf-8") as f:
            for Password in f.readlines():
                MD5 = hashlib.md5()
                MD5.update(Password.encode("utf8"))
                Password_md5 = MD5.hexdigest()
                Password_md5_2 = Password_md5[8:24]
                if Original_MD5 == Password_md5_2:
                    print(f"原密码：{Password}原MD5：{Password_md5_2}")
                if MD5_Write == 1:
                    with open('Lowercase MD5 16-bit rainbow table(小写).txt', mode='a', encoding='utf-8') as f:
                        password2 = f"加密前：{Password}加密后:{Password_md5_2}"
                        f.write(str(password2))
                        f.write('\n')
                        f.write(str(qwe))
                        f.write('\n')
                        f.close()
    elif Judge_MD5_32bit == 1:                      #判断小写32位MD5
        with open(f"{Dict}", encoding="utf-8") as f:
            for Password in f.readlines():
                MD5 = hashlib.md5()
                MD5.update(Password.encode("utf8"))
                Password_md5 = MD5.hexdigest()
                if Original_MD5 == Password_md5:
                    print(f"原密码：{Password}原MD5：{Password_md5}")
                if MD5_Write == 1:
                    with open('Lowercase MD5 32-bit rainbow table(小写).txt', mode='a', encoding='utf-8') as f:
                        password2 = f"加密前：{Password}加密后:{Password_md5}"
                        f.write(str(password2))
                        f.write('\n')
                        f.write(str(qwe))
                        f.write('\n')
                        f.close()
elif b == 1:                                         #大写MD5
    if Judge_MD5_16bit == 1:                         #判断大写16位MD5
        with open(f"{Dict}", encoding="utf-8") as f:
            for Password in f.readlines():
                MD5 = hashlib.md5()
                MD5.update(Password.encode("utf8"))
                Password_md5 = MD5.hexdigest()
                Password_md5_2 = Password_md5[8:24]
                Password_md5_3 = Password_md5_2.upper()
                if Original_MD5 == Password_md5_2:
                    print(f"原密码：{Password}原MD5：{Password_md5_2}")
                if MD5_Write == 1:
                    with open('Lowercase MD5 16-bit rainbow table(大写).txt', mode='a', encoding='utf-8') as f:
                        password2 = f"加密前：{Password}加密后:{Password_md5_3}"
                        f.write(str(password2))
                        f.write('\n')
                        f.write(str(qwe))
                        f.write('\n')
                        f.close()
    elif Judge_MD5_32bit == 1:                        #判断大写32位MD5
        with open(f"{Dict}", encoding="utf-8")as f:
            for Password in f.readlines():
                MD5 = hashlib.md5()
                MD5.update(Password.encode("utf8"))
                Password_md5 = MD5.hexdigest()
                Password_md5_2 = Password_md5.upper()
                if Original_MD5 == Password_md5_2:
                    print(f"原密码：{Password}原MD5：{Password_md5_2}")
                if MD5_Write == 1:
                    with open('Lowercase MD5 32-bit rainbow table(大写).txt', mode='a', encoding='utf-8') as f:
                        password2 = f"加密前：{Password}加密后:{Password_md5_2}"
                        f.write(str(password2))
                        f.write('\n')
                        f.write(str(qwe))
                        f.write('\n')
                        f.close()


tme2 = time.perf_counter()
print(f"耗时: {tme2 - tme:0.4f} seconds")


