#This is the Python script to implement Linked List. Please stop reading book, I spent more than 1 week for nothing
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def get_item(self, n):
        i = 1
        cur_node = self.head
        while i < n:
            if cur_node.next:
                cur_node = cur_node.next
                i += 1
            else:
                print('''Linked List doesn't have this item''')
        return cur_node.data
    
    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return

        last_node = self.head
        while last_node.next:
            last_node = last_node.next
        last_node.next = new_node

    def prepend(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # def insert_after_node(self, prev_node, data):
    #     if not prev_node:
    #         print('There is no previous node')
    #     new_node = Node(data)
    #     new_node.next = prev_node.next
    #     prev_node.next = new_node

    def get_size(self):
        cur_node = self.head
        i = 1
        while cur_node.next:
            cur_node = cur_node.next
            i += 1
        return i
        
llist = LinkedList()
llist.append(1)
llist.append(2)
llist.append(3)
llist.prepend('A')
# # llist.insert_after_node(llist.get_item(3), 'B')
# llist.print_list()
# print(llist.get_item(2))
# print(llist.get_size())
print(llist.head)



    
