#START Question 1
numbers = []

for i in range(1, 101): # a question
    numbers.append(i)

print(numbers[0])   # b question
print(numbers[-1])  # c question
print(f'in array have {len(numbers)} index')  # d question
print(numbers[2: 12])  # e question
print(numbers[79:])   # f question
print(numbers[0: 17])  # g question
print(numbers[:: -1])  # h question
print(numbers[1:100:2])  # i question
print(numbers[2:100:3])  # j question
print(numbers[6:100:7])  # k question
print(numbers[9:100:10])  # l question
print(numbers[98:64:-3])  # m question
print(numbers.insert(49, 999))  # n question
print(numbers.pop(100))  # o question
#END

#START Question 2

array: list[float] = []
num = 0

while num != -999:
    num: float = float(input("Enter a your height: "))
    if 1.60 <= num <= 3 :
        array.append(num)
    else:
        continue

print(array)

print(f"{len(array)} players were taken")
print(f"The height of the tallest player is {max(array)} meters")
print(f"The height of the shortest player is {min(array)} meters")

count = 0
for i in array:
    if i > 2:
        count += 1

print(f"{count} players taller than 2 meters")

average = sum(array) // len(array)
count2 = 0
for i in array:
    if i > average:
        count2 += 1

print(f"{count2} players are taller than average")
#END

#START Question 3
numbers = [i for i in range(10, 101, 10)]
while True:
    num2 = int(input("Enter a number : "))
    if num2 == -999:
        break
    for i in range(len(numbers)):
        if num2 <= numbers[i]:
            numbers.insert(i, num2)
            break
print(numbers)
#END