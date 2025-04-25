class Node:
    def __init__(self, data):
        self.data = data
        self.next_node = None

    def __repr__(self):
        return str(self.data)

class LinkedList:
    def __init__(self):
        self.head = None
        self.num_of_nodes = 0

    # O(1) constant running time
    def insert_start(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            new_node.next_node = self.head
            self.head = new_node

    # O(N)
    def insert_end(self, data):
        self.num_of_nodes += 1
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
        else:
            actual_node = self.head
            while actual_node.next_node is not None:
                actual_node = actual_node.next_node
            actual_node.next_node = new_node

    # O(1) constant running time
    def size_of_list(self):
        return self.num_of_nodes

    # O(n) linear running time
    def traverse(self):
        actual_node = self.head
        while actual_node is not None:
            print(actual_node)
            actual_node = actual_node.next_node

if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_start(10)
    linked_list.insert_start('Adam')
    linked_list.insert_start(7.5)
    linked_list.insert_end(100)
    linked_list.insert_end(1000)
    linked_list.traverse()