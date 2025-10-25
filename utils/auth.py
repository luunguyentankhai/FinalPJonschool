from models.user import User
from models.role import Role
import utils.security as security

Res_User = {
    User(
        username="ADMIN",
        password="2607279acdf5f6c9580f3f3777439be9:4cb40014b947ef3c886c1818873141fee8bffb8c5b63245cb24b40eb95257bd4",
        role=Role.ADMIN,
    ),
    User(
        username="TEACHER",
        password="0466c635abe2cf87dbab40c1f482f0f9:a7d7ad78f10cc3dd822e1282a1faaf57bfd4436fa0acbed9a5eba3eadff7d5c1",
        role=Role.TEACHER,
    ),
    User(
        username="STUDENT",
        password="2508648613e58b1672dcb4679e39daac:ccc2b392141f1e616859e8082f564358be86370f920e97c8f0815f24c9056c3f",
        role=Role.STUDENT,
    ),
}


def authenticate_user():
    MAX_ATTEMPTS = 3

    for attempts in range(1, MAX_ATTEMPTS + 1):
        print(f"\nLogin Attempt {attempts}/{MAX_ATTEMPTS}")
        username_inp = str(input()).strip()
        password_inp = str(input()).strip()

        found_ur = None

        for user in Res_User:
            if user.username == username_inp:
                found_ur = user
                break

        if found_ur and security.check_PW(password_inp, found_ur.password):
            print(f"\nLogin successful! Role: {found_ur.role.name}")
            return found_ur.role
        

        print("Invalid username or password. Please try again.")

    print("\nMaximum login attempts reached. Exiting program.")
    return None
