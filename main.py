# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


# def print_hi(name):
#     # Use a breakpoint in the code line below to debug your script.
#     print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.
#
#
# # Press the green button in the gutter to run the script.
# if __name__ == '__main__':
#     print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/

def openfile():
    with open('student.txt','r', encoding='utf-8') as file:
        d = {}
        student_old = file.readlines()
        for item in student_old:  # 每一个item 是一个字典对应一个学生的所有信息， id name english python java
            d = eval(item)  # 将字符串转换成字典
        print(d)

openfile()