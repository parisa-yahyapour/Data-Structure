n = int(input())
v = {}
for i in range(n - 1):
    s,d = map(int, input().split())
    s -= 1
    d -= 1
    if s in v:
        v[s].append(d)
    else:
        temp = []
        temp.append(d)
        v.update({s : temp})
    if d in v:
        v[d].append(s)
    else:
        temp = []
        temp.append(s)
        v.update({d : temp})
temp = input().split()
l = [int(i) - 1 for i in temp]
l.insert(0,0)

def BFS(edges, v, num_v):
    queue = []
    visited = [False] * num_v
    parent = [-1] * num_v
    queue.append(v)
    visited[v] = True
    while queue:
        s = queue.pop(0)
        for i in edges[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                parent[i] = s
    return parent

def find_pass(s , d, parents):
    temp = parents[d]
    path = []
    path.append(d)
    while temp != s:
        path.append(temp)
        temp = parents[temp]
    path.reverse()
    return path



path_f = []
path_f.append(0)
for i in range(len(l) - 1):
    parents = BFS(v, l[i], n)
    path_f.extend(find_pass(l[i], l[i + 1], parents))
parent2 = BFS(v, l[-1], n)
path_f.extend(find_pass(l[-1],0,parent2))
path_f.pop()
if len(path_f) == 2*n - 2:
    print(" ".join(str(i + 1) for i in path_f))
else:
    print("-1")
