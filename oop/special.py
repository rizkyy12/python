class Employee:
    #classvariable
    raise_amount = 1.05
    
    def __init__(self, name, email, pay):
        self.name = name
        self.email = email + '@company.com'
        self.pay = pay
        
    def showInfo(self):
        return '{} {}'.format(self.name, self.email)
        return print(f'Nama: {self.name}, email: {self.email}, pay: {self.pay}')
    
    def apply_raise(self):
        self.pay = int(self.pay*Employee.raise_amount)
        
    def __repr__(self):
        return "Employee ('{}', '{}', '{}')".format(self.name, self.email, self.pay)

    def __str__(self):
        return "{} - {}".format(self.name, self.email)
    
    def __add__(self, other):
        return self.pay + other.pay 
    
    def __len__(self):
        return len(self.name)
    
emp1 = Employee('Rizky Andhika Akbar', 'rizkyandikaakbar', 40000)
emp2 = Employee('Sabrina Nurul Natasya', 'sabrinanrln', 30000)

#print(emp1)
#print(repr(emp1))
#print(str(emp1))
#print(emp1.__repr__())
#print(emp1.__str__())
print(len(emp1))