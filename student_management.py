class Student:
    # creating instance of student by constructor
    def __init__(self,name,age, roll_number):
        self.name = name
        self.age = age
        self.roll_number =roll_number
class School:
     # constructor of school class
    def __init__(self):
        self.students = []
    def add_students(self,name,age,roll_number):
        # create student object
        s = Student(name, age, roll_number)
        self.students.append(s)

    def display_students(self):
        #to display all students who have been added
        for student in self.students:
            print('Name: ',student.name)
            print('Age: ', student.age)
            print('Roll Number: ', student.roll_number)
            print('-'*30)

    def edit_student(self,roll_number,new_name,new_age):
        for s in self.students:
            if s.roll_number == roll_number:
                s.name = new_name
                s.age = new_age
                print('Student will roll number {} has been edited'.format(s.roll_number))
                return
# Creating school Object
school = School()

while True:
    # take user input of student info one at a time
    choice = input('Enter your choice \n1) Add Student \n2) Display List of students \n3) Edit data \n5) Quit: \n')

    if choice =='1':
        name = input('Enter name: ')
        age = input('Enter age: ')
        roll_number = input('Enter roll number: ')

        # pass user inputs to add_students method
        school.add_students(name, age, roll_number)

    elif choice =='2':
        school.display_students()

    elif choice =='3':
        roll_num = input('Enter roll number of student yu want to edit: ')
        new_name = input('Enter new name: ')
        new_age = input('Enter new age: ')
        school.edit_student(roll_num,new_name,new_age)
    else:
        break


