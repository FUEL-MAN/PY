# Данные за 2 дня
temp = [-9.1,-10.5,-11,-10.7,-10.5,-11.4,-11.6,-12.1]
# Средняя температура
# Температура положительная или отрицательная: лід/вода.
# Уменьшается/увеличивается
# Минимальные и максимальные показатели.
avg_temp = sum(temp)/len(temp)
print(avg_temp)
if max(temp)<0:
    print("Температура выше 0 не поднималась")
else:
    print("Температура поднималась выше 0 ")
t0 = temp[0]
sum = 0
for i in range(len(temp)-1):
    print(temp[i+1]-temp[i])
    sum+=temp[i+1]-temp[i]
print("sum",sum)
print("min",min(temp))
print("max",max(temp))
