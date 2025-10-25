from models.student import StudentData

# add new student into students list
def Add_New(Slist):

    name = str(input("Input student name: "))

    while True:
        try:
            brith_year = int(input("Input student year: "))
            break
        except ValueError:
            print(f"Error: Birth is a integer")

    seid = str(input("Input student ID: "))
    major = str(input("Input student major: "))

    while True:
        try:
            gpa = float(input("Input student GPA: "))
            temp_gpa_check = StudentData(None, 0, None, None, gpa)
            break
        except ValueError as e:
            print(f"Value Error: {e}")

    # add all input to student list
    students = StudentData(name, brith_year, seid, major, gpa)
    Slist.append(students)
    print(f"-----------------------------")
