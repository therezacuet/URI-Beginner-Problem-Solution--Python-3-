import math
x1,y1=input().split(" ")
x2,y2=input().split(" ")
r=(float(x2)-float(x1))**2+(float(y2)-float(y1))**2
distance= math.sqrt(r)

print('%.4f'%distance)
