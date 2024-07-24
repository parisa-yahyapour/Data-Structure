bozko = {}
num = int(input())
pos = {}
perv = {}
l = [int(x) for x in input().split()]
for i in range(0,num):
    pos.update({l[i] : i+1})
s1 = []
s1.append(0)
for i in range(num,0,-1):
    while (s1[-1] > pos[i]):
        s1.pop()
    perv.update({i : s1[-1]})
    s1.append(pos[i])
while (len(s1) != 1):
    s1.pop()
print(0)
ans = 0
for i in range(1, num+1):
    while (s1[-1] > pos[i]):
        ans -= bozko[s1[-1]]
        s1.pop()
    if perv[i] != 0 and (s1[-1] == 0 or perv[i] != perv[l[s1[-1] -1 ]]):
        bozko.update({pos[i] : 1})
    else:
        bozko.update({pos[i] : 0})
    s1.append(pos[i])
    ans += bozko[pos[i]]
    print(ans)
