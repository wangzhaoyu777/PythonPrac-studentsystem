# Zhaoyu Wang developed
# time: 2023-03-28 12:03 p.m.
import os.path

filename = 'student.txt'


def main():
    while True:
        menu()
        choice = int(input('plz select:\n'))
        if choice in range(8):
            if choice == 0:
                answer = input('Are you sure to exit?y/n:\n').lower()
                if answer == 'y':
                    print('Thank you for using')
                    break
                else:
                    continue
            elif choice == 1:
                insert()
            elif choice == 2:
                search()
            elif choice == 3:
                delete()
            elif choice == 4:
                update()
            elif choice == 5:
                sort()
            elif choice == 6:
                display_total_number()
            elif choice == 7:
                display_all_students()


def menu():
    print('Student Management System'.center(80, '='))
    print('Menu List'.center(80, '-'))
    print('Menu List'.rjust(44))
    print('1.Create student\'s information')
    print('2.Search student\'s information')
    print('3.Delete student\'s information')
    print('4.Update student\'s information')
    print('5.Organize student\'s information')
    print('6.Display the number of student')
    print('7.Display all student\'s information')
    print('0.Exit')


def insert():
    student_list = []
    while True:
        id = input('please enter ID:\n')
        if not id:
            break
        name = input('please enter name:\n')
        if not name:
            break

        try:
            english = int(input('enter English score:\n'))
            python = int(input('enter Python score:\n'))
            java = int(input('enter Java score:\n'))
        except:
            print('please enter valid number:\n')
            continue
        student = {'id': id, 'name': name, 'english': english, 'python': python, 'java': java}
        student_list.append(student)
        answer = input('continue adding?y/n:\n').lower()
        if answer == 'y':
            continue
        else:
            break

    save(student_list)
    print('finishing enter new student')


def save(lst):
    try:
        stu_txt = open(filename, 'a', encoding='UTF-8')
    except:
        stu_txt = open(filename, 'w', encoding='UTF-8')
    for item in lst:
        stu_txt.write(str(item) + '\n')
    stu_txt.close()


def search():
    pass


def delete():
    while True:
        student_id = input('enter the ID you want to delete')
        if student_id != '':
            if os.path.exists(filename):  # 判断文件是否存在 filename=student。txt
                with open(filename, 'r', encoding='utf-8') as file:  # 遍历所有信息存到student_old里面
                    student_old = file.readlines()
                    # print(student_old)
            else:
                student_old = []  # 不明白
            flag = False  # 标记是否删除   不明白
            if student_old:
                with open(filename, 'w', encoding='utf-8') as wfile:
                    d = {}
                    for item in student_old:  # 每一个item 是一个字典对应一个学生的所有信息， id english python java
                        d = dict(eval(item))  # 将字符串转换成字典 ???
                        if d['id'] != student_id:  # 重新写入数据，唯独不写要删除的一条
                            wfile.write(str(d) + '\n')
                        else:
                            flag = True
                    if flag:
                        print(f'id {student_id} has been deleted')
                    else:
                        print(f'id {student_id} is not found')
            else:
                print('no information')
                break
            display_all_students()  # 删除之后显示全部
            answer = input('continue delete?y/n ').lower()
            if answer == 'y':
                continue
            else:
                break


def update():
    display_all_students()
    if os.path.exists(filename):
        with open(filename, 'r', encoding='utf-8') as rfile:
            student_old = rfile.readlines()
    else:
        return # else下只写一个return，程序执行到这一步是会自动退出函数，
               # 即使是在一个循环体内，程序也不会在执行，此时return 相当于None即一个空值
    student_id = input('please enter the ID you want to update')
    with open(filename,'w', encoding='utf-8') as wfile:
        for item in student_old:
            d = dict(eval(item))
            if d['id'] == student_id:
                print('find it, update now!')
                while True:
                    try:
                        d['name'] = input('enter name')
                        d['english'] = input('enter English score')
                        d['python'] = input('enter Python score')
                        d['java'] = input('enter Java score')
                    except:
                        print('error, enter again')
                        continue
                    else:
                        break
                wfile.write(str(d) + '\n')
                print('update successful')
            else:
                wfile.write(str(d) + '\n')
        answer = input('do you want to update others?y/n ').lower()
        if answer == 'y':
            update()


def sort():
    pass


def display_total_number():
    pass


def display_all_students():
    pass


if __name__ == '__main__':  # 不明白
    main()
