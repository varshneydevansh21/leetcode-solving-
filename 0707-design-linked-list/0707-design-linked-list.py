class Node:
    def __init__(self, val=0, next=None):
        self.val = val              # Node value
        self.next = next            # Pointer to next node

class MyLinkedList:
    def __init__(self):
        self.head = None            # Start of the list
        self.size = 0               # Number of elements in list

    def get(self, index: int) -> int:
        if index < 0 or index >= self.size:
            return -1
        temp = self.head
        for _ in range(index):      # Move to index-th node
            temp = temp.next
        return temp.val

    def addAtHead(self, val: int) -> None:
        node = Node(val, self.head) # New node points to current head
        self.head = node            # Head is now the new node
        self.size += 1

    def addAtTail(self, val: int) -> None:
        node = Node(val)
        if not self.head:           # If list is empty
            self.head = node
        else:
            temp = self.head
            while temp.next:        # Go to last node
                temp = temp.next
            temp.next = node        # Link last node to new node
        self.size += 1

    def addAtIndex(self, index: int, val: int) -> None:
        if index < 0:
            index = 0
        if index > self.size:       # Out of bounds
            return
        if index == 0:              # Add at head
            self.addAtHead(val)
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next    # Move to node before index
            node = Node(val, prev.next)
            prev.next = node        # Insert node
            self.size += 1

    def deleteAtIndex(self, index: int) -> None:
        if index < 0 or index >= self.size:  # Invalid index
            return
        if index == 0:                       # Delete head
            self.head = self.head.next
        else:
            prev = self.head
            for _ in range(index - 1):
                prev = prev.next            # Move to node before index
            prev.next = prev.next.next      # Bypass target node
        self.size -= 1