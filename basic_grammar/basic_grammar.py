# 1
# pip install requests
# 在/Lib/site-packages目录下查看是否有requests目录即可确认是否安装成功

# 2
a = 2.918
print(a)
print(type(a))
a = int(a)
print(a)
print(type(a))
print('*'*50)

# 3
a = 18
print('18的二进制数是'+bin(a))
print('*'*50)

# 4
str = 'Python is popular'
print(str.replace('Python', 'java', 1))
print((str.replace('Python', 'java', 1)).replace('java', 'JAVA'))
# 把字符串中的 old（旧字符串） 替换成 new(新字符串)，如果指定第三个参数max，则替换不超过 max 次
print('*'*50)

# 5
list_ = [1, 2, 3, 4, 5, 6, 7, 8]
for i in list_:
    if (i % 2) == 0:
        print(i)
print('*'*50)

# 6
dic = {'name': 'xiaohuang', 'sex': 'male', 'province': 'shanghai'}
print(dic)
dic['province'] = '江苏'
print(dic)
print('*'*50)

# 7
test_str = "Python was   created in 1989,Python is   using in AI,big data,IOT."
print(test_str)
print(test_str.lower())
test_str = test_str.replace(",", " ")
test_str = test_str.replace(".", " ")
test_str_split = test_str.split(" ")
print(test_str_split)
while "" in test_str_split:
    test_str_split.remove("")
print(test_str_split)
len = len(test_str_split)
print(int(len/2))
print(test_str_split[(int(len/2))])
print('*'*50)

# 8
list1 = ["python", 5, 6, 8]
list2 = ["python", "5", 6, 8, 10]
list3 = list1+list2
print(list3)
set1 = set(list3)
print(set1)
list4 = list(set1)
print(list4)
