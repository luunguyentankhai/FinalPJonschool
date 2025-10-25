# print_student after sorting
def print_student_after(Slist):
    print("\n--=Student List After Sorting=--")
    if not Slist:
        return
    for student in Slist:
        print(student)
    print(f"-----------------------------")

# sorting the student in class
def Sorting(Slist):
    if not Slist:
        print("List is empty. Can not sort")
        return

    print(f"\nSelect sorting criteria")
    print(f"1. Sorting by Name(A-Z)")
    print(f"2. Sorting by GPA(Ascending to Descending)")
    print(f"3. Sorting by Birth Year(Young to Old)")

    while True:
        try:
            choice = int(input("Select criteria: "))
            if choice in [1, 2, 3]:
                break
            else:
                print(f"Error: Select invalid. Please select 1,2 or 3 again")
        except ValueError:
            print(f"Error: Please input a integer")

    if choice == 1:
        Slist.sort(key=lambda student: student.name.lower())
        print("Sorting by Name successful")

    elif choice == 2:
        Slist.sort(key=lambda student: student.gpa, reverse=True)
        print("Sorting by GPA successful")

    elif choice == 3:
        Slist.sort(key=lambda student: student.birth, reverse=True)
        print("Sorting by Birth Year successful")

    print_student_after(Slist)
