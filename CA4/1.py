n,m = map(int, input().split())
v = {}
for i in range(m):
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


def BFS(visited, edges, s, team, colors):
    queue = []
    queue.append(s)
    visited[s] = True
    colors[s] = team
    while queue:
        queue.pop(0)
        for i in edges[s]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True
                colors[i] = not team

visited = [False] * n
color = [-1] * n
team = False
for i in range(n):
    if visited[i] == False:
        BFS(visited, v, i, team, color)

team1 = []
for i in range(n):
    if color[i] == True:
        team1.append(i + 1)
print(len(team1))
print(" ".join(str(i) for i in team1))


