N = int(input())
numbers = []
for i in range(N):
    numbers.append(int(input()))

# Для сортировки воспользуемся алгоритмом Шелла
last_index = len(numbers) - 1
step = len(numbers) // 2
while step > 0:
    for i in range(step, last_index + 1, 1):
        j = i
        delta = j - step
        while delta >= 0 and numbers[delta] < numbers[j]:
            numbers[delta], numbers[j] = numbers[j], numbers[delta]
            j = delta
            delta = j - step
    step //= 2

for number in numbers:
    print(number)
