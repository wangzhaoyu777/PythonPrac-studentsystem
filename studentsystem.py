# Zhaoyu Wang developed
# time: 2023-03-28 12:03 p.m.

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
        student = {'id':id, 'name':name, 'english':english, 'python':python, 'java':java}
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
        stu_txt = open(filename,'a', encoding='UTF-8')
    except:
        stu_txt = open(filename,'w', encoding='UTF-8')
    for item in lst:
        stu_txt.write(str(item)+'\n')
    stu_txt.close()

def search():
    pass


def delete():
    pass


def update():
    pass


def sort():
    pass


def display_total_number():
    pass


def display_all_students():
    pass
if __name__ == '__main__': # 不明白
    main()