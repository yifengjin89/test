# 1/2/2020
#ASCII
print(ord('a'))
print(ord('A'))
print(ord('0'))

print(chr(97))
print(chr(65))
print(chr(48))

letter = 't'  # 转换小写字母到大写
print(chr(65 + ord(letter) - 97)) # chr(ord('A') + (ord('letter') - ord('a'))
#print(letter.upper())
print("===========================================================")
n = [2,3,4,5]
for index, value in enumerate(n):
    print(index, value)
print("===========================================================")
for i in range(5):
    if i == 3:
        continue  # 将会跳过 i == 5 时的语句
    print(i)
print("===========================================================")
for i in range(5):
    if i == 3:
        break   # 将会跳出循环
    print(i)
print("===========================================================")
# random
import random

res = random.choice(range(1, 101))  # 随机数 1~100
print(res)
res2 = random.randrange(1, 101)  # 随机数 1~100
print(res2)

list1 = [1, 2, 3, 4, 5, 6] # 将序列的所有元素随机排列
random.shuffle(list1)
print(list1)

print(random.uniform(3, 9))  # 随机生成出一个3~9 的实数

# if 练习
# 从控制台输入一个整数， 判断是否是偶数

num1 = random.randrange(150, 156)
if num1 % 2 == 0:
    print("num1 = ", num1, " is even number")
else:
    print("num1 = ", num1, " is odd number")

# 闰年 ==》 能被4整除但是不能被100整除 或者 能被400整除
if (num1 % 4 == 0 and num1 % 100 != 0)  or num1 % 400 == 0:
    print('num1 = ', num1, '是闰年')
else:
    print('num1 =', num1, '不是闰年')


print("num2 = ", num1)  # 水仙花数 => 153 = 1^3 + 5^3 + 3^3
c = num1 % 10
b = num1 // 10 % 10
a = num1 // 100
if num1 == c ** 3 + b ** 3 + a ** 3:
    print("num1 是水仙花数")
else:
    print("不是水仙花数")
print("===========================================================")
str1 = "sunck is a good man sssss"
print("str1[:5] = %s " % (str1[:5]) )  # 从头截取到给定下标之前
print("good" in str1) # 判断 "good" 在 str1 里 或 否
print(str1.find("good")) # 判断 "good" 在str1 里 或 否， 并返还第一次出现的下标
print("char 's' in str1 = ", str1.count("s", 0, len(str1))) # 计算char 或者string 在某个string里出现的次数

# print  打印， 占位符  int %d,  str %s, float %f, float %.3f 精确到小数点后面3位
float1 = 10.123656
print("num1 = %d, str1 = %s, float1 = %.10f " % (num1, str1, float1))
# \n 换行符
print("num1 = %d\nstr1 = %s\nfloat1 = %.10f " % (num1, str1, float1))
# \  \ 单引号 'gggggg'
print('Tom is a \'good\' man')
print("===========================================================")

#string eval()： 将字符串str当成有效的表达式来求值并返回计算结果
num2 = eval("123")
print(num2)
print(eval("12+3"))
print(eval("12-3"))
print("===========================================================")

# while 练习
str2 = "sunck"
index = 0
while index < len(str2):
    print("str2[%d] = %s " % (index, str2[index]))
    index += 1
print("===========================================================")
# 打印所有三位数中的水仙花数
index = 100
while index < 1000:
    c = index % 10
    b = index // 10 % 10
    a = index // 100
    if index == a ** 3 + b ** 3 + c ** 3:
        print("水仙花数 = %d " % (index))
    index += 1
print("===========================================================")
count = 0
i = 10000
while i < 100000:
    e = i % 10
    d = i // 10 % 10
    b = i // 1000 % 10
    a = i // 10000
    if a == e and d == b:
        count += 1
    i += 1
print("回文数between 10000~100000 一共有: %d " %(count))
print("===========================================================")
# prime number
num3 = random.randrange(2, 20)
index = 2
while index < num3:
    if num3 % index != 0:
        print("is prime = %d" % (num3))
        break
    else:
        print("is not prime = %d" % (num3))
        break
    index += 1
print("===========================================================")
# 计算string 里面 数字的和
str3 = "1asg5dd2"
sum = 0
index = 0
while index < len(str3):
    if str3[index].isdigit():  # if str3[index] >= '0' and str3[index] <= '9':
        sum += int(str3[index])
    index += 1
print("sum = %d" % (sum))
print("===========================================================")

