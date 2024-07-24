from collections import deque
import sys
input = sys.stdin.readline
def reverse_part(text : str, start : int, end : int):
    l = [text[i] for i in range(start, end+1)]
    l.reverse()
    target = ""
    if start != 0:
        target =target + text[0 : start]
    middle = ''.join(str(j) for j in l)
    target = target+ middle
    if end != len(text) - 1:
        target = target + text[end + 1 : len(text)]
    return target

def create_garph_vertices(text: str):
    graph = deque()
    matrix = {}
    matrix.update({text : []})
    graph.append(text)
    while len(graph) != 0:
        x = graph.pop()
        for i in range(len(x)):
            for j in range(i,len(x)):
                sub = reverse_part(x,i,j)
                if sub not in matrix:
                    graph.append(sub)
                    matrix.update({sub: [x]})
                matrix[x].append(sub)
    return matrix

def BFS(edges, v):
    queue = deque()
    visited = {}
    level = {}
    queue.append(v)
    level.update({v : 0})
    visited.update({v : True})
    while queue:
        s = queue.popleft()
        for i in edges[s]:
            if i not in visited:
                queue.append(i)
                visited.update({i : True})
                level.update({i : level[s] + 1})
    return level

def convert(main_text : str, source_text : str, destination_text : str):
    alphabet = {}
    for i in range(len(main_text)):
        alphabet.update({source_text[i] : main_text[i]})
    string_d = ""
    for j in range(len(destination_text)):
        string_d = string_d + alphabet[destination_text[j]]
    return string_d

main_text = "abcdefgh"
n = int(input())
r = int(input())
wnated_text = main_text[0 : n]
matrix = create_garph_vertices(wnated_text)
levels = BFS(matrix, wnated_text)
for i in range(r):
    source, destination = map(str, input().split())
    new_d = convert(wnated_text,source, destination)
    print(levels[new_d])
    
