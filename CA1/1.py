s = list(input())
n = {0 :1, 1 : 0}
p = [0]*1024
p[0] = 1
ans = 0


def to_decimal(l :list)-> int:
    sum = 0
    for i in range(len(l)):
        sum += l[i] * pow(2,i)
    return sum

a = [0,0,0,0,0,0,0,0,0,0]
for c in range(len(s)):
    a[ord(s[c]) - 97] = n[a[ord(s[c]) - 97]]
    ans += p[to_decimal(a)]
    for i in range(10):
        b = a.copy()
        b[i] = n[b[i]]
        ans += p[to_decimal(b)]
    p[to_decimal(a)] += 1
print(ans)
