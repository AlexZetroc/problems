"""
Difficulty: Easy
Category: Linked Lists

Remove Duplicates From Linked List

You're given the head of a Singly Linked List whose nodes are in sorted order with respect to their values.
Write a function that returns a modified version of the Linked List that doesn't contain any nodes with duplicate values.
The Linked List should be modified in place (i.e., you shouldn't createa a brand new list), and then modified Linked List
should still have its nodes sorted with respect to their values.

Each LinkedList node has an integer "value" as well as a "next" nmode pointing to the next node in the list
or to None/Null if it's the tail of the list

"""

class LinkedList:
    def __init__(self, value):
        self.value = value
        self.next = None


def remove_duplicates_from_linked_list(LinkedList):
    current_node = LinkedList
    while current_node is not None:
        next_different_node = current_node.next
        while next_different_node is not None and next_different_node.value == current_node.value:
            next_different_node = next_different_node.next

        current_node.next = next_different_node
        current_node = next_different_node

    return LinkedList


# This section is only for the test
# Define the LinkedList
head_node = LinkedList(1)
nodes = [
    {"id": "1-2", "next": "1-3", "value": 1},
    {"id": "1-3", "next": "2", "value": 1},
    {"id": "2", "next": "3", "value": 3},
    {"id": "3", "next": "3-2", "value": 4},
    {"id": "3-2", "next": "3-3", "value": 4},
    {"id": "3-3", "next": "4", "value": 4},
    {"id": "4", "next": "5", "value": 5},
    {"id": "5", "next": "5-2", "value": 6},
    {"id": "5-2", "next": None, "value": 6}
]

# Create the linked list based on the node data
current_node = head_node
for node_data in nodes:
    new_node = LinkedList(node_data["value"])
    current_node.next = new_node
    current_node = new_node

result = remove_duplicates_from_linked_list(head_node)

# Print the values of the resulting linked list to verify
current_node = result
while current_node is not None:
    print(current_node.value)
    current_node = current_node.next