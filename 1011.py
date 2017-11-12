a,b,c=input().split(" ")
A=float(a)
B=float(b)
C=float(c)

triangle_area=0.5*A*C
circle_area=3.14159*C*C
trapezium_area=0.5*(A+B)*C
square_area=B*B
rectangle_area=A*B

print('TRIANGULO: %.3f'%triangle_area)
print('CIRCULO: %.3f'%circle_area)
print('TRAPEZIO: %.3f'%trapezium_area)
print('QUADRADO: %.3f'%square_area)
print('RETANGULO: %.3f'%rectangle_area)
