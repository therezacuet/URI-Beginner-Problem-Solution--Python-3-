a,b,c=input().split(" ")
A=int(a)
B=int(b)
C=int(c)
ab=(A+B+abs(A-B))/2
abc=(ab+C+abs(ab-C))/2

print('%i eh o maior'%abc)
