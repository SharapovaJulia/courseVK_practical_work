#Необходимо написать программу, которая будет считывать со стандартного ввода положительное целое число – порядковый номер 1 <= n <= 30, и выводить n-е по счету число Фибоначчи. Числа Фибоначчи это последовательность чисел такая, что каждое следующее число это сумма двух предыдущих. Первое и второе числа Фибоначчи это числа 1. То есть первые два числа это 1 и 1, третье число это 2 (сумма первого и второго), четвертое число это 3 (сумма второго и третьего), пятое – 5, шестое – 8 и так далее. Нужно написать этот код с помощью рекурсии.
import time
start_time = time.time()
def fibonacci(n):
    numbers = [1, 1]
    for i in range(n-2):
        numbers.append(numbers[i] + numbers[i + 1])
    return numbers[-1]


# fibonacci_numbers = {}
# def fibonacci(n):
#     if n in fibonacci_numbers:
#         value = fibonacci_numbers[n]
#     elif n == 1 or n == 2:
#         value = 1
#     else:
#         value = fibonacci(n -2) + fibonacci(n -1)
#     fibonacci_numbers[n] = value
#     return value

number = int(input())
print(fibonacci(number))

end_time = time.time()
execution_time = end_time - start_time
print(f"Время выполнения: {execution_time} секунд")