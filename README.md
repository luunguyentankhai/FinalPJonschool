<div align="center">
    <img src=7.png width=400 alt="hi chat" >
</div>

# LOGIN ACCOUNT TESTING
|UserName|PassWord|
|:---:|:---:|
|TEACHER|teaching|
|STUDENTS|student123|

---
# THIS IS FINAL PROJECT PFP191 BY GROUP 3
---
## 1. INTRODUCTION

### 1.1 DESCRIPTION
- The project develops a **Student Management System** using the Python programming language.
- The program allows managing student records, entering grades and calculating GPA, searching, sorting, saving/reading data from files, while applying object-oriented programming (OOP), exception handling, and templates.

### 1.2 PROJECT TEAM 
| # | Student ID | Full Name | Completion Level | Task Performed |
| :--- | :--- | :--- | :--- | :--- |
|1|**SE203817**|**Lưu Nguyễn Tấn Khải**|100%|100%|
|2|**SE203829**|**Nguyễn Nhật Huy**|100%|100%|
|3|**SE204019**|**Nguyễn Phạm Mai Phương**|100%|100%|
|4|**SE204029**|**Lê Nam Phong**|100%|100%|

---
## 2. REQUIREMENT ANALYSIS & DECOMPOSITION

### 2.1 DATA

| # | Name | Description |
| :---: | :--- | :--- |
| **1** | **Code** | Student ID (The unique identifier for each student record). |
| **2** | **Data File** | `students.txt` (The file used for persistent storage). |
| **3** | **Data File** | `Input.csv` (The file used for load input)|

### 2.2. Functions

| # | Function | Description |
| :---: | :--- | :--- |
| **1** | **Student Management** | Manage students (Core CRUD operations and data manipulation). |

#### 2.2.1 Sub-functions of Student Management

To manage the student list effectively, the system must include the following sub-functions:

* **addStudent:** Add a new student record to the list.
* **editStudent:** Modify the information of an existing student.
* **deleteStudent:** Remove a student record from the list.
* **searchStudent:** Find students based on specific criteria (ID or Name).
* **sortStudent:** Arrange the student list based on a selected field (Name, GPA, etc.).
* **calculateGPA:** Calculate the overall average GPA of all students in the list.
* **fileIO:** Handle data persistence (reading from/writing to files).

---
## 3. ALGORITHM DESIGN & FLOWCHARTS

#### FLowChart Main.py
```mermaid
    graph TD
    A["Start: main()"] --> L{"Call authenticate_user()"};
    
    L -- "Returns None (Fails)" --> F[Exit Program];
    
    L -- "Returns Role (Success)" --> R[Save user_lg];
    R --> B("Initialize StudentManager(user_lg)");
    B --> C("Load Data: manager.Output_Load()");
    C --> D{"Main Loop: choice != 7"};

    %% Main function branches
    D -- "Yes" --> E("Display Menu and Get choice (0-7)");
    
    E --> G{"Check choice"};
    
    G -- "0: Display" --> G0("output_student_list(manager, Slist)");
    G -- "1: Add" --> G1("manager.addnew(Slist)"); 
    G -- "2: Edit" --> G2("manager.editing(Slist)");
    G -- "3: Delete" --> G3("manager.deleting(Slist)");
    G -- "4: Search" --> G4("manager.searching(Slist)");
    G -- "5: Sort" --> G5("manager.sorting(Slist)");
    G -- "6: GPA" --> G6("manager.calculate_gpa(Slist)");
    
    %% Return to loop (Quyền đã được kiểm tra bên trong G1-G6)
    G0,G1,G2,G3,G4,G5,G6 --> D;

    %% Program Exit
    G -- "7: Exit" --> N("Save Data: manager.Input_Load(Slist)");
    N --> O["End"];
    D -- "No" --> O;
```
---
#### FlowChart Services/Students_Manager.py

