class Employee:
    #classvariable
    raise_amount = 1.05
    num_employee = 0
    
    def __init__(self, name, email, pay):
        self.name = name
        self.email = email + '@company.com'
        self.pay = pay
        
        Employee.num_employee += 1
        
    def showInfo(self):
        return '{} {}'.format(self.name, self.email)
        #return print(f'Nama: {self.name}, email: {self.email}, pay: {self.pay}')
    
    def apply_raise(self):
        self.pay = int(self.pay*Employee.raise_amount )
        
    @classmethod
    def set_raise_amt(cls, amount):
        cls.raise_amount = amount 
        
    @classmethod
    def from_str(cls, emp_str):
        name, email, pay = em1_str.split('-')
        return cls (name, email, pay)
        
    @staticmethod
    def hari_kerja(day):
        if day.weekday() == 5 or day.weekday() == 6:
            return False 
        return True 
                
em1 = Employee('Sabrina Nurul N','sabrinanuruln', 50000)
em2 = Employee('Rizky Andhika A','rizkyandikaakbar', 100000)

import datetime
my_date = datetime.date(2020, 8, 28)
print(Employee.hari_kerja(my_date))
#classmethode
#em1_str = 'Andhika-rizkyandikaakbar-69000'
#new_em1 = Employee.from_str(em1_str)
#print(new_em1.name)
