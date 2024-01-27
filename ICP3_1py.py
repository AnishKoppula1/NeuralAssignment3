#Employee Class
class Employee:
    num_of_employees = 0  #data member that counts the number of Employees

    # constructor that initializes name, family, salary, department
    def __init__(self, name, family, salary, department):
        self.name = name
        self.family = family
        self.salary = salary
        self.department = department
        Employee.num_of_employees += 1   #Incrementing the employee count on instance creation
        
    #a function to average salary that accepts Employee array and returns average
    @staticmethod
    def employees_average_salary(employees):
        employee_salaries = [emp.salary for emp in employees] #creating an array of Salaries using list comprehension
        sum_of_salaries = sum(employee_salaries)
        employee_count = len(employees)
        return sum_of_salaries / employee_count


#FulltimeEmployee Class
class FulltimeEmployee(Employee):
    # constructor that initializes name, family, salary, department
    def __init__(self, name, family, salary, department):
        super().__init__(name, family, salary, department) #calling EMployee class Constructor


# Creating instances of Employee and FulltimeEmployee classes
employee_1 = Employee("Anish", "Koppula", 30000, "Associate Software Developer")
employee_2 = Employee("Rohit", "Sharma", 100000, "Manager")
employee_3 = FulltimeEmployee("Virat", "Kohli", 50000, "Senior Developer")
employee_4 = FulltimeEmployee("Arunab", "Koppula", 7000000, "CEO")

#creating a list using the Employee and FulltimeEmployee class instances
employees = [employee_1, employee_2, employee_3, employee_4]

#calling datamember using Employee Class
print("No of Employess : " + str(FulltimeEmployee.num_of_employees))

# Calling member functions using FulltimeEmployee class
print("Average salary of all employees : " + str(Employee.employees_average_salary(employees)))


