class Employee:
    
    def __init__(self, first, last):
        self.first = first
        self.last = last
    
    @property
    def email(self):
        return '{}{}@company.com'.format(self.first, self.last)
    
    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)
    
    @fullname.setter
    def fullname(self, name):
        first, last = name.split(' ')
        self.first = first
        self.last = last
    
    @fullname.deleter 
    def fullname(self):
        print('Delete Name!')
        self.first = None 
        self.last = None
    
emp1 = Employee('RizkyAndhika', 'Akbar')
emp1.fullname = 'Amnjay solo'

print('Nama lengkap: ', emp1.fullname)
print('Nama depan: ', emp1.first)
print('Email: ', emp1.email)

del emp1.fullname
    
