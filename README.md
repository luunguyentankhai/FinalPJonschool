<div align="center">
    <img src=7.png width=400 alt="hi chat" >
</div>

- `students.txt this a test case file`

# THIS IS LAB1 PROJECT PFP191 BY GROUP 3
---
## ABOUT

- I don't know that is a final project or is a lab 1 because if is a lab 1, that is so diffcult with almost students in class.

- I fully comment all in my code so if you don't know what the fucking code mean you can ask me :>>.

- Last one, I don't write report and make presentation because I write all code you just have read this description then rewrite just fucking easy
---
## Summary Components
### 1/ Models/student.py
---
 Type | Name | Primary Role |
| :--- | :--- | :--- |
| **Class** | **StudentData** | Holds the data for a single(`Name`,`Birth`,`ID`,`Major`,`GPA`) |
| **Property** | `gpa` | The getter for the GPA attribute |
| **Setter** | `gpa` | Validates GPA range (0.0 to 4.0) before assigning the value |
| **Method** | `__init__` | Initializes the student attributes(`__name`, `__birth`, `__SID`, `__major`, `__gpa`) |
| **Method** | `__str__` | Formats data for display |
---
### 2/ Services/student_manager.py

| Type | Name | Function Description |
| :--- | :--- | :--- |
| **Class** | **StudentManager** | The main management class, handling operations on the student list (`Slist`). |
| **Variable** | `DATA_FILE` | Constant specifying the data file name (`students.txt`). |
| **Method** | `calculate_gpa(Slist)` | Calculates the average GPA of all students in `Slist`. |
| **Method** | `find_edit_by_ID(Slist, search_ID)` | Finds a student by ID (case-insensitive). |
| **Method** | `find_edit_by_Name(Slist, search_Name)` | Searches for students by name (substring search). |
| **Method** | `_search_for_action(Slist)` | Core logic to ask the user to search by ID or Name, used for Edit/Delete/Search. |
| **Method** | `_do_edit_logic(student, Slist)` | Core handler for editing and updating individual student fields. |
| **Method** | `addnew(Slist)` | Adds a new student object to `Slist`. |
| **Method** | `searching(Slist)` | Performs the search and displays results. |
| **Method** | `editing(Slist)` | Finds and edits a student's information. |
| **Method** | `deleting(Slist)` | Finds, confirms, and deletes a student from `Slist`. |
| **Method** | `sorting(Slist)` | Sorts `Slist` by Name, GPA, or Birth Year. |
| **Method** | `print_student_after(Slist)` | Displays the student list after sorting. |
| **Method** | `Input_Load(Slist)` | **(Save Data)** Saves the current `Slist` to the `.txt` file. |
| **Method** | `Output_Load()` | **(Load Data)** Loads data from the `.txt` file and returns the `Slist`. |
---
### 3/ Utils/validation.py

| Type | Name | Function Description |
| :--- | :--- | :--- |
| **Function** | `select_menu_choice()` | Gets the integer choice from the user for the main menu (0 to 7). |
| **Function** | `get_number_choice()` | Gets the integer choice for search/edit options (1: ID, 2: Name). |
---
### 4. main.py (Execution)

| Type | Name | Function Description |
| :--- | :--- | :--- |
| **Function** | `output_student_list(manager, Slist)` | Displays the entire **Slist** , including the **overall average GPA**. |
| **Function** | `main()` | The main function that starts the program, contains the core menu loop and calls service methods. |
| **Variable** | `Slist` | The main list holding the **StudentData** objects. |
| **Variable** | `manager` | The instance of the **StudentManager** class. |
---
#### THAT ALL INFO I THINK YOU NEED SO NOW DO REPORT AND PRESENTATION( I DON'T THINK TEACHER CALL WE MAKE PRESENTATION)
<div align="center">
    <img src="10.png" width=400 >
</div>