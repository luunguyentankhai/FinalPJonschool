Permission = {
    "ADMIN": ["add", "edit", "delete", "search", "sort", "gpa", "io"],
    "TEACHER": ["add", "edit", "delete", "search", "sort", "gpa", "io"],
    "STUDENTS": ["search", "sort", "gpa"],
}


def Check_permision(user_lg, key_permission):
    if key_permission in Permission.get(user_lg, []):
        return True
    print(f"\nAccess Denied: Role {user_lg} cannot perform '{key_permission}'.")
    return False
