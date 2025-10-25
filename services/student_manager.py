from models.student import StudentData

# check permision
from utils.check_permision import Check_permision

# Components
from services.adding import Add_New
from services.editing import Editing
from services.searching import Searching
from services.deleting import Deleting
from services.calculating import Average_GPA, statistics
from services.sorting import Sorting
from services.IO_services import Save_File, Load_File


class StudentManager:

    def __init__(self, user_lg):
        self.user_lg = user_lg

    def _check_permision(self, key_permission):
        return Check_permision(self.user_lg, key_permission)

    # Adding function
    def addnew(self, Slist):
        if self._check_permision("add"):
            Add_New(Slist)

    # Editing function
    def editing(self, Slist):
        if self._check_permision("edit"):
            Editing(Slist)

    # Searching function
    def searching(self, Slist):
        Searching(Slist)

    # Deleting function
    def deleting(self, Slist):
        if self._check_permision("delete"):
            Deleting(Slist)

    # Sorting function
    def sorting(self, Slist):
        Sorting(Slist)

    # Calculating gpa function
    def classification_gpa(self, Slist):
        aver = Average_GPA(Slist)
        classification = statistics(Slist)

        print(f"\n---GPA STATISTICS---\n")
        print(f"Average GPA (All student): {aver}")
        print(f"\nGPA Classification")

        total_student = len(Slist)
        for catergory, count in classification.items():
            percent = (count / total_student) * 100 if total_student > 0 else 0
            bar = "█" * int(percent / 2)
            print(f"{catergory:<22} | {count:3} students | {bar} ({percent:.1f}%)")
        print(f"--------------------------")

    # Write Slist into file .txt
    def Savefile(self, Slist):
        if self._check_permision("io"):
            Save_File(Slist)

    # Load file from file .csv or .txt
    def Loadfile(self):
        return Load_File()
