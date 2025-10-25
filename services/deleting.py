from services.searching import _search_for_action

# deleting the student in list
def Deleting(Slist):

    if not Slist:
        print(f"List is empty. Can not delete")
        return

    found_candidates = _search_for_action(Slist)

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