###### Function _search_for_action
```mermaid
    graph TD
    A[Start: Search Action] --> B{Get Search Type: ID or Name};

    %% -------------------- ID Branch --------------------
    B -- "ID (1)" --> C[Input search ID];
    C --> D{Student Found by ID?};
    
    D -- "Found" --> E[Return Student Object];
    D -- "Not Found" --> F[Print Error: ID Not Found] & F --> G[Return Empty List];

    %% -------------------- Name Branch --------------------
    B -- "Name (2)" --> H[Input search Name];
    H --> I[Candidates = Find by Name];
    
    I --> J{Candidates is empty?};
    J -- "Yes" --> F; 

    I --> K{Candidates > 1?};

    %% Multiple Results Case (Name Duplicates)
    K -- "Yes" --> L[Display all candidates];
    L --> M{Loop: Verify ID?};
    
    M -- "Enter to Cancel" --> O[Print Cancel] & O --> G;
    M -- "Input ID" --> P{ID found in Candidates list?};
    
    P -- "Found" --> E;
    P -- "Not Found" --> Q[Print Error: Invalid ID] & Q --> M;
    
    %% Single Result Case
    K -- "No" --> E;
```
---
###### Function _do_edit_logic
```mermaid
    graph TD
    A["Start: _do_edit_logic(student)"] --> B["Print current data of student"];
    
    B --> C{"Loop: Display fields to edit"};
    C --> D{"Get user choice (1-5 or 0 to finish)"};

    D -- "Choice 0 (Finish)" --> E["Exit Edit Flow"];
    E --> Z["End"]; 

    D -- "Choice 1-5" --> F["Call appropriate validate_function"];
    F --> G{"Validation Successful?"};
    
    G -- "No" --> C;
    
    G -- "Yes" --> H["Update student.attribute"];
    H --> I["Print 'Update successful'"];
    I --> C;

    D -- "Invalid Choice" --> C;
```
---
###### Function Addnew
```mermaid
    graph TD
    A["Start: addnew(Slist)"] --> B{"_check_permision('add')"};
    
    B -- "False (Access Denied)" --> Z[Return];
    
    B -- "True" --> C["Input Name, Birth, ID, Major"];
    C --> D{"Input and Validate GPA"};
    
    D -- "Invalid (ValueError)" --> D;
    D -- "Valid" --> E["Create StudentData object"];
    E --> F["Slist.append(student)"];
    F --> G["Print 'Successful'"];
    G --> Z;
```
---
###### Function Editing
```mermaid
    graph TD
    A["Start: editing(Slist)"] --> B{"_check_permision('edit')"};
    
    B -- "False (Access Denied)" --> Z[Return];
    
    B -- "True" --> C{"Is Slist empty?"};
    C -- "Yes" --> Z;
    
    C -- "No" --> D["Call _search_for_action(Slist)"];
    D --> E{Found Candidates?};
    
    E -- "No" --> Z;
    E -- "Yes" --> F["student_to_edit = candidates[0]"];
    F --> G["Call _do_edit_logic(student_to_edit, Slist)"];
    G --> Z;
```
---
###### Function Deleting
```mermaid
    graph TD
    A["Start: deleting(Slist)"] --> B{"_check_permision('delete')"};
    
    B -- "False (Access Denied)" --> Z[Return];
    
    B -- "True" --> C{"Is Slist empty?"};
    C -- "Yes" --> Z;
    
    C -- "No" --> D["Call _search_for_action(Slist)"];
    D --> E{Found Candidates?};
    
    E -- "No" --> Z;
    E -- "Yes" --> F["student_to_delete = candidates[0]"];
    F --> G["Prompt Confirmation (Y/N)"];
    
    G -- "N/Other" --> H["Print 'Cancel delete'"];
    H --> Z;
    
    G -- "Y" --> I["Slist.remove(student_to_delete)"];
    I --> J["Print 'Delete successful'"];
    J --> Z;
```
---
###### Function Searching
```mermaid
    graph TD
    A["Start: searching(Slist)"] --> B{"candidates = _search_for_action(Slist)"};
    
    B -- "Search Fails" --> C["Print "No students matched criteria.""];
    C --> Z[End];
    
    B -- "Search Success" --> D["Display candidates list"];
    D --> Z;
```
---
###### Function Sorting
```mermaid
    graph TD
    A["Start: sorting(Slist)"] --> B["Print Sorting Menu (Name, GPA, Birth Year)"];
    B --> C{"Get user choice (1-3)"};
    
    C -- "Invalid Choice" --> B;

    C -- "Valid Choice" --> D["Perform Slist.sort() based on choice"];
    D --> E["Print "Sorting successful!""];
    E --> F["Display sorted list"];
    F --> Z[End];
```
---
###### Function Calculate GPA
```mermaid
    graph TD
    A["Start: calculate_gpa(Slist)"] --> B{Is Slist empty?};

    B -- "Yes" --> C["Return 0.0"];
    C --> Z[End];

    B -- "No" --> D["Initialize total_gpa = 0.0"];
    D --> E{"Loop through each student in Slist"};

    E --> F["total_gpa = total_gpa + student.gpa"];
    F --> E;

    E --> G["Calculate average = total_gpa / len(Slist)"];
    G --> H["Print average GPA"];
    H --> I["Return average GPA"];
    I --> Z;
```
---
###### Functions Input/Output system

