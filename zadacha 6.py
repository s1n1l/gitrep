"""6. Поміняти місцями вміст змінних A і B і вивести нові значення A і B."""


x = float(input())
y = float(input())

def ch(a,b):
    c = a;
    a = b;
    b = c;
    return(a,b)

print(ch(x, y))