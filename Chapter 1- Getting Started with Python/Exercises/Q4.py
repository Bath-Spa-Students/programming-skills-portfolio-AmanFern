a = float(input('Side 1: '))  
b = float(input('Side 2: '))  
c = float(input('Side 3: '))  
#formula for semi perimeter (needed for area)
s = (a+b+c)/2

# formula for area of triangle  
area = (s*(s-a)*(s-b)*(s-c)) ** 0.5  
print('The area of the triangle is %0.2f' %area)