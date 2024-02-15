"""
Difficulty: Easy
Category: Graphs

Depth-first search

you're given a Node class that has a name and an array of optional children nodes. When put together, the
nodes form an acyclic tree-like structure.

Implement the depth_first_search meethod on the Node class, which takes in an empty array, traverses the tree
using the Depth-first Search approach (specifically navigating the tree from left to right), stores all of the nodes'
names in the input array, and returns it.
"""

class Node:
    def __init__(self, name):
        self.children = []
        self.name = name

    def add_child(self, name):
        self.children.append(Node(name))
        return self

    def depth_first_search(self, array):
        array.append(self.name)
        for child in self.children:
            child.depth_first_search(array)
        return array