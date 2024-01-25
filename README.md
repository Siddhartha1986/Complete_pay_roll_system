
# Payroll System

## Overview
The Payroll System is a comprehensive solution for managing employee payroll in a simple and efficient manner. The system supports different types of employees, including those paid monthly, hourly, and on a commission basis. It offers functionalities to add new employees, calculate their payroll, and handle employee data through a file system.

## Features
- **Employee Management:** Add new employees with different salary structures.
- **Payroll Calculation:** Compute payroll for all types of employees.
- **File Handling:** Save and read employee data from a CSV file.
- **User-friendly Interface:** Easy-to-use console-based interface.

## Setup
No specific installation is required. The system is written in Python and can be run in any environment where Python is installed.

1. Ensure Python (version 3.x) is installed on your system.
2. Download the payroll system script (`payroll_system.py`).
3. Run the script in a Python environment.

## Usage
The system is interactive and console-based. Follow these steps to use the system:

1. **Start the System**: Run the script. You will be greeted with a menu of options.

2. **Add Employee**: 
    - Choose option `1` to add an employee.
    - Enter the employee's salary type (monthly, hourly, commission).
    - Follow the prompts to enter employee details (name, salary, hours worked, etc.).
    - The employee will be assigned an ID and added to the system.

3. **Write Employees to File**: 
    - Choose option `2` to save current employee data to `employee.csv`.
    - Employee data is written in a structured format to the CSV file.

4. **Read Employees from File**: 
    - Choose option `3` to load employee data from `employee.csv`.
    - This option reads employee data and displays it.

5. **Print Payroll**:
    - Choose option `4` to calculate and display the payroll for all employees.

6. **Exit the System**:
    - Choose option `0` to exit the system.

## File Structure
- `employee.csv`: This file is used to store and retrieve employee data.

## Dependencies
- Python 3.x

## Limitations
- The system is console-based and does not currently support a graphical user interface.
- Error handling is basic and might not cover all edge cases.

## Contributing
Contributions to improve the Payroll System are welcome. Please feel free to fork the repository and submit pull requests.

## License
MIT

