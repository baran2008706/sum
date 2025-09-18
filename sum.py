count = int(input("enter how many numbers you want to sum: "))
lst = []
for counter in range(count):
    number = int(input("number: "))
    lst.append(number)

print(lst)
summ = 0
for i in lst:
    summ += i

print(summ)
