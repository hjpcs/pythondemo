file_read = open("D:\PyCharm\project\pythondemo\classes_and_modules\\test.txt", "r", encoding='utf-8')
print(file_read.read())
file_read.close()

file_write = open("D:\PyCharm\project\pythondemo\classes_and_modules\\test.txt", "a", encoding='utf-8')
file_write.write("today is friday!\n")
file_write.write("今天是星期五\n")
file_write.flush()
file_write.close()