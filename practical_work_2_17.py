def filter(func, seq):
    for y in seq:
        if func(y):
            yield y

func_in, seq_in = eval(input()), eval(input())

for x in filter(func_in, seq_in):
   print(x)