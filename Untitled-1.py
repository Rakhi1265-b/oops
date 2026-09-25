class Employee:

    def __init__(self,name,age,salary):
        self.name = name
        self._age=age
        self.__salary = salary

    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self,new_salary):
        self.__salary = new_salary

e = Employee("jhon",20,10000)
print("before updating salary",e.salary)
e.salary = 20000
print("after updating salary",e.salary)