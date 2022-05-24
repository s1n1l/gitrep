"""7. За довжинами двох сторін деякого трикутника і кутом між ними знайти довжину третьої сторони і
площу цього трикутника."""
import math

a = float(input())
b = float(input())
u = float(input())

def sttr(a,b,u) -> float:
 q=round (math.cos(math.radians(u)),1)
 z = ((a * a) + (b * b )) - (2 * a * b * q)
 x = math.sqrt(z)
 return x

def plosh (a, b, u) -> float:
    q = round(math.sin(math.radians(u)), 1)
    s = (a * b * 0.5 * q)
    return s
print("Третья сторона", sttr(a,b,u))
print("Площадь треугольника" , plosh(a,b,u))





