"""
Difficulty: Easy
Category: linked Lists

Middle Node

You're given a Linked List with at least one node. Write a function that returns the middle node of the 
Linked List. If there are no two middle nodes(i.e. an even legth list), your function should return the second
of these nodes.

Each LinkedList node has an integer value as well as a next node pointing to the next node in the list
or to None if It's the tail of the list.
"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None

    def middle_node(LinkedList):
        slow_node = LinkedList
        fast_node = LinkedList

        while fast_node and fast_node.next:
            slow_node = slow_node.next
            fast_node = fast_node.next.next

        return slow_node