
class Node:
    def __init__ (self, a , t , s) :
        self.A = a
        self.T = t
        self.S = s

    def __lt__ (self, node) :
        return self.S < node.S
        
    def __eq__(self, node):
        return self.S == node.S
            
def bubble_up(index, data : list):
    index_parent = int((index - 1)/2)
    current_node = data[index]
    while index > 0 and current_node.__lt__(data[index_parent]):
        data[index] = data[index_parent]
        index = index_parent
        index_parent = int((index_parent - 1) / 2)
    data[index] = current_node 


def bubble_down(index, data : list):
        current_node = data[index]
        temp = 0
        while index < int(len(data)/2) and len(data) != 1:
            right_child = 2 * index + 2
            left_child = 2 * index + 1
            if right_child < len(data) and data[right_child].__lt__(data[left_child]):
                temp = right_child
            else:
                temp = left_child
            if current_node.__lt__(data[temp]) or current_node.__eq__(data[temp]):
                break
            data[index] = data[temp]
            index = temp
        data[index] = current_node

def heap_push(value, data : list):
        for i in value:
            data.append(i)
            bubble_up(len(data) - 1, data)

def heap_pop(data : list):
        if len(data) == 0:
             return
        data[0] = data[len(data) - 1]
        data.pop()
        if len(data) != 0:
            bubble_down(0, data)


n_s = input().split()
num = int(n_s[0])
day = int(n_s[1])
dic = {}
total  = 0
for i in range(num):
    temp = input().split()
    new_node = Node(int(temp[0]), int(temp[1]), -int(temp[2]))
    sum = int(temp[1]) * -int(temp[2])
    total += sum
    if int(temp[0]) not in dic:
        dic.update({int(temp[0]) : [new_node]})
    else:
        dic[int(temp[0])].append(new_node)
days = []
ld = len(dic)
for d in range(1, day+1):
    if ld != 0:
        if d in dic:
            heap_push(dic[d], days)
            ld -= 1
    if len(days) != 0:
        days[0].T -= 1
        total -= days[0].S
        if days[0].T == 0:
            heap_pop(days)
print(-total)
