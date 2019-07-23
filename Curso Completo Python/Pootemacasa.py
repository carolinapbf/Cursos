class Cylinder(object):
    pi=3.14
    def __init__(self,height=1,radius=1):
        self.height=height
        self.radius=radius
        pass
        
    def volume(self):
        return self.height*(3.14)*self.radius**2

    def area(self):
        return 2*(3.14)*self.radius*(self.height+self.radius)
        
c=Cylinder(2,3)
print(c.volume())
print(c.area())