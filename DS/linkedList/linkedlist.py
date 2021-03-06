# 'Create node'

class node:
    def __init__(self, data=None):
        self.data = data
        self.next = None


class linkedlist:
    def __init__(self):
        self.head = node()

    def append(self, data):
        new_node = node(data)
        current = self.head

        while current.next is not None:
            current = current.next

        current.next = new_node

    def length(self):
        current = self.head
        total = 0
        while current.next is not None:
            total += 1
            current = current.next
        return total

    def display(self):
        elements = []
        current_node = self.head
        while current_node.next is not None:
            current_node = current_node.next
            elements.append(current_node.data)
        print(elements)

    def retrieve(self, index):
        if index >= self.length():
            print("Too much")
            return None

        current_index = 0
        current_node = self.head
        while True:
            current_node = current_node.next
            if current_index == index:
                return current_node.data

            current_index += 1

    def remove(self, index):
        if index > self.length():
            print("Too much")
            return None

        current_index = 0
        current_node = self.head

        while True:
            last_node = current_node
            current_node = current_node.next
            if current_index == index:
                last_node.next = current_node.next
                return
            current_index +=1

my_list = linkedlist()

my_list.display()

my_list.append(1)
my_list.append(9)
my_list.append(34)
my_list.append(5)

my_list.display()

print(my_list.retrieve(1))

my_list.remove(1)

my_list.display()