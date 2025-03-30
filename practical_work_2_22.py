from typing import List, Dict

def make_most_common_keys(d: Dict[int, int]) -> List[int]:
    l = []
    d = {k: v for v, k in d.items()}
    v = sorted(d, reverse=True)
    for i in v:
        l.append(d[i])
    return l

code = []
while data := input():
  code.append(data)
code = "\n".join(code)
exec(code)
