
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

    # O(n) linear running time
    def remove(self, data):
        # The list is empty
        if self.head is None:
            return
        actual_node = self.head
        # We have to track the previous node for future pointer updates
        # This is why doubly linked lists are better - We can get the previous
        # node (Here with linked list it is impossible
        previous_node = None

        # Search for the item we want to remove (data)
        while actual_node is not None and actual_node.data != data:
            previous_node = actual_node
            actual_node = actual_node.next_node

        # Search miss
        if actual_node is None:
            return

        # Update the references (So we have the data we want to remove)
        if previous_node is None:
            self.head = actual_node.next_node
        else:
            # Remove an internal node by updating the pointers
            # NO NEED to delete the node because the garbage collector will do that
            previous_node.next_node = actual_node.next_node


if __name__ == '__main__':
    linked_list = LinkedList()
    linked_list.insert_end(10)
    linked_list.insert_start(100)
    linked_list.insert_start(1000)
    linked_list.insert_end('Adam')
    linked_list.insert_end(7.5)
    linked_list.traverse()
    print('-----')
    linked_list.remove(2000)
    linked_list.traverse()
    print('-----')
    linked_list.remove('Adam')
    linked_list.traverse()
    print('-----')
    linked_list.remove(1000)
    linked_list.traverse()







