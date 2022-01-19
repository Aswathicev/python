
class Rectangle:
   def _init_(self,length,width):
       self.__length=length
       self.__width=width
   def area(self):
       return self._length*self._width
   def _lt_(self,other):
       return self.area()>other.area()
   l1=int(input("eneter the length of first rectangle:"))
   w1=int(input("eneter the width of first rectangle:"))
   rectangle1=(l1,w1)
   l2=int(input("eneter the length of second rectangle:"))
   w2=int(input("eneter the width of second rectangle:"))
   rectangle2=(l2,w2)
   if rectangle1 < rectangle2:
       print("area of rectangle 1 is smaller")
   else:
       print("area of rectangle 2 is smaler")