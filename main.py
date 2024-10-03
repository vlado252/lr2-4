import math
x = float(input("Введи значение x:"))
y = float(input("Введи значение y:"))
z = float(input("Введи значение z:"))
w =pow(math.fabs(math.cos(x)-math.cos(y)), 1+2*pow(math.sin(y),2))*(1+z+((pow(z,2))/2)+((pow(z,3))/4)+((pow(z,4))/4))
print("Результат = ",w)
