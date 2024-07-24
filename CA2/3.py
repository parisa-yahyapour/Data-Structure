num = int(input())
q = []
d = {}
for i in range(num):
    q.append(int(input()))
for j in q:
    if j not in d:
        d.update({j: 1})
    else:
        d[j] += 1
result = []
step = 0
open_interval = 0
stack = []
for c in q:
    if c == 0:
        result.append(step)
        step = 0
        open_interval  = 0
        stack.clear()
        continue
    elif c not in stack:
        stack.append(c)
        open_interval += 1
    d[c] -= 1
    if d[c] == 0:
        stack.pop()
        step = max(open_interval,step)
        open_interval -= 1
result.append(step)
if len(stack) == 0:
    print(max(result))
else:
    print(-1)
        
            
