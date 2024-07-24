import sys
import re


class Queue:
    def __init__(self):
        self.data = []

    def getSize(self):
        return len(self.data)

    def enqueue(self, value):
        self.data.append(value)

    def dequeue(self):
        if len(self.data) != 0:
            temp = self.data[0]
            self.data.remove(temp)
            return temp
        else:
            return None

    def isEmpty(self):
        return (len(self.data) == 0)

    def getInOneLine(self):
        if len(self.data) != 0:
            return ' '.join(str(n) for n in self.data)
        else:
            return None


class Stack:
    def __init__(self, size=10):
        self.size_data = size
        self.data = []

    def isEmpty(self):
        return (len(self.data) == 0)

    def push(self, value):
        if self.size_data > len(self.data):
            self.data.append(value)

    def pop(self):
        if len(self.data) != 0:
            return self.data.pop(len(self.data) - 1)
        else:
            return None

    def put(self, value):
        if len(self.data) != 0:
            self.pop()
        self.push(value)

    def peek(self):
        if len(self.data) != 0:
            return self.data[len(self.data) - 1]
        else:
            return None

    def expand(self):
        self.size_data *= 2

    def getInOneLine(self):
        if len(self.data) != 0:
            return ' '.join(str(n) for n in self.data)
        else:
            return None

    def getSize(self):
        return len(self.data)

    def getCapacity(self):
        return self.size_data


class Node:
    def __init__(self, val):
        self.data = val
        self.next = None
    


class LinkedList:
    
    def __init__(self):
        self.head = Node(None)

    def getList(self):
        n = self.head.next
        str = ""
        if n != None:
            while n != None:
                str = str + n.data + " "  
                n = n.next
        return str
        

    def insertFront(self, new_data):
        new_node = Node(new_data)
        pre = self.head.next
        (self.head).next = new_node
        new_node.next = pre

    def insertEnd(self, new_data):
        current = self.head.next
        if current != None:
            while current.next != None:
                current = current.next
            new_node = Node(new_data)
            current.next = new_node
        else:
            self.insertFront(new_data)
        

    def reverse(self):
        if self.head.next != None:
            list_nodes = []
            n = self.head.next
            while n != None:
                list_nodes.append(n)
                n = n.next
            list_nodes.reverse()
            for i in range(len(list_nodes) - 1):
                list_nodes[i].next = list_nodes[i+1]
            list_nodes[len(list_nodes) - 1].next = None
            self.head.next = list_nodes[0]


class Runner:
    dsMap = {'stack': Stack, 'queue': Queue, 'linked_list': LinkedList}
    callRegex = re.compile(r'^(\w+)\.(\w+)\(([\w, ]*)\)$')

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
        args = argsList.split(',') if argsList != '' else []

        method = getattr(self.items[itemName], funcName)
        result = method(*args)
        if result is not None:
            print(result)


def main():
    runner = Runner(sys.stdin)
    runner.run()


if __name__ == "__main__":
    main()
