#Необходимо написать программу, которая будет считывать последовательности измерений. В каждой последовательности нужно выбрать максимальное значение, а в итоге вывести отсортированный по убыванию список этих макс значений, разделенных символом “;”. Во входных данных в первой строке будет задано целое положительное число – сколько записей нужно обработать, причем самих записей может быть больше чем это число, это нужно учесть. Значения в рамках одной записи разделены пробелом, минимальное число значений в записи – 1. Записи разделены переводом строки.
count_sequence = int(input())
max_from_the_sequence = []

for i in range(count_sequence):
    sequence = input()
    sequence = sequence.split()
    sequence = [int(x) for x in sequence]
    max_from_the_sequence.append(max(sequence))

max_from_the_sequence.sort(reverse = True)
print(';'.join(map(str, max_from_the_sequence)))