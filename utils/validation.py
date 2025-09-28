# choice number to find
def get_number_choice():
    while True:
        try:
            n = int(input("Input type to do: "))
            if n in [1, 2]:
                return n
            else:
                print(f"Error these have 2 type to do: Please input a again")
        except ValueError:
            print("Error: Please input integer 1 or 2")


def select_menu_choice():
    while True:
        # input number selection and check error
        try:
            n = int(input(f"Input number to use services: "))
            # check n is a integer on 0 to 7
            if 0 <= n <= 7:
                return n
            else:
                print(f"Error: Input 0 to 7 again")
        except ValueError:
            print("Error: Please input integer 0 to 7")