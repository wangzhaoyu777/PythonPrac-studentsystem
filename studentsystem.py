# Zhaoyu Wang developed
# time: 2023-03-28 12:03 p.m.

def main():
    while True:
        menu()
        choice = int(input())
        if choice in range(8):
            if choice == 0:
                answer = input('Are you sure to exit?y/n').lower()
                if answer =='y':
                    print('Thank you for using')
                    break
                else:
                    continue
            elif choice==1:
                pass

def menu():
    print('Student Management System'.center(80,'='))
    print('Menu List'.center(80,'-'))
    print('Menu List'.rjust(44))
    print('1.Create student\'s information')
    print('2.Search student\'s information')
    print('3.Delete student\'s information')
    print('4.Edit student\'s information')
    print('5.Organize student\'s information')
    print('6.Display the number of student')
    print('7.Display all student\'s information')
    print('0.Exit')

def insert():
    pass
def delete():
    pass
def search():
    pass
def update():
    pass
def display_all_students():
    pass
def display_total_number():
    pass