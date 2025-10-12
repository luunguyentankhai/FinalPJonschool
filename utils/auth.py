def authenticate_user():
    MAX_ATTEMPTS = 3
    

    User = {
        "TEACHER": ("TEACHER", "teaching"),
        "STUDENTS": ("STUDENTS", "student123"),
    }

    for attempts in range(1, MAX_ATTEMPTS + 1):
        print(f"\nLogin Attempt {attempts}/{MAX_ATTEMPTS}")
        username = str(input()).strip()
        password = str(input()).strip()

        if username in User:
            lg, pw = User[username]
            if password == pw:
                print(f"\nLogin successful! Role: {lg}.")
                return lg

        print("Invalid username or password. Please try again.")

    print("\nMaximum login attempts reached. Exiting program.")
    return None
