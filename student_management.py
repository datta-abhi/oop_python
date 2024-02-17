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

# Creating school Object
school = School()

while True:
    # take user input of student info one at a time
    choice = input('Enter your choice \n1) Add Student \n2) Display List of students \n3) Quit: \n')

    if choice =='1':
        name = input('Enter name: ')
        age = input('Enter age: ')
        roll_number = input('Enter roll number: ')

        # pass user inputs to add_students method
        school.add_students(name, age, roll_number)

    elif choice =='2':
        school.display_students()
    else:
        break


