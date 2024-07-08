import numpy as np;
from queue import Queue;
import random
from collections import deque

# ARRAYS

# Creating an array

arr = np.array([1, 2, 3, 4, 5])
# print(arr)

# Arithmetical operation on whole array

# print(arr + 2)

# Usage the addition, substraction, multiplication, division operations

arr1 = np.array([1, 2, 3]) 
arr2 = np.array([4, 5, 6]) 
# print(arr1 + arr2)

# Agregation functions

# print(np.sum(arr))
# print(np.mean(arr))
# print(np.max(arr))
# print(np.min(arr))

#  3 X 3 array

arr3 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])



# LISTS

my_list = [1, 2, 3, 4, 5]


# Appending list

my_list.append(6)

# Insertion element into a special postion

my_list2 = [1, 2, 4, 5]

my_list2.insert(3,4)


# Removal element
my_list.remove(3)


# Sorting list

my_list3 = [3, 1, 4, 1, 5, 9, 2]
my_list3.sort()




# DICTIONARIES

my_dict={'name': 'John', 'age': 25}


# taking value by key
# print(my_dict['name'])

# changing value
my_dict['age'] = 38
my_dict['city'] = 'Kyiv'

# print(my_dict)

del my_dict['age']

# print(my_dict)

# SETS

my_set = set([1,2,3,4,5])
my_set.add(6)
my_set.remove(1)
my_set.discard(2)
# print(my_set)

set_1 = {1, 2, 3, 4, 5}
set_2 = {4, 5, 6, 7, 8}


# print(set_1.union(set_2)) # об'єднання
# print(set_1.intersection(set_2)) # перетин
# print(set_1.difference(set_2)) # різниця
# print(set_1.symmetric_difference(set_2)) # сіметрична різниця

# STACK

# stack = []

# stack.append('a')
# stack.append('b')
# stack.append('c')
# print(stack)
# print(stack.pop())
# print(stack)


# проверка верхнего элемента стека
# def peek(stack):
#   return stack[-1]

# print(peek(stack))

# проверка пустоты стека
# def is_empty(stack):
#   return len(stack) == 0

# print(is_empty(stack))


# STACK CLASS 

class Stack:
    def __init__(self):
      self.stack = []

  # Adding element to stack
    def push(self, item):
      self.stack.append(item)
  
  # Deleting element from stack
    def pop(self):
      if len(self.stack) < 1:
        return None
      return self.stack.pop()

  # Checking the emptiness od stack
    def is_empty(self):
      return len(self.stack) == 0

  # Taking the top element without deleting
    def peek(self):
      if not self.is_empty():
        return self.stack[-1]
    
    def len(self):
      return len(self.stack)


s = Stack()
s.push('a')
s.push('b')
s.push('c')
s.push('d')


# print(s.len())
# print(s.pop())
# print(s.len())
# print(s.peek())
# print(s.is_empty())

#QUEUE

# q = Queue(maxsize=3)

# # print(q.empty())

# q.put('a')
# q.put('b')
# q.put('c')

# # print(q.full())
# # print(q.qsize())

# q.get('a')
# q.get('b')
# print(q.qsize())


# Clients in Bank

# class Client:
#   def __init__(self, name):
#     self.name = name
#     self.operations = random.randint(1, 5)

# class Bank:
#   def __init__(self):
#     self.clients = Queue()

#   def new_client(self, client):
#     self.clients.put(client)

#   def serve_clients(self):
#     while not self.clients.empty():
#       current_client = self.clients.get()
#       print(f"Обслуговуэмо клієнта {current_client.name} з {current_client.operations} операцій")  


# bank = Bank()

# for i in range(5):
#   bank.new_client(Client(f"Клієнт{i}"))

# bank.serve_clients()

# DEQUE

# d = deque()


# d.append('right')
# d.appendleft('left')

# d.pop()
# d.popleft()

# d.extend(['a', 'b', 'c'])
# d.extendleft(['x', 'y', 'z'])
# print(d)

# d.rotate(-2)
# print(d)

# Обмеження розміру

# d = deque(maxlen=5)
# d.extend([1, 2, 3, 4, 2, 5])
# print(d.count(2))


# LINKED LIST

# class Node:
#   def __init__(self, data=None):
#     self.data = data
#     self.next = None

# class LinkedList:
#   def __init__(self):
#     self.head = None

# # insert at the beggining

#   def insert_at_the_beginning(self, data):
#     new_node = Node(data)
#     new_node.next = self.head
#     self.head = new_node


#   def insert_at_end(self, data):
#     new_node = Node(data)
#     if self.head is None:
#       self.head = new_node
#     else:
#       cur = self.head
#       while cur.next:
#         cur = cur.next
#       cur.next = new_node


# # insert after

#   def insert_after(self, prev_node: Node, data):
#     if prev_node is None:
#       print("The previous Node doesen't exist")
#       return
#     new_node = Node(data)
#     new_node.next = prev_node.next
#     prev_node.next = new_node

#   def delete_node(self, key: int):
#     cur = self.head
#     if cur and cur.data == key:
#       self.head = cur.next
#       cur = None
#       return
#     prev = None
#     while cur and cur.data != key:
#       prev = cur
#       cur = cur.next
#     if cur is None:
#       return
#     prev.next = cur.next
#     cur = None

#   def search_element(self, data) -> Node | None:
#     cur = self.head
#     while cur: 
#       if cur.data == data:
#         return cur
#       cur = cur.next
#       return None

#   def print_list(self):
#     current = self.head
#     while current:
#       print(current.data)
#       current = current.next


# llist = LinkedList()

# llist.insert_at_the_beginning(5)
# llist.insert_at_the_beginning(10)

# llist.insert_at_end(15)

# # llist.print_list()

# llist.delete_node(10)

# llist.print_list()

# print('\searching elem 15:')
# element = llist.search_element(15)
# if element:
#   print(element.data)


# DOUBLE LINKED LIST

# class Node:
#   def __init__ (self, data):
#     self.data = data
#     self.next = None
#     self.prev = None


# class DoublyLinkedList:
#   def __init__(self):
#     self.head = None
#     self.tail = None

#   def append(self, data):
#     new_node = Node(data)
#     if self.head is None:
#       self.head = new_node
#       self.tail = self.head
#     else:
#       self.tail.next = new_node
#       new_node.prev = self.tail
#       self.tail = new_node

#   def push(self,data):
#     new_node = Node(data)
#     new_node.next = self.head
#     if self.head:
#       self.head.prev = new_node
#     else:
#       self.tail = new_node
#     self.head = new_node

#   def insert_after(self, prev_node, data):
#     if not prev_node:
#       return
#     new_node = Node(data)
#     new_node.next = prev_node.next
#     prev_node.next = new_node
#     new_node.prev = prev_node
#     if new_node.next:
#       new_node.next.prev = new_node
#     else:
#       self.tail

# def insert_before(self, next_node, data):
#   if not next_node:
#     return
#   new_node = Node(data)
#   new_node.prev = next_node.prev
#   next_node.prev = new_node
#   if new_node.prev:
#     new_node.prev.next = new_node
#   else:
#     self.head = new_node 

# def remove(self.data):
#   current_node = self.head
#   while current_node:
#     if current_node.data == data:
#       if current_node.prev:
#           current_node.prev.next = current_node.next
#       else:
#         self.head = current_node.next
#       if current_node.next:
