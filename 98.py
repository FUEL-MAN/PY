#9
n1 = input("Введите трехзначное число: ")
n1 = int(n)

d6 = n1 % 10
d5 = n1 % 100 // 10
d4 = n1 // 100

print("Сумма цифр числа:", d6 + d5 + d4)
print("Сред арифмет:", (d6 + d5 + d4) / 3)

#8
n = input("Введите четырехзначное число: ")
n = int(n)

d3 = n % 10
d2 = n % 100 // 10
d1 = n // 100

print("Сумма цифр числа:", d3 + d2 + d1)
print("Сред арифмет:", (d3 + d2 + d1) / 3)
