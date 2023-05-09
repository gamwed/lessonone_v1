# Firts task
# numbers = []
# for i in range(5):
#     number = int(input("Введіть ціле число: "))
#     numbers += [number]
#
# minimum = min(numbers)
# maximum = max(numbers)
# average = sum(numbers) / len(numbers)
#
# print("Мінімум:", minimum)
# print("Максимум:", maximum)
# print("Середнє:", average)


# 2 task
# x = float(input("Ведіть перше число: "))
# y = float(input("Ведіть друге число: "))
# print("Складання: ", x+y)
# print("Віднімання: ", x-y)
# print("Множення: ", x*y)
# print("Ділення: ", x/y)

#  3 task
# import math
# r = float(input("Ведить радіус кола, який ви хочете разрухавати"))
# print("Диаметр кола= ", r*2)
# print("Довжина кола= ", 2*math.pi*r)
# print("Площа кола= ", math.pi*(r*r))

# 4 task
# xyz = []
# xyz = input("введіть тризначне число: ")
# print(xyz[0])
# print(xyz[1])
# print(xyz[2])

xyz = int(input("введіть тризначне число: "))

print("Перше: ",xyz//100)
print("Друге: ",(xyz//10)%10)
print("Трете: ",xyz % 10)

# 5 task
# invest = int(input("Введіть сумму депозиту: "))
# years = int(input("На скількі років"))
# print("Прибуток=  ", (invest*10)/100)**years)