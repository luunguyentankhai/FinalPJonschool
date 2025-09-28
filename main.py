# Made by Team 3
# Student name : Lưu Nguyễn Tấn Khải SE203817
# Student name : Nguyễn Nhật Huy SE203829
# Student name : Nguyễn Phạm Mai Phương SE204019
# Student name : Lê Nam Phong SE 204029
# Lab1 subject PFP191

#@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@@@@~~~*@@@@@@@@@@@@@@@@@@@@@@
#@@@@@@@@@@@@@@@@@@@@@8~~~$~~~o$@@@@@@@@@@i1@@@@@@@
#@@@@@@@@@@@@@@@@@&3$$#~~~&&n&~&$$$$$$86@@@@$@@@@@@
#@@@@@@@@@@@@@6$$$$$$$$8~~13&v~&$$$$$$$$#%@6zn@@@@@
#@@@@@@@@@@3$$$$$$$$$$$$1~~~z~~$$$$$$$$&1na@i@@@@@@
#@@@@@@@#8$$$$$$$$$$$$$##i~vi8$@@#&&&@&#1v3@31@@@@@
#@@@@@@%$$$$$$$$$$#&#$$$$$$$$$$$$$$$$$$$@13%~@@@@@@
#@@@@@%&&$$$$$#&$$$$$$$$$$$&@@&%8%$#@#$$$$#%81a@@@@
#@@@@@@%&&$#&$$$$$$$##88!iiiiiiiiizzii883##%&i1@@@@
#@@@@@@@&#@$$$$$&888izzz8aiiii3zizauii3ii3#&&@@&@@@
#@@@@@@@@&&$$@883iiiazz3vuzzzzu%ziiiiii$iiu&@&@@@@@
#@@@@@@@&&3#8$iiiiiiiii;.3ii6ii8#ii!iii8iii@@&&%@@@
#@@@@@@@3&&8i!iii8iii6@..*1ii8ii6 8i6!i8iiiz@@&&&@@
#@@@@@@@$&&i3iiiiii68 .....$ii@ii8 ..-. iii1#&6@@@@
#@@@@@@@#&&i%iiiii$n6866$-...$8i.3$u33-%i3i6i8@@@@@
#@@na&#&&&@i3iiiiii.------.......-----oiiii$iii@@@@
#@@@@@@@@@iii%iii6ii!+-----;;~;~..----*iii8v#$ @@@@
#@@@@@@iiiii88o8iii6&.....;;;;;;...... #$$$@-u @@@@
#@@@@@@@@@iiii8%@88$ .....*;;;;u.....$$&$$8!o^v&1@@
#@@@@@@!!!!!ii88@i6i!@@#1 . uo..+8$#3iz6#$$n!&.@.@@
#@@@!!!6$8!!!!!8@@!8!!!&#&@%%%#&&#$iii16$$$!6.^.u@@
#@@@@@@%%%!!8!!!!3%!!3!!!!@&&#&&$#i!!i!6&$$$$.. &@@
#@@@@@@@@%%3!38!!866666@@$@888666#!!63%%#$$$$@@#@@@
#@@@@@@@@@@@$3333%8666@$$666$$@$%@@@%%%&%%@@@@@@@@@

from services.student_manager import StudentManager
from utils.validation import select_menu_choice

def output_student_list(manager, Slist):
    if not Slist:
        print(f"List is empty")
        return
    print(f"--=Student list=--")
    for i, student in enumerate(Slist):
        print(f"{i+1}. {student}")

    overall_gpa = manager.calculate_gpa(Slist)

    print(f"-----------------------------")
    print(f"TOTAL students: {len(Slist)} | Average GPA: {round(overall_gpa,2)}")
    print(f"-----------------------------")

def main():
    # call the StudentManager
    manager = StudentManager("", "", 0, "", 0.0)

    # create a list to input and output student
    Slist = manager.Output_Load()

    running = True
    while running:
        # Console-Based UI
        print(f"\n")
        print(f"Menu to manage students list:")
        print(f"0/ Show students list")
        print(f"1/ Add new student")
        print(f"2/ Edit student info")
        print(f"3/ Delete student info")
        print(f"4/ Search student")
        print(f"5/ Sorting student")
        print(f"6/ Calculate GPA (Average GPA)")
        print(f"7/ Exit and extract file to .txt file")
        print(f"\n")

        n = select_menu_choice()

        match n:
            case 0:
                output_student_list(manager, Slist)
            case 1:
                print(f"Please input new student: ")
                manager.addnew(Slist)
            case 2:
                manager.editing(Slist)
            case 3:
                manager.deleting(Slist)
            case 4:
                manager.searching(Slist)
            case 5:
                manager.sorting(Slist)
            case 6:
                overall_gpa = manager.calculate_gpa(Slist)
                print(f"Average GPA all student: {round(overall_gpa,2)}")
            case 7:
                manager.Input_Load(Slist)
                print("Programming exit...")
                running = False


if __name__ == "__main__":
    main()



