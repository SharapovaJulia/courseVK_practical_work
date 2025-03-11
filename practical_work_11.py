answer = []
string = input().lower()
symbols = '!,.?;:#$%^&*(),'

for x in symbols:
    if x in string:
        string = string.replace(x, '')

string_sorted = string.split(' ')
for x in string_sorted:
    unique_symbols = set(x)
    if len(x) >= 5 and len(unique_symbols) >= 4 and string_sorted.count(x) > 2:
        answer.append(x)
answer = sorted(set(answer))
for i in range (len(answer)):
    print(answer[i])