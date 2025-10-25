import os
from models.student import StudentData
from pathlib import Path


# Absolute PATH
curr_dir = Path(__file__)
Service_dir = curr_dir.parent
Project_dir = Service_dir.parent
Data_dir = Project_dir / "data"

Data_dir.mkdir(parents=True, exist_ok=True)

DEFAULT_DATA_FILE = Data_dir / "students.csv"


# Save file
def Save_File(Slist):
    try:
        with open(DEFAULT_DATA_FILE, "w", encoding="utf-8") as f:
            f.write("Name,Birth,SID,Major,GPA\n")

            for student in Slist:
                line = f"{student.name},{student.birth},{student.sid},{student.major},{student.gpa}\n"
                f.write(line)

        print(f"Save date into file successful: {DEFAULT_DATA_FILE}")

    except Exception as e:
        print(f"Error to save into file: {e}")


# Load file
def Load_File():
    Slist_Loaded = []

    while True:
        file_to_load = input("Input file name to load(data.csv, info.txt): ").strip()

        if file_to_load.lower() == DEFAULT_DATA_FILE.name.lower():
            print(f"Error: Cannot load default file to save {DEFAULT_DATA_FILE}")
            continue

        if not file_to_load.lower().endswith((".csv", ".txt")):
            print(f"Error: File must be .csv or .txt")
            continue
        break

    full_load_path = Data_dir / file_to_load

    if os.path.exists(full_load_path):
        try:
            with open(full_load_path, "r", encoding="utf-8") as f:
                next(f)

                for line in f:
                    fields = line.strip().split(",")
                    if len(fields) == 5:
                        sid = fields[2]
                        name = fields[0]
                        try:
                            birth = int(fields[1])
                            major = fields[3]
                            gpa = float(fields[4])
                        except ValueError:
                            print(f"Skip ValueError: {line.strip()}")
                            continue
                        student = StudentData(name, birth, sid, major, gpa)
                        Slist_Loaded.append(student)
            print(
                f"Load data successful for {full_load_path}. ({len(Slist_Loaded)} student)"
            )
            return Slist_Loaded

        except Exception as e:
            print(f"Error loading data: {e}. Start with Empty List")
            return []
    else:
        print(f"File data {full_load_path} not exists. Start with Empty List")
        return []
