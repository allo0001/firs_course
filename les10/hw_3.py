class Cell():
    
    def __init__(self, section):
        self.section = section
        
    
    def __add__(self, other):
        return Cell(self.section + other.section)
    
    def __sub__(self, other):
        return Cell(s) if (s:=self.section-other.section) > 0 \
                            else 'Не возможно произвести операцию!'
    
    def __mul__(self, other):
        return Cell(self.section * other.section)
    
    def __floordiv__(self, other):
        return Cell(self.section // other.section)
    
    def __repr__(self):
        return f'Cell: section - {self.section}'
    
    def make_order(self, part):
        return ('*'*part + '\n') * (self.section//part) + '*'*(self.section%part) + '\n' 
    
    
c1 = Cell(15)
c2 = Cell(10)
c3 = Cell(3)

print(c1 + c2 + c3)    
print(c1 - c2)
print(c2 - c1)
print(c1 * c2)  
print(c1 // c2, end='\n\n')
print(c1.make_order(6)) 
print(c2.make_order(4))
print(c3.make_order(5))

