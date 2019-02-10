
class Emp:
    
    num_of_emps=0
    raise_amt=1.05
    def __init__(self, first, last, pay):
        self.first=first
        self.last=last
        self.pay=pay
        self.email=first+'.'+last+'@company.com'
        Emp.num_of_emps+=1
    
    def fullname(self):
        return '{} {}'.format(emp1.first, self.last)
        
    def apply_raise(self):
        self.pay=int(self.pay*self.raise_amt)
        
emp1=Emp("Corey", "Scaufer", 40000)
emp2=Emp("Scander", "Cafer", 50000)
print(emp1.email)
print(emp1.fullname())
print(emp1.pay)
emp1.apply_raise()
print(emp1.pay)
print(emp1.raise_amt)
print(Emp.raise_amt)

print(emp1.__dict__)
print(Emp.__dict__)
print(Emp.num_of_emps)

'''
Output:

Corey.Scaufer@company.com
Corey Scaufer
40000
42000
1.05
1.05
{'last': 'Scaufer', 'first': 'Corey', 'email': 'Corey.Scaufer@company.com', 'pay': 42000}
{'num_of_emps': 2, '__dict__': <attribute '__dict__' of 'Emp' objects>, '__module__': '__main__', '__doc__': None, '__init__': <function Emp.__init__ at 0x7f692be80158>, 'raise_amt': 1.05, '__weakref__': <attribute '__weakref__' of 'Emp' objects>, 'fullname': <function Emp.fullname at 0x7f692be801e0>, 'apply_raise': <function Emp.apply_raise at 0x7f692be80268>}
2


'''
