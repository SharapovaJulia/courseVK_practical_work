def map(func, seq):
   for y in seq:
      yield func(y)

func_in, seq_in = eval(input()), eval(input())

for x in map(func_in, seq_in):
   print(x)