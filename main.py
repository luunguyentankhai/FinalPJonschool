# Made by FIammttea and team 3
# Final project assignment subject PFP191
from Studentlist import List

#main menu
def main():
    running = True
    while running:
        #Console-Based UI
        print(f"Students in class list")
        print(f"0/ Show students list")
        print(f"1/ Add new student")
        print(f"2/ Edit student info")
        print(f"3/ Delete student info")
        print(f"4/ Search student")
        print(f"5/ Sorting student")
        print(f"6/ Exit and extract file to .txt file")
        
        #input number selection
        n = int(input(f"input number to use services: "))
        while 0> n or n>6:
            print(f"syntax error")
            n = int(input(f"please input number to use services"))

        match n: 
            case 0:
                pass
            case 1:
                pass
            case 2:
                pass
            case 3:
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                running = False
        
    

if __name__ == "__main__":
    main()