- <strong>INPUT</strong>
```mermaid
    graph TD
    A["Start: Input_Load(Slist)"] --> B{"_check_permision('io')"};
    
    B -- "False (Access Denied)" --> Z[Return];
    
    B -- "True" --> C["Open DEFAULT_DATA_FILE ('w')"];
    C --> D["Write Header Line"];
    D --> E["Loop through Slist"];
    E --> F["Write each student data line"];
    F --> E;
    
    E --> G["Close file"];
    G --> H["Print 'Save successful'"];
    H --> Z;
```
- <strong>OUTPUT</strong>
```mermaid
    graph TD
    A["Start: Output_Load"] --> B["Find all .csv and .txt files"];
    B --> C["Filter: Remove students.txt"];
    
    C --> D{"Loadable files found?"};
    
    D -- "No" --> E["Print 'No files found'"];
    E --> Z["Return Empty List"];
    
    D -- "Yes" --> F["Display list of files with numbers"];
    F --> G{"Get User Selection"};
    
    G -- "Select 0 (Skip)" --> Z;
    G -- "Select File (1-N)" --> H{"Is Selection Valid?"};
    
    H -- "No" --> G;
    
    H -- "Yes" --> I["Select file_to_load"];
    I --> J["Open and Read file"];
    
    J --> K{"Error Reading or Formatting?"};
    
    K -- "Yes" --> L["Print Error"] & L --> Z;
    
    K -- "No" --> M["Process data line by line"];
    M --> N["Create StudentData objects"];
    N --> O["Append to Slist_Loaded"];
    O --> P["Return Slist_Loaded"];
```
---
#### FlowChart Utils/Validation.py
```mermaid
    graph TD
    A["Start: validate_function"] --> B{Loop};
    B --> C["Prompt user for input"];
    C --> D["Read input data"];

    %% CHECK 1: Empty String
    D --> E{"Input is empty?"};
    E -- "Yes" --> F["Print Error: Cannot be empty"];
    F --> C;

    E -- "No" --> G{"Try to Convert/Cast"};
    
    %% CHECK 2: Data Type (Conversion)
    G -- "Conversion Fails" --> H["Print Error: Invalid data type"];
    H --> C;

    G -- "Conversion Success" --> I{"Check Range/Condition?"};

    %% CHECK 3: Range / Business Rule
    I -- "Out of Range" --> J["Print Error: Value outside valid range"];
    J --> C;

    I -- "Valid" --> K["Return Valid Data"];
```
---
#### FlowChart Utils/auth.py
```mermaid
graph TD
    A["Start: authenticate_user()"] --> B["Set MAX_ATTEMPTS = 3"];
    B --> C{"Loop attempts from 1 to 3"};
    
    C --> D["Prompt for Username/Password"];
    D --> E{"Is Username in USERS?"};
    
    E -- "No" --> G["Print 'Invalid username/password'"];
    G --> C; 
    
    E -- "Yes" --> H{"Is Password Correct?"};
    
    H -- "No" --> G; 
    
    H -- "Yes" --> I["Print 'Login successful'"];
    I --> J["Return user ROLE"];
    J --> Z["End"];

    C -- "Loop Ends (3 Attempts)" --> K["Print 'Max attempts reached'"];
    K --> L["Return None"];
    L --> Z;
```
---
#### FlowChart Models/student.py
```mermaid
    graph TD
    A["Start: Set gpa(value)"] --> B{Is value a number?};

    %% Check 1: Data Type
    B -- "No" --> C["Raise TypeError"];
    C --> Z[End];

    B -- "Yes" --> D{"Is 0.0 <= value <= 4.0?"};

    %% Check 2: Range
    D -- "No" --> E["Raise ValueError"];
    E --> Z;

    D -- "Yes" --> F["Assign value to _gpa"];
    F --> Z;
```
---

## 4. IMPLEMENTATION OF BASIC FUNCTIONS

### 4.1 FUNCTIONS AND STEPS  

| Function | Sub-steps |
| :--- | :--- |
| **Add Student** | **Check Permission ('add')** → Input information (Name, Birth, ID, Major, GPA) → Validate input → Create object → Save to list |
| **Calculate GPA** | Iterate list → Get each GPA → Calculate average |
| **Search by ID/Name** |Select search by ID or Name → Input search query → Iterate list → Return results |
| **Edit Information** | **Check Permission ('edit')** → Find student → Display information → Input new data → Update list |
| **Delete Student** | **Check Permission ('delete')** → Find student → Confirm deletion → Remove from list |
| **Sort List** | Select criteria (Name, GPA, Birth Year) → Sort list → Display results |
| **Write Data to File** | **Check Permission ('io')** → Open file → Write student list → Close file |
| **Read Data from File** | Open file → Read data → Create student list → Return list |
| **Display List** | Iterate through each student → Print out information |
| **Menu Navigation** | Display menu → Input selection → Call correct function |

---

### 4.2 PATTERNS (RECURRING)

## 📋 Tóm hợp Mẫu Thiết kế và Kỹ thuật

| Pattern | Description |
| :--- | :--- |
| **Object-Oriented Design (OOD)** | Use the **`StudentData`** and **`StudentManager`** classes to organize program logic and data, following the Single Responsibility Principle. |
| **Encapsulation** | Use a **Property (`@property`)** for GPA in `StudentData` to protect the internal variable (`_gpa`) and enforce validation rules. |
| **Input Validation** | Check for valid input (e.g., GPA must be from 0.0 to 4.0; menu selections must be within range) and data types. |
| **Access Control** | Use the **`_check_permision`** method within `StudentManager` to restrict functions (Add, Edit, Delete, IO) based on the user's **`role`** (TEACHER, STUDENTS). |
| **Authentication** | Use the **`authenticate_user()`** function to verify user identity (username/password) and assign a corresponding **`role`** before starting the main program. |
| **Menu Structure** | Use a **loop and integer selection (`match/case`)** to navigate the main menu, providing a clear user interface. |
| **Search by Field** | Iterate through the list to find students by **ID** or by **name** (case-insensitive substring search). |
| **File I/O** | Read and write the student list to/from the **`students.txt`** file, ensuring data persistence. |
| **Exception Handling** | Use `try...except` blocks to catch errors when converting data types, handling invalid GPA values, or dealing with **File I/O** issues. |

---

## 5. OBJECT-ORIENTED DESIGN (OOP) 
```mermaid
classDiagram
    class StudentData {
        - name: str
        - birth: int
        - sid: str
        - major: str
        - _gpa: float
        + gpa: float
        
        + __init__(name, birth, SID, major, gpa)
        + get_gpa(): float
        + set_gpa(value: float)
        + __str__(): str
    }
```

```mermaid
classDiagram
    class StudentManager {
        + DEFAULT_DATA_FILE: str = "students.txt"
        + Permission: dict
        - user_lg: str
        
        + __init__(user_lg: str)
        - _check_permision(key_permission: str): bool
        - _search_for_action(Slist: list): list
        - _do_edit_logic(student: StudentData, Slist: list)
        
        + print_student_after(Slist: list)
        + find_edit_by_ID(Slist: list, search_ID: str): StudentData
        + find_edit_by_Name(Slist: list, search_Name: str): list
        
        + addnew(Slist: list)
        + searching(Slist: list)
        + editing(Slist: list)
        + deleting(Slist: list)
        + sorting(Slist: list)
        + calculate_gpa(Slist: list): float
        
        + Input_Load(Slist: list)
        + Output_Load(): list
    }
```
---
## 6. FILE I/O & TESTING 
##### 1/ Models/student.py
---
 Type | Name | Primary Role |
| :--- | :--- | :--- |
| **Class** | **StudentData** | Holds the data for a single(`Name`,`Birth`,`ID`,`Major`,`GPA`) |
| **Property** | `gpa` | The getter for the GPA attribute |
| **Setter** | `gpa` | Validates GPA range (0.0 to 4.0) before assigning the value |
| **Method** | `__init__` | Initializes the student attributes(`__name`, `__birth`, `__SID`, `__major`, `__gpa`) |
| **Method** | `__str__` | Formats data for display |
---
##### 2/ Services/student_manager.py

| Type | Name | Function Description |
| :--- | :--- | :--- |
| **Class** | **StudentManager** | The main management class, handling all student list operations and **user permission checks**. |
| **Variable** | `DEFAULT_DATA_FILE` | Constant specifying the data file name (`students.txt`). |
| **Variable** | `Permission` | **Class-level dictionary defining access rights** for each user role (e.g., 'TEACHER', 'STUDENTS'). |
| **Attribute** | `user_lg` | Instance attribute storing the **role of the currently logged-in user**. |
| **Method** | `__init__(user_lg)` | **Constructor** that initializes the manager instance with the **logged-in user's role**. |
| **Method** | `_check_permision(key_permission)` | **Core permission check.** Returns `True` if `user_lg` has the requested right (`key_permission`), otherwise prints "Access Denied" and returns `False`. |
| **Method** | `calculate_gpa(Slist)` | Calculates the average GPA of all students in `Slist`. |
| **Method** | `find_edit_by_ID(Slist, search_ID)` | Finds a student by ID (case-insensitive). |
| **Method** | `find_edit_by_Name(Slist, search_Name)` | Searches for students by name (substring search). |
| **Method** | `_search_for_action(Slist)` | Core logic to ask the user to search by ID or Name, used internally for Edit/Delete/Search. |
| **Method** | `_do_edit_logic(student, Slist)` | Core handler for editing and updating individual student fields. |
| **Method** | `addnew(Slist)` | **(Permission Checked)** Adds a new student object to `Slist`. |
| **Method** | `searching(Slist)` | Performs the search and displays results. |
| **Method** | `editing(Slist)` | **(Permission Checked)** Finds and edits a student's information. |
| **Method** | `deleting(Slist)` | **(Permission Checked)** Finds, confirms, and deletes a student from `Slist`. |
| **Method** | `sorting(Slist)` | Sorts `Slist` by Name, GPA, or Birth Year. |
| **Method** | `print_student_after(Slist)` | Displays the student list after sorting. |
| **Method** | `Input_Load(Slist)` | **(Permission Checked / Save Data)** Saves the current `Slist` to the `.txt` file. |
| **Method** | `Output_Load()` | **(Load Data)** Loads data from the `.txt` file and returns the `Slist`. |
---
##### 3/ Utils

###### /validation.py

| Type | Name | Function Description |
| :--- | :--- | :--- |
| **Function** | `select_menu_choice()` | Gets the integer choice from the user for the main menu (0 to 7). |
| **Function** | `get_number_choice()` | Gets the integer choice for search/edit options (1: ID, 2: Name). |

###### /auth.py


| Type | Name | Function Description |
| :--- | :--- | :--- |
| **Function** | `authenticate_user()` | Handles the **login process** with a limit of 3 attempts. It checks the input username and password against the internal `USERS` dictionary. Returns the validated **user role** (e.g., 'TEACHER', 'STUDENTS') on success, or `None` on failure. |
---
##### 4/ main.py (Execution)

| Type | Name | Function Description |
| :--- | :--- | :--- |
| **Function** | `main()` | The main function that **starts the program by calling `authenticate_user()`**, initializes the `StudentManager` with the user's role, loads data, and contains the core menu loop, calling appropriate service methods. |
| **Function** | `output_student_list(manager, Slist)` | Displays the entire **`Slist`**, and conditionally displays the **overall average GPA** by calling `manager.calculate_gpa()`. |
| **Variable** | `user_lg` | Variable storing the **validated role** of the logged-in user (e.g., 'TEACHER', 'STUDENTS') returned by `authenticate_user()`. |
| **Variable** | `manager` | The instance of the **`StudentManager`** class, initialized with `user_lg`. |
| **Variable** | `Slist` | The main list holding the **`StudentData`** objects, loaded from the file at startup. |
---

## 7. EXPERIMENTAL RESULTS

##### Menu program run

<img src="./assets/1.jpg">

##### Add new student

<img src="./assets/2.jpg">

##### GPA calculate

<img src="./assets/5.jpg">

##### Editing and Deleting student

<img src="./assets/4.jpg">

##### Sorting result

<img src="./assets/6.jpg">

##### I/O file

<img src="./assets/7.jpg">

---

## 8. APPENDIX

|#|Code File|
|:---|:---|
|1|`main.py`|
|2|`/models/student.py`|
|3|`/services/student_manager.py`|
|4|`/utils/validation.py`|
|5|`/utils/auth.py`|

|#|Test Case File|
|:---|:---|
|1|`students.txt`|
|2|`Input.csv`|

<div align="center">
    <img src="10.png" width=400 >
</div>