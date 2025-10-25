from utils.validation import get_number_choice


def _search_for_action(Slist):
    print(f"\nPlease select type of finding to edit: ")
    print(f"1/ Finding by ID")
    print(f"2/ Finding by Name")

    choice = get_number_choice()

    # find by ID
    if choice == 1:
        search_ID = input(f"Input student ID to edit: ").strip()
        student = find_edit_by_ID(Slist, search_ID)
        if student:
            return [student]
        else:
            print(f"Error: Can not find student with ID")
            return []

    # find by Name
    elif choice == 2:
        search_Name = input(f"Input student Name to edit: ").strip()
        candidates = find_edit_by_Name(Slist, search_Name)

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

                student = find_edit_by_ID(candidates, verify_id)
                if student:
                    return [student]
                else:
                    print(f"Error: Can not find student with ID {verify_id}")

        else:
            return candidates

    return []


# find by ID
def find_edit_by_ID(Slist, search_ID: str):
    for student in Slist:
        if student.sid.lower() == search_ID.lower():
            return student
    return None


# find by Name
def find_edit_by_Name(Slist, search_Name: str):
    found_list = []
    for student in Slist:
        if search_Name.lower() in student.name.lower():
            found_list.append(student)
    return found_list


# searching the student in list
def Searching(Slist):
    if not Slist:
        print(f"List is empty")
        return

    found_student = _search_for_action(Slist)

    if found_student:
        print(f"\n Found {len(found_student)} result: ")
        for i, student in enumerate(found_student):
            print(f"{i+1}. {student}")
