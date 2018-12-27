dic = {"name": "xiaozhang", "sex": "male"}
try:
    print(dic["grade"])
except KeyError as e:
    print("字典中没有这个key:")
    print(e)

print(dic["name"])
print(dic["sex"])
