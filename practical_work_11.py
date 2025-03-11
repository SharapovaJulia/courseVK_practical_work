import re
answer = []
string = input().lower()
string = re.sub(r'[^a-z0-9\s]', '', string)
string_sorted = string.split(' ')
for x in string_sorted:
    unique_symbols = set(x)
    if len(x) >= 5 and len(unique_symbols) >= 4 and string_sorted.count(x) > 2:
        answer.append(x)
answer = sorted(set(answer))
for i in range (len(answer)):
    print(answer[i])