import csv

# Function to split a sentence into a list of words based on a separator
def my_split(sentence, sep):
	lst = []
	tmp = ""
	for c in sentence:
		if c != sep:
			tmp += c
		else:
			lst.append(tmp)
	if tmp:
		list.append(tmp)      # Appends the last segment if it's not empty
	
	return(lst)

# Function to join elements of a list into a string with a separator
def my_join(lst,sep):
	mystr = ""
	for elm in lst[0:len(lst)]:
		mystr += str(elm)+str(sep)
		
	return(mystr)


# Class representing the payroll system
class PayrollSystem:
	def calculate_payroll(self, employees):
		
		for employee in employees:
			print("Employee Payroll")
			print("================")
			print(f"Payroll for: {employee.id} - {employee.name}")
			print(f"- Check amount: {employee.calculate_salary()}")
			print("")

# Base class for an employee
class Employee:
	def __init__(self, id, name):
		self.id = id
		self.name = name
	
	# Method to ask for employee's name
	def ask_name(self):
		try:
			self.name = str(input("Please enter employee name:"))
		except:
			self.name = ""

# Subclass for employees with a fixed monthly salary
class SalaryEmployee(Employee):
	def __init__(self, id, name, monthly_salary):
		super().__init__(id,name)
		self.salary = "M"
		self.monthly_salary = int(monthly_salary)

	# String representation of a salary employee
	def __str__(self):
		return f"{self.id},{self.name},{self.salary},{self.monthly_salary}"

	# Method to ask for employee's monthly salary
	def ask_salary(self):
		try:
			self.monthly_salary = int(input("Please enter monthly salary:"))
		except:
			self.monthly_salary = 0

	# Calculate salary for a monthly salaried employee
	def calculate_salary(self):
		return self.monthly_salary

# Subclass for employees who are paid hourly
class HourlyEmployee(Employee):
	finalwage = 0
	def __init__(self,id,name,hour_rate,hour_worked):
		super().__init__(id,name)
		self.salary = "H"
		self.hour_rate = hour_rate
		self.hour_worked = hour_worked

	# String representation of an hourly employee
	def __str__(self):
		return f"{self.id},{self.name},{self.salary},{self.hour_worked},{self.hour_rate}"
	
	# Method to ask for hours worked and hourly rate
	def ask_salary(self):
		try:
			self.hour_worked = int(input("Please enter hours worked:"))
			self.hour_rate = int(input("Please enter hour rate:"))
		except:
			self.hour_worked = 0
			self.hour_rate = 0
	
	# Calculate salary for an hourly employee
	def calculate_salary(self):
		self.finalwage = self.hour_worked*self.hour_rate
		return self.finalwage
		

# Subclass for employees who receive a commission in addition to their salary		
class CommissionEmployee(SalaryEmployee):
	wage = 0  # Variable to store final wage
	def __init__(self,id,name,monthly_salary,comission):
		super().__init__(id,name,monthly_salary)
		self.salary ="C"
		self.comission = comission

	# String representation of a commission employee
	def __str__(self):
		return f"{self.id},{self.name},{self.salary},{self.monthly_salary},{self.comission}"

	# Method to ask for monthly salary and commission
	def ask_salary(self):
		try:
			self.monthly_salary = int(input("Please enter monthly salary:"))
			self.comission = int(input("Please enter commission:"))
		except:
			self.monthly_salary = 0
			self.commission = 0

	# Calculate salary for a commission employee
	def calculate_salary(self):
		self.wage = self.monthly_salary+self.comission
		return self.wage


# Main script to interact with the payroll system

employees = []     # List to store employees
id = 1             # Initial employee ID

# Loop for user interaction
while True:
    print("(1) Add employee to employees\n(2) Write employees to file\n(3) Read employees from file\n(4) Print payroll\n(0) Quit\n")
    selection = int(input("Please select one: "))
    
    if selection == 1:
        
        
        while True:
            salarytype = int(input("Please enter salary type:\n(1) monthly\n(2) hourly\n(3) commission\n(0) Quit\n"))
            if salarytype == 1:
                employee = SalaryEmployee(id,"",0)
                SalaryEmployee.ask_name(employee)
                SalaryEmployee.ask_salary(employee)
                employees.append(employee)
                id += 1
            elif salarytype == 2:
                employee = HourlyEmployee(id,"",0,0)
                HourlyEmployee.ask_name(employee)
                HourlyEmployee.ask_salary(employee)
                employees.append(employee)
                id += 1
    
            elif salarytype == 3:
                employee = CommissionEmployee(id,"",0,0)
                CommissionEmployee.ask_name(employee)
                CommissionEmployee.ask_salary(employee)
                employees.append(employee)
                id += 1
            elif salarytype == 0:
                break
            else:
                print("Incorrect selection.")
    
    elif selection == 2:
        list2 = []
        filehandle2 = open("employee.csv","w")
        for i in employees:
            list2.append(i)
        string2 = my_join(list2,"\n")
        filehandle2.write(string2)
        filehandle2.close()
        print(len(employees) ," employee(s) added to employee.csv")
    
    elif selection == 3:
        index3 = []
        filehandle3 = open("employee.csv","r")
        content = filehandle3.readlines()
        for line in content:
            sline = line.strip("\n")
            index3.append(sline)
        filehandle3.close()
        print(len(index3) ," employee(s) read from employee.csv")

        for i in index3:
            print(i)
                            
    
    elif selection == 4:
        payroll_system = PayrollSystem()
        payroll_system.calculate_payroll(employees)
    
    elif selection == 0:
        print("Service shutting down, thank you.")
        break
    else:
        print("Incorrect selection.")
    

	
		  
