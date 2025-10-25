from services.searching import _search_for_action, find_edit_by_ID


# logic editing core
def _do_edit_logic(student, Slist):
    print(f"--=Editing student infomation=--")

    # edit new ID
    origin_sid = student.sid
    while True:
        new_sid = input(f"Input a new ID (None to not change {student.sid}): ").strip()
        if not new_sid:
            break

        # check ID duplication
        if new_sid.lower() != origin_sid.lower():
            if find_edit_by_ID(Slist, new_sid):
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
    new_major = input(f"Input new major (None to not change {student.major}): ").strip()
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


# editing the student in list
def Editing(Slist):
    if not Slist:
        print("List is empty. Can not edit")
        return

    found_candidates = _search_for_action(Slist)

    if found_candidates:
        student_to_edit = found_candidates[0]
        _do_edit_logic(student_to_edit, Slist)
    else:
        pass
