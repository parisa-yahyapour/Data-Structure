s = input()
i = 0
p = 0
l = []
m = -1
while i != len(s):
    if s[i] not in l:
        l.append(s[i])
        i += 1
    else:
        m = max(m , len(l))
        p += 1
        i = p
        l.clear()
print(max(len(l), m))
