import random
from Studentlist import ManagerList

class addnew:
    def __init__(self,):
        self.students = []
         
    def ma(self):
        num = ["0","1","2","3","4","5","6","7","8","9"]
        mssv = random.choice(num)
        for j in range (0,9):
            mssv += random.choice(num)  
        return mssv

    def add(self, name, birth, major, gpa):
        students_id = addnew.ma()
        new_students = ManagerList(name,birth,students_id,major,gpa)
        self.students.append(new_students)
        print(f"Add new success students: {new_students.__name}")

    def search(self, name):
        name = name.lower()
        find_students = [
            i for i in self.students
            if name in i.name.lower()
        ]

        if not find_students:
            print(f"Not student search in list")
        else:
            print(f"Found {len(find_students)}")



        