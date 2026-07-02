numbers = []
accepted = True
while True:
    num = int(input('Enter number:').strip())
    if num == 0:
        break
    numbers.append(num)

for i in range(len(numbers)):
    for j in range(len(numbers)-1):
       if numbers[j]>numbers[j+1]:
           numbers[j],numbers[j+1] = numbers[j+1],numbers[j]

   
print(numbers)