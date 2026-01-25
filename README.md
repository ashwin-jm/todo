# 📝 To-Do Application from the Command Line (Python)

This project is a **step-by-step guide** to building a simple **To-Do application in Python** using the command line.

The goal is not just to build the app, but to **understand the core Python concepts** that appear while building it.

By the end of this guide, you will be able to:

- Build a working CLI To-Do app
- Understand why each change is made
- Learn how data persistence works

## 📌 What Will the Application Do?

A basic To-Do application must support these actions:

- Add tasks
- View tasks
- Delete tasks
- Complete tasks
- Persist data even after the program exits

We’ll build this incrementally, fixing problems as they appear.

## 🧠 Step 1: Initial Idea (Naive Implementation)

We start by printing a menu and asking the user what they want to do.

```python
print("To Do List Application")

print("1. Add a task")
print("2. Delete a task")  
print("3. View tasks")
print("4. Complete a task")
print("5. Exit")

user_choice = input("Enter your choice (1-5): ")

```

### 🔍 What We Learn Here

**print()** displays output

**input()** takes input from the user

User input is always a string

## 🧠 Step 2: Storing Tasks Using a List

We need a place to store tasks while the program runs.

```python
user_tasks = []
```

### 🔍 What Is a List?

A list is a built-in data structure that is used to store multiple values. The values could be of the same or different type. 

```python
Example:

["Buy milk", "Do homework"]
[3,4,5]
["Buy milk", 4, "Do homework", 5]
```

We use a list because:

- Order matters
- Tasks can be added or removed
- It’s simple and flexible

## ❌ Observation 1: Program Exits After One Action

After performing one action, the program exits.

### ❌ Why This Happens

The code executes top to bottom only once.

### ✅ Modification

We wrap the logic inside a while True: loop.

```python
while True:
    # menu + logic
```

### 🔍 What We Learn

- while True creates an infinite loop
- Loops allow programs to keep running

## ❌ Observation 2: Data Is Still Lost

Even with the loop, tasks disappear.

### ❌ Root Cause: Variable Scope

Initially, this was written like this:

```python
while True:
    user_tasks = []
```

Each loop iteration **recreates the list**, deleting old data.

### ✅ Modification

Declare the list outside the loop.

```python
user_tasks = []

while True:
    ...
```

### 🔍 What We Learn

**Scope** defines:

- Where a variable exists
- How long it lives

A variable inside a loop is recreated every iteration.

## ❌ Observation 3: Invalid Choices Aren’t Handled

If the user enters 6, nothing meaningful happens.

### ✅ Modification

Add a final else block.

```python
else:
    print("Invalid choice. Please try again.")
```

### 🔍 What We Learn

- Defensive programming
- Always handle unexpected user input

## ❌ Observation 4: Case Sensitivity Bug

In Python:

```python
"Do a project" != "do a project"
```

So deleting "Do a project" fails if the stored task is "do a project".

### ✅ Modification: Normalize Strings
```python
task_to_delete = input().lower()

if task.lower() == task_to_delete:
```

### 🔍 What We Learn

- Strings are case-sensitive
- lower() normalizes text
- Always normalize both sides of a comparison

## ❌ Observation 5: “Not Found” Prints Multiple Times

If the task is at the end of the list, "not found" prints for every earlier task.

### ❌ Why This Happens

The else was inside the for loop.

### ✅ Modification: Use a found Flag

```python
found = False

for task in user_tasks:
    if condition:
        found = True
        break

if not found:
    print("Task not found")
```

### 🔍 What We Learn

- Loops don’t mean failure until they finish
- Control flow matters

## 🧠 Step 3: Function Extraction

At this stage, all logic was inside main().

We extracted functionality into functions:

- show_menu()
- add_task()
- view_tasks()
- remove_task()
- complete_task()

### 🔍 What Is a Function?

A function:

- Groups related logic
- Has a name
- Can be reused

Example:

```python
def add_task(task_list):
    ...
```

### 🔍 What We Learn

- Code reusability
- Clean structure
- Separation of concerns

## 🧠 Step 4: Memory vs Storage (File Persistence)
### ❌ Problem

Tasks disappear when the program exits.

### 🔍 Why?

Data stored in variables lives only in **memory (RAM)**.

### ✅ Solution: File Storage (JSON)

We store tasks in a file called tasks.json.

### 🔍 Why JSON?

- Human readable
- Easy to use in Python
- Common in real systems

### 📂 File Storage Functions
**load_tasks()**
```python
def load_tasks():
    if os.path.exists(TASKS_FILE):
        with open(TASKS_FILE, 'r') as file:
            return json.load(file)
    return []
```

**save_tasks()**
```python
def save_tasks(task_list):
    with open(TASKS_FILE, 'w') as file:
        json.dump(task_list, file, indent=4)
```

### 🔍 What We Learn

- Serialization & deserialization
- Disk vs memory
- Persistent state
- Fault tolerance

## 🧠 Storage Choices (Introduction)

Different ways to store data:

- JSON (used here)
- CSV
- Parquet
- SQLite (next logical step)

## ✅ Final Outcome

By following this guide, you have learned:

### 🧠 Python Concepts

- Variables
- Lists
- Input/output
- Loops
- Functions
- Scope
-String normalization

### 🧠 Software Engineering Concepts

- Iterative development
- Bug discovery & fixes
- Persistence
- Separation of concerns
- Defensive programming

### 🚀 What You Can Build Next

- Add task IDs
- Store {id, task, completed}
- Replace JSON with SQLite
- Convert this into a FastAPI backend
- Build a React frontend

## ⭐ Final Note

This project is intentionally simple — because real learning happens when simple things break.

“Small programs teach big ideas.”

Happy building!