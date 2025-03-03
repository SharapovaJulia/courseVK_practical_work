#Необходимо написать программу, которая будет считывать последовательности измерений. В каждой последовательности нужно выбрать максимальное значение, а в итоге вывести отсортированный по убыванию список этих макс значений, разделенных символом “;”. Во входных данных в первой строке будет задано целое положительное число – сколько записей нужно обработать, причем самих записей может быть больше чем это число, это нужно учесть. Значения в рамках одной записи разделены пробелом, минимальное число значений в записи – 1. Записи разделены переводом строки.
count_sequence = int(input())
search_status = True
max_from_the_sequence = []
while sequence:= list(input().split()):
    if count_sequence != 0:
        for i in range(len(sequence)):
            sequence[i] = int(sequence[i])
        max_from_the_sequence.append(max(sequence))
        count_sequence -= 1
max_from_the_sequence.sort(reverse = True)
print(max_from_the_sequence)