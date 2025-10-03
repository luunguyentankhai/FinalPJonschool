<div align="center">
    <img src=7.png width=400 alt="hi chat" >
</div>

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
    A["Start: main()"] --> B("Initialize StudentManager and Slist");
    B --> C("Load Data: manager.Output_Load()");
    C --> D{"Main Loop: choice != 0"};

    %% Main function branches
    D -- "Yes" --> E("Display Menu and Get choice");
    E --> F{"Check choice"};
    
    F -- "1: Add" --> G("manager.addnew(Slist)");
    F -- "2: Edit" --> H("manager.editing(Slist)");
    F -- "3: Delete" --> I("manager.deleting(Slist)");
    F -- "4: Search" --> J("manager.searching(Slist)");
    F -- "5: Sort" --> K("manager.sorting(Slist)");
    F -- "6: GPA" --> L("manager.calculate_gpa(Slist)");
    F -- "7: Display" --> M("output_student_list");
    
    %% Return to loop
    G --> D;
    H --> D;
    I --> D;
    J --> D;
    K --> D;
    L --> D;
    M --> D;

    %% Program Exit
    F -- "0: Exit" --> N("Save Data: manager.Input_Load(Slist)");
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
    A["Start: addnew(Slist)"] --> B[Loop: Get Name];
    B --> C[Loop: Get Birth Year];
    C --> D[Loop: Get SID];
    D --> E{Is SID unique?};
    
    E -- "No" --> F[Print Error: SID exists];
    F --> D;

    E -- "Yes" --> G[Loop: Get Major];
    G --> H[Loop: Get GPA];

    H --> I[Create StudentData Object];
    I --> J[Append to Slist];
    J --> Z[End];
```
---
###### Function Editing
```mermaid
    graph TD
    A["Start: editing(Slist)"] --> B{"candidates = _search_for_action(Slist)"};
    
    B -- "Search Fails" --> C["Print "Edit cancelled/Student not found""];
    C --> Z[End];
    
    B -- "Search Success" --> D[Get student object];
    
    D --> E["Call _do_edit_logic(student)"];
    E --> F["Print "Edit process finished.""];
    F --> Z;
```
---
###### Function Deleting
```mermaid
    graph TD
    A["Start: deleting(Slist)"] --> B{"student = _search_for_action(Slist)"};
    
    B -- "Search Fails" --> C["Print "Delete cancelled/Student not found""];
    C --> Z[End];
    
    B -- "Search Success" --> D["Get student object"];
    D --> E["Print data & Ask for confirmation (Y/N)"];
    
    E --> F{"User Confirmed (Y)?"};
    
    F -- "No" --> C; 
    
    F -- "Yes" --> G["Remove student from Slist"];
    G --> H["Print "Delete successful!""];
    H --> Z;
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
    A["Start: Input_Load(Slist)"] --> B{Is Slist empty?};

    B -- "Yes" --> C["Print 'Slist is empty, no data to save.'"];
    C --> Z["End"];

    B -- "No" --> D["Open default file (students.txt) for writing"];
    D --> E["Write Header Line to file"];
    
    E --> F{Loop through each student in Slist};
    F --> G["Format student data into CSV string"];
    G --> H["Write data string to file"];
    H --> F;

    F --> I["Close file"];
    I --> J["Print 'Data saved successfully!'"];
    J --> Z;
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
| **Add Student** | Input information (Name, Birth, ID, Major, GPA) → Validate input → Create object → Save to list |
| **Calculate GPA** | Iterate list → Get each GPA → Calculate average |
| **Search by ID/Name** | Select search by ID or Name → Input search query → Iterate list → Return results |
| **Edit Information** | Find student → Display information → Input new data → Update list |
| **Delete Student** | Find student → Confirm deletion → Remove from list |
| **Sort List** | Select criteria (Name, GPA, Birth Year) → Sort list → Display results |
| **Write Data to File** | Open file → Write student list → Close file |
| **Read Data from File** | Open file → Read data → Create student list → Return list |
| **Display List** | Iterate through each student → Print out information |
| **Menu Navigation** | Display menu → Input selection → Call correct function |

---

### 4.2 PATTERNS (RECURRING)

| Pattern | Description |
| :--- | :--- |
| **Input Validation** | Check for valid input (e.g., GPA must be from 0.0 to 4.0) |
| **Menu Structure** | Use a loop and integer selection to navigate the main menu |
| **Search by Field** | Iterate through the list to find by ID or by name |
| **File I/O** | Read and write the student list to/from the `students.txt` file |
| **Exception Handling** | Catch errors when unable to read the file or data format is invalid |
| **Object-Oriented Design** | Use the `StudentData` and `StudentManager` classes to organize program logic |
| **User Confirmation** | Require confirmation before deleting or editing information |

---

## 5. OBJECT-ORIENTED DESIGN (OOP) 
```
+---------------------------+
|       StudentData         |
+---------------------------+
| - name: str               |  <- Attribute
| - birth: int              |
| - sid: str                |
| - major: str              |
| - _gpa: float             |  <- Internal Variable (Protected/Private convention)
|                           |
| + gpa: float              |  <- Property (Represents Getter/Setter)
+---------------------------+
| + __init__(name, birth,   |  <- Constructor Method
|   SID, major, gpa)        |
| + get_gpa(): float        |  <- Getter (@property gpa)
| + set_gpa(value: float)   |  <- Setter (@gpa.setter)
| + __str__(): str          |  <- Display Method
+---------------------------+
```

```
+-------------------------------------------------------------+
|                     StudentManager                          |
+-------------------------------------------------------------+
| + DATA_FILE: str = "students.txt"                           | <- Class Attribute
+-------------------------------------------------------------+
| + __init__(name:str, birth:int, SID:str, major:str, gpa:float)| <- Constructor (Functionally 'pass')
| + print_student_after(Slist: list)                          |
|                                                             |
| - _search_for_action(Slist: list): list                     | <- Core Search Logic
| - _do_edit_logic(student: StudentData, Slist: list)         | <- Core Edit Logic
|                                                             |
| + find_edit_by_ID(Slist: list, search_ID: str): StudentData |
| + find_edit_by_Name(Slist: list, search_Name: str): list    |
|                                                             |
| + addnew(Slist: list)                                       |
| + searching(Slist: list)                                    |
| + editing(Slist: list)                                      |
| + deleting(Slist: list)                                     |
| + sorting(Slist: list)                                      |
| + calculate_gpa(Slist: list): float                         |
|                                                             |
| + Input_Load(Slist: list)                                   | <- Write/Save Data
| + Output_Load(): list                                       | <- Read/Load Data
+-------------------------------------------------------------+
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
##### 3/ Utils/validation.py

| Type | Name | Function Description |
| :--- | :--- | :--- |
| **Function** | `select_menu_choice()` | Gets the integer choice from the user for the main menu (0 to 7). |
| **Function** | `get_number_choice()` | Gets the integer choice for search/edit options (1: ID, 2: Name). |
---
##### 4/ main.py (Execution)

| Type | Name | Function Description |
| :--- | :--- | :--- |
| **Function** | `output_student_list(manager, Slist)` | Displays the entire **Slist** , including the **overall average GPA**. |
| **Function** | `main()` | The main function that starts the program, contains the core menu loop and calls service methods. |
| **Variable** | `Slist` | The main list holding the **StudentData** objects. |
| **Variable** | `manager` | The instance of the **StudentManager** class. |
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

|#|Test Case File|
|:---|:---|
|1|`students.txt`|
|2|`Input.csv`|

<div align="center">
    <img src="10.png" width=400 >
</div>