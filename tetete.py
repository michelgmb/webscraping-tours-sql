class Employee:
    def __int__(self, first, last, pay):
        self.first = first
        self.last = last
        self.pay = pay
        self.email = first + '.' + last + '@company.com'


emp_1 = Employee("michel", "gandeu", 140000)
emp_2 = ("sarah", "Ndolo", 120000)


print(emp_1.email)
