# Реалізація однозв'язного списку з конспекту, додані методи для виконання завдання виділені коментарями

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next: Node | None = None


class LinkedList:
    def __init__(self):
        self.head = None

    def insert_at_beginning(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            cur = self.head
            while cur.next:
                cur = cur.next
            cur.next = new_node

    def insert_after(self, prev_node: Node, data):
        if prev_node is None:
            print("Попереднього вузла не існує.")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node

    def delete_node(self, key: int):
        cur = self.head
        if cur and cur.data == key:
            self.head = cur.next
            cur = None
            return
        prev = None
        while cur and cur.data != key:
            prev = cur
            cur = cur.next
        if cur is None:
            return
        if prev is not None:
            prev.next = cur.next
        cur = None

    def search_element(self, data: int) -> Node | None:
        cur = self.head
        while cur:
            if cur.data == data:
                return cur
            cur = cur.next
        return None

    def print_list(self):
        current = self.head
        while current:
            print(current.data)
            current = current.next
            
    # 1. реверсування однозв'язного списку, змінюючи посилання між вузлами
    def reverse_list(self):
        prev = None
        current = self.head
        
        while current is not None:
            next_node = current.next
            current.next = prev
            prev = current
            current = next_node
            
        self.head = prev

    # 2. алгоритм сортування для однозв'язного списку - сортування вставками
    def insertion_sort(self):
        if self.head is None or self.head.next is None:
            return
        
        sorted_head = None
        current = self.head
        
        while current is not None:
            next_node = current.next
            
            if sorted_head is None or sorted_head.data >= current.data:
                current.next = sorted_head
                sorted_head = current
            else:
                temp = sorted_head
                while temp.next and temp.next.data < current.data:
                    temp = temp.next
                    
                current.next = temp.next
                temp.next = current
                
            current = next_node
            
        self.head = sorted_head
        
# 3. функція, що об'єднує два відсортовані однозв'язні списки в один відсортований список
def merge_sorted_lists(llist1, llist2):
    merged_list = LinkedList()
    
    current1 = llist1.head
    current2 = llist2.head
    
    if current1 is None:
        while current2:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next
        return merged_list
    if current2 is None:
        while current1:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        return merged_list
    
    while current1 and current2:
        if current1.data <= current2.data:
            merged_list.insert_at_end(current1.data)
            current1 = current1.next
        else:
            merged_list.insert_at_end(current2.data)
            current2 = current2.next
    
    while current1:
        merged_list.insert_at_end(current1.data)
        current1 = current1.next
        
    while current2:
        merged_list.insert_at_end(current2.data)
        current2 = current2.next
    
    return merged_list
        
# == Тестування реверсування ==
llist = LinkedList()
llist.insert_at_end(1)
llist.insert_at_end(2)
llist.insert_at_end(3)
print("Original List:")
llist.print_list()
llist.reverse_list()
print("Reversed List:")
llist.print_list()
print("=" * 40)

# == Тестування сорутвання ==
llist = LinkedList()
llist.insert_at_end(5)
llist.insert_at_end(2)
llist.insert_at_end(8)
llist.insert_at_end(1)
llist.insert_at_end(9)
print("Original List:")
llist.print_list()
llist.insertion_sort()
print("Sorted List:")
llist.print_list()
print("=" * 40)

# == Тестування об'єднання двох відсортованих списків ==
llist1 = LinkedList()
llist1.insert_at_end(1)
llist1.insert_at_end(3)
llist1.insert_at_end(5)
llist1.insert_at_end(7)
print("First sorted list:")
llist1.print_list()

llist2 = LinkedList()
llist2.insert_at_end(2)
llist2.insert_at_end(4)
llist2.insert_at_end(6)
llist2.insert_at_end(10)
llist2.insert_at_end(11)
print("Second sorted list:")
llist2.print_list()

merged_list = merge_sorted_lists(llist1, llist2)
print("Merged sorted list:")
merged_list.print_list()