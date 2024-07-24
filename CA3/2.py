VALUE = 0
LEFT_CHILD = 1
RIGHT_CHILD = 2

class Node:
    def __init__(self,key):
        self.value = key
        self.left = None
        self.right = None
        self.father = None
        
    def get_value(self):
        return self.value

    def set_right_child(self, value):
        self.right = value
        
    def set_left_child(self, value):
        self.left = value
      
    def get_child(self, direction):
        if direction == 'R':
            return self.right
        else:
            return self.left
        
    def set_father(self, node):
        self.father = node
    
    def get_father(self):
        return self.father
        
def find_node_place(node : Node, new_node : Node):
        if new_node.get_value() < node.get_value() and node.get_child('L') == None:
            new_node.set_father(node)
            node.set_left_child(new_node)
            return node
        elif new_node.get_value() >= node.get_value() and node.get_child('R') == None:
            new_node.set_father(node)
            node.set_right_child(new_node)
            return node
        elif new_node.get_value() < node.get_value() and node.get_child('L') != None:
            return find_node_place(node.get_child('L'), new_node)
        else:
            return find_node_place(node.get_child('R'), new_node)


def insert(key, root, all_nodes):
    if root == None:
        root = Node(key)
        all_nodes.append(root)
        return root
    else:
        new_node = Node(key)
        father = find_node_place(root, new_node)
        all_nodes.append(new_node)
        return father
    
def find_path_to_root(node):
    path = []
    temp = node
    while temp != None:
        path.append(temp)
        temp = temp.get_father()
    return path

num = int(input())
sequence = input().split()
numbers = input().split()
sequence_nodes = []
output1 = ""
root = insert(int(sequence[0]), None, sequence_nodes)
for i in range(1,num):
    temp = insert(int(sequence[i]), root, sequence_nodes)
    output1 += str(temp.get_value())
    output1 += " "
print(output1)



first_node = sequence_nodes[int(numbers[0]) - 1]
second_node = sequence_nodes[int(numbers[1]) - 1]
first_path = find_path_to_root(first_node)
second_path = find_path_to_root(second_node)
difference = max(len(first_path), len(second_path)) - min(len(first_path), len(second_path))
if difference != 0:
    if max(len(first_path), len(second_path)) == len(first_path):
        for i in range(difference):
            first_path.pop(0)
    else:
        for i in range(difference):
            second_path.pop(0)
lca = None
for i in range(len(first_path)):
    if first_path[i] == second_path[i]:
        lca = first_path[i]
        break
index = 1
for i in sequence_nodes:
    if i == lca:
        print(index)
        break
    index += 1
         


