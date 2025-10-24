from models.student import StudentData
from utils.validation import get_number_choice
import os


DEFAULT_DATA_FILE = "students.txt"


class StudentManager:

    Permission = {
        "TEACHER": ["add", "edit", "delete", "search", "sort", "gpa", "io"],
        "STUDENTS": ["search", "sort", "gpa"],
    }

    def __init__(self, user_lg):
        self.user_lg = user_lg

    # check access denied
    def _check_permision(self, key_permission):
        if key_permission in self.Permission.get(self.user_lg, []):
            return True
        print(f"\nAccess Denied: Role {self.user_lg} cannot perform '{key_permission}'.")
        return False

    # print_student after sorting
    def print_student_after(self, Slist):
        print("\n--=Student List After Sorting=--")
        if not Slist:
            return
        for student in Slist:
            print(student)
        print(f"-----------------------------")

    # find for editing, searching, deleting and sorting core
    def _search_for_action(self, Slist):
        print(f"\nPlease select type of finding to edit: ")
        print(f"1/ Finding by ID")
        print(f"2/ Finding by Name")

        choice = get_number_choice()

        # find by ID
        if choice == 1:
            search_ID = input(f"Input student ID to edit: ").strip()
            student = self.find_edit_by_ID(Slist, search_ID)
            if student:
                return [student]
            else:
                print(f"Error: Can not find student with ID")
                return []

        # find by Name
        elif choice == 2:
            search_Name = input(f"Input student Name to edit: ").strip()
            candidates = self.find_edit_by_Name(Slist, search_Name)

            if not candidates:
                print(f"Can not find student name: {search_Name}")
                return []

            elif len(candidates) > 1:
                print("Found many result: ")

                for i, student in enumerate(candidates):
                    print(f"{i+1}. {student}")

                while True:
                    verify_id = input("Please verity correct student ID: ").strip()

                    if not verify_id:
                        print("Cancel search")
                        return []

                    student = self.find_edit_by_ID(candidates, verify_id)
                    if student:
                        return [student]
                    else:
                        print(f"Error: Can not find student with ID {verify_id}")

            else:
                return candidates

        return []

    # logic editing core
    def _do_edit_logic(self, student, Slist):
        print(f"--=Editing student infomation=--")

        # edit new ID
        origin_sid = student.sid
        while True:
            new_sid = input(
                f"Input a new ID (None to not change {student.sid}): "
            ).strip()
            if not new_sid:
                break

            # check ID duplication
            if new_sid.lower() != origin_sid.lower():
                if self.find_edit_by_ID(Slist, new_sid):
                    print(f"Error ID {new_sid} exists in list ")
                    continue
            # check done and replace new ID
            student.sid = new_sid
            break

        # edit new name
        new_name = input(
            f"Input new student Name (None to not change {student.name}): "
        ).strip()
        if new_name:
            student.name = new_name

        # edit new birth
        while True:
            new_birth_str = input(
                f"Input new birth (None to not change {student.birth}):"
            ).strip()

            if not new_birth_str:
                break
            try:
                student.birth = int(new_birth_str)
                break
            except ValueError:
                print("Error: Birth is a integer please input again")

        # edit new major
        new_major = input(
            f"Input new major (None to not change {student.major}): "
        ).strip()
        if new_major:
            student.major = new_major

        # edit GPA
        while True:
            new_GPA_str = input(
                f"Input new GPA (None to not change {student.gpa}): "
            ).strip()

            if not new_GPA_str:
                break
            try:
                new_gpa = float(new_GPA_str)
                student.gpa = new_gpa
                break
            except ValueError as e:
                print(f"Error: GPA is a float (error value {e}) please input again")

        print("\nEditint successful")
        print(student)

    # find by ID
    def find_edit_by_ID(self, Slist, search_ID: str):
        for student in Slist:
            if student.sid.lower() == search_ID.lower():
                return student
        return None

    # find by Name
    def find_edit_by_Name(self, Slist, search_Name: str):
        found_list = []
        for student in Slist:
            if search_Name.lower() in student.name.lower():
                found_list.append(student)
        return found_list

    # Services in menu list
    # add new student into students list
    def addnew(self, Slist):

        if not self._check_permision("add"):
            return

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

    # searching the student in list
    def searching(self, Slist):
        if not Slist:
            print(f"List is empty")
            return

        found_student = self._search_for_action(Slist)

        if found_student:
            print(f"\n Found {len(found_student)} result: ")
            for i, student in enumerate(found_student):
                print(f"{i+1}. {student}")

    # editing the student in list
    def editing(self, Slist):
        if not self._check_permision("edit"):
            return

        if not Slist:
            print("List is empty. Can not edit")
            return

        found_candidates = self._search_for_action(Slist)

        if found_candidates:
            student_to_edit = found_candidates[0]
            self._do_edit_logic(student_to_edit, Slist)
        else:
            pass

    # deleting the student in list
    def deleting(self, Slist):
        if not self._check_permision("delete"):
            return

        if not Slist:
            print(f"List is empty. Can not delete")
            return

        found_candidates = self._search_for_action(Slist)

        if found_candidates:
            student_to_delete = found_candidates[0]
            print(f"Do you sure to delete student:")
            print(f"Name: {student_to_delete.name} \nID: {student_to_delete.sid}")

            confirmation = input(f"Accept to delete (Y/N): ").strip().upper()

            if confirmation == "Y":
                Slist.remove(student_to_delete)
                print(
                    f"Delete student {student_to_delete.name} id {student_to_delete.sid} successful"
                )
            else:
                print(f"Cancel delete student")
        else:
            pass

    # sorting the student in class
    def sorting(self, Slist):
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

        self.print_student_after(Slist)

    # Calculate Average GPA student
    def calculate_gpa(self, Slist):
        if not Slist:
            return 0.0

        total_gpa = sum(student.gpa for student in Slist)
        return total_gpa / len(Slist)

    # Save/Load file
    def Input_Load(self, Slist):
        if not self._check_permision("io"):
            return

        try:
            with open(DEFAULT_DATA_FILE, "w", encoding="utf-8") as f:
                f.write("Name,Birth,SID,Major,GPA\n")

                for student in Slist:
                    line = f"{student.name},{student.birth},{student.sid},{student.major},{student.gpa}\n"
                    f.write(line)

            print(f"Save date into file successful: {DEFAULT_DATA_FILE}")

        except Exception as e:
            print(f"Error to save into file: {e}")

    def Output_Load(self):
        Slist_Loaded = []

        while True:
            file_to_load = input(
                "Input file name to load(data.csv, info.txt): "
            ).strip()

            if file_to_load.lower() == DEFAULT_DATA_FILE.lower():
                print(f"Error: Cannot load default file to save {DEFAULT_DATA_FILE}")
                continue

            if not file_to_load.lower().endswith((".csv", ".txt")):
                print(f"Error: File must be .csv or .txt")
                continue
            break

        if os.path.exists(file_to_load):
            try:
                with open(file_to_load, "r", encoding="utf-8") as f:
                    next(f)

                    for line in f:
                        fields = line.strip().split(",")
                        if len(fields) == 5:
                            sid = fields[2]
                            name = fields[0]
                            try:
                                birth = int(fields[1])
                                major = fields[3]
                                gpa = float(fields[4])
                            except ValueError:
                                print(f"Skip ValueError: {line.strip()}")
                                continue
                            student = StudentData(name, birth, sid, major, gpa)
                            Slist_Loaded.append(student)
                print(
                    f"Load data successful for {file_to_load}. ({len(Slist_Loaded)} student)"
                )
                return Slist_Loaded

            except Exception as e:
                print(f"Error loading data: {e}. Start with Empty List")
                return []
        else:
            print(f"File data {file_to_load} not exists. Start with Empty List")
            return []
