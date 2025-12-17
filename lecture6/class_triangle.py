import math

class Triangle:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    
    def lenght(self):
        return math.sqrt(self.x**2 + self.y**2)
    
    def area(self):
        return self.x*self.y
    
    def perimeter(self):
        return (self.x + self.y + self.lenght())
        

triangle1 = Triangle(6, 8)
print("Length:", triangle1.lenght())
print("Area:", triangle1.area())
print("Perimeter:", triangle1.perimeter())