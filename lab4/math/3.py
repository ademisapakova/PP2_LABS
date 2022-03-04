from math import tan, pi
sides = int(input('Input umber of sides: '))
length = int(input('Input the length of a side: '))

p_area = sides*(length**2) / (4 * tan(pi / sides))


print(f'The area of the polygon is: {round(p_area)}')




