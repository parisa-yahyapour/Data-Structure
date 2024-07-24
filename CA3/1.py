import sys
import re


INVALID_INDEX = 'invalid index'
OUT_OF_RANGE_INDEX = 'out of range index'
EMPTY = 'empty'


class MinHeap:
    class Node:
        def __init__(self, value):
            self.value = value
        def get_value(self):
            return self.value

    def __init__(self):
        self.data = []
        self.num_elements = 0

    def bubble_up(self, index):
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index >= len(self.data) or index < 0:
            raise Exception(OUT_OF_RANGE_INDEX)
        index_parent = int((index - 1)/2)
        current_node = self.data[index]
        while index > 0 and current_node.get_value() < (self.data[index_parent]).get_value():
            self.data[index] = self.data[index_parent]
            index = index_parent
            index_parent = int((index_parent - 1) / 2)
        self.data[index] = current_node 


    def bubble_down(self, index):
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index >= self.num_elements or index < 0:
            raise Exception(OUT_OF_RANGE_INDEX)
        current_node = self.data[index]
        temp = 0
        while index < int(len(self.data)/2) and self.num_elements != 1:
            right_child = 2 * index + 2
            left_child = 2 * index + 1
            if right_child < len(self.data) and self.data[left_child].get_value() > self.data[right_child].get_value():
                temp = right_child
            else:
                temp = left_child
            if current_node.get_value() <= self.data[temp].get_value():
                break
            self.data[index] = self.data[temp]
            index = temp
        self.data[index] = current_node

    def heap_push(self, value):
        if type(value) != int:
            raise Exception(INVALID_INDEX)
        new_node = self.Node(value)
        self.data.append(new_node)
        self.num_elements += 1
        self.bubble_up(len(self.data) - 1)

    def heap_pop(self):
        if self.num_elements == 0:
            raise Exception(EMPTY)
        root_value = self.data[0].get_value()
        self.data[0] = self.data[len(self.data) - 1]
        self.data.pop()
        self.num_elements -= 1
        if self.num_elements != 0:
            self.bubble_down(0)
        return root_value

    def find_min_child(self, index):
        if type(index) != int:
            raise Exception(INVALID_INDEX)
        if index >= self.num_elements or index < 0:
            raise Exception(OUT_OF_RANGE_INDEX)
        if index != self.num_elements -1:
            left_child = 2 * index + 1
            right_child = 2 * index + 2
            if self.data[right_child].get_value() > self.data[left_child].get_value():
                return left_child
            else:
                return right_child

    def heapify(self, *args):
        for i in args:
            if type(i) != int:
                raise Exception(INVALID_INDEX)
            self.heap_push(i)



class HuffmanTree:
    class Node:
        def __init__(self, value):
            self.data = value
            self.frequency = None
            self.left_child = None
            self.right_child = None
            
        def get_frequency(self):
            return self.frequency
        
        def set_freq(self, repeat):
            self.frequency = repeat

        def set_left_child(self, left):
            self.left_child = left

        def set_right_child(self,right):
            self.right_child = right

        def get_alphabet(self):
            return self.data
        
        def get_child(self, direction):
            if direction == 'R':
                return self.right_child
            else:
                return self.left_child

    def __init__(self):
        self.letters = []
        self.dic = {}
        self.root = None
    

    def set_letters(self, *args):
        for i in args:
            new_node = self.Node(i)
            self.letters.append(new_node)
            self.dic.update({i : [None,None]})#path , frequency

    def set_repetitions(self, *args):
        index = 0
        for i in args:
            self.letters[index].set_freq(i)
            self.dic[self.letters[index].get_alphabet()][1] = i
            index += 1    

    def sort_method(self, n):
        return n.get_frequency()    

    def build_huffman_tree(self):
        self.letters.sort(key=self.sort_method)
        while len(self.letters) != 1:
            new_node = self.Node(None)
            new_node.set_left_child(self.letters[0])
            sum = self.letters[0].get_frequency()
            self.letters.pop(0)
            new_node.set_right_child(self.letters[0])
            sum += self.letters[0].get_frequency()
            self.letters.pop(0)
            new_node.set_freq(sum)
            self.letters.append(new_node)
            self.letters.sort(key=self.sort_method)
        self.root = self.letters[0]
        self.find_alphabet_codes(self.root)

    def find_alphabet_codes(self, node, path = ''):
        if node != None:
            if node.get_child('R') == None and node.get_child('L') == None:
                self.dic[node.get_alphabet()][0] = path
                return
            left = node.get_child('L')
            right = node.get_child('R')
            self.find_alphabet_codes(left, path + '0')
            self.find_alphabet_codes(right, path + '1')
        return

    def get_huffman_code_cost(self):
        sum = 0
        for i in self.dic:
            sum += len(self.dic[i][0]) * self.dic[i][1]
        return sum 


    def text_encoding(self, text):
        temp = {}
        for i in range(len(text)):
            if text[i] not in temp:
                temp.update({text[i] : 1})
            else:
                temp[text[i]] += 1
        aplphabet = list(temp.keys())
        for i in aplphabet:
            new_node = self.Node(i)
            self.letters.append(new_node)
            self.dic.update({i : [None,None]})#path , frequency
        index = 0
        value = list(temp.values())
        for i in value:
            self.letters[index].set_freq(i)
            self.dic[self.letters[index].get_alphabet()][1] = i
            index += 1 
        self.build_huffman_tree()
        



class Bst:
    class Node:
        def __init__(self,key):
            self.value = key
            self.left = None
            self.right = None
        
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


    def __init__(self):
        self.root = None
        self.num_nodes = 0
        self.inorder_str = ""

    def set_root(self, value):
        new_node = self.Node(value)
        self.root = new_node

    def find_node_place(self,node, new_key):
        if node == None:
            node = self.Node(new_key)
            return node
        if new_key < node.get_value():
            node.set_left_child(self.find_node_place(node.get_child('L'),new_key))
        else:
            node.set_right_child(self.find_node_place(node.get_child('R'),new_key))
        return node

    def insert(self, key):
        if self.root == None:
            self.root = self.Node(key)
        else:
            self.find_node_place(self.root, key)
        self.num_nodes += 1

    def print_tree(self, node):
        if node != None:
            if node.get_child('L') != None:
                self.print_tree(node.get_child('L'))
            self.inorder_str += str(node.get_value())
            self.inorder_str += " "
            if node.get_child('R') != None:
                self.print_tree(node.get_child('R'))

    def inorder(self):
        self.print_tree(self.root)
        print(self.inorder_str)
        self.inorder_str = ""


class Runner:
    dsMap = {'min_heap': MinHeap, 'bst': Bst, 'huffman_tree': HuffmanTree}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, \-"\']*)\)$')

    def __init__(self, inputSrc):
        self.input = inputSrc
        self.items = {}

    def run(self):
        for line in self.input:
            line = line.strip()
            action, _, param = line.partition(' ')
            actionMethod = getattr(self, action, None)
            if actionMethod is None:
                return
            actionMethod(param)

    def make(self, params):
        itemType, itemName = params.split()
        self.items[itemName] = self.dsMap[itemType]()

    def call(self, params):
        regexRes = self.callRegex.match(params)
        itemName, funcName, argsList = regexRes.groups()

        args = [x.strip() for x in argsList.split(',')] if argsList != '' else []
        args = [x[1:-1] if x[0] in ('"', "'") else int(x) for x in args]

        method = getattr(self.items[itemName], funcName)
        try:
            result = method(*args)
        except Exception as ex:
            print(ex)
        else:
            if result is not None:
                print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
