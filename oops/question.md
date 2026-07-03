# Assignment: Employee Management System 

Every employee has:

-   Employee ID
-   Name
-   Department
-   Designation
-   Salary
-   Years of Experience
-   City

Instead of using a database, the company wants to store the employee
data inside a file.

------------------------------------------------------------------------

# Step 1: Create an Employee Class

Create a class named `Employee`.

It should contain the following attributes:

-   employee_id
-   name
-   department
-   designation
-   salary
-   experience
-   city

Also create a method that converts an employee object into a dictionary.

Example:

``` python
{
    "employee_id": 101,
    "name": "Rahul",
    "department": "Engineering",
    "designation": "Software Engineer",
    "salary": 85000,
    "experience": 3,
    "city": "Pune"
}
```

------------------------------------------------------------------------

# Step 2: Create EmployeeManager Class

Create another class called `EmployeeManager`.

This class should internally maintain

-   a list of Employee objects
-   a dictionary for fast lookup

Example

``` python
employees = []

employee_map = {
    101: Employee(...),
    102: Employee(...)
}
```

------------------------------------------------------------------------

# Step 3: Implement Operations

Implement methods for the following:

### Add Employee

Add a new employee.

Also update the dictionary.

------------------------------------------------------------------------

### Remove Employee

Remove employee using Employee ID.

------------------------------------------------------------------------

### Update Salary

Increase or decrease salary using Employee ID.

------------------------------------------------------------------------

### Search Employee

Search using Employee ID.

Return the Employee object.

------------------------------------------------------------------------

### Search by Department

Return all employees belonging to a department.

Example:

Engineering

returns

-   Rahul
-   Mohit
-   Aman

------------------------------------------------------------------------

### Search by City

Return all employees from a city.

------------------------------------------------------------------------

### Search Employees with Salary Greater Than

Example:

Salary \> 70000

Return matching employees.

------------------------------------------------------------------------

### Search Employees with Experience Greater Than

Example:

Experience \>= 5 years

Return matching employees.

------------------------------------------------------------------------

### Group Employees Department Wise

Return a dictionary like

``` python
{
    "Engineering": [Employee1, Employee2],
    "HR": [Employee3],
    "Finance": [Employee4]
}
```

------------------------------------------------------------------------

### Find Highest Paid Employee

Return the employee with maximum salary.

------------------------------------------------------------------------

### Find Average Salary

Return average salary of all employees.

------------------------------------------------------------------------

# Step 4: Store Data in File

Store all employees in a file named

    employees.txt

One employee per line.

Hint:

Store dictionary representation.

------------------------------------------------------------------------

# Step 5: Load Data from File

Read the file.

Create Employee objects again.

Store them in both

-   list
-   dictionary

------------------------------------------------------------------------

# Step 6: Generate Reports

Generate the following reports.

## Report 1

Employees sorted by salary (Highest to Lowest)

------------------------------------------------------------------------

## Report 2

Employees sorted by experience

------------------------------------------------------------------------

## Report 3

Department-wise employee count

Example

    Engineering : 8
    HR : 3
    Finance : 5

------------------------------------------------------------------------

## Report 4

Employees earning more than average salary.

------------------------------------------------------------------------

## Report 5

Top 3 highest paid employees.

------------------------------------------------------------------------



# Sample Menu

``` text
1. Add Employee
2. Remove Employee
3. Update Salary
4. Search by ID
5. Search by Department
6. Search by City
7. Salary Report
8. Experience Report
9. Save to File
10. Load from File
11. Exit
```

------------------------------------------------------------------------
