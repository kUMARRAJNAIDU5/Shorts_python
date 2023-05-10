# defining a class Employee
class Employee:
    # constructor
    company_name = "CISCO"
    __previous_company_name = "TELSTRA"
    def __init__(self, name, sal):
        self._name = name;   # protected attribute
        self._sal = sal;     # protected attribute


# defining a child class
class HR(Employee):

    # member function task
    def task(self):
        print("We manage Employees")


emp = Employee("Captain", 10000);
print(emp._sal)
print(emp._name)
print(emp.company_name)
print(emp._Employee__previous_company_name)


hrEmp = HR("Captain", 10000);
hrEmp._sal;
hrEmp.task();