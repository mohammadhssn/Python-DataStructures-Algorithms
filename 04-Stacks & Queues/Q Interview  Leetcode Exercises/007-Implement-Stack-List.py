"""
Instructions:
Stack: Implement Stack Using a List (⚡Interview Question)
In the Stack: Intro video we discussed how stacks are commonly implemented using a list instead of a linked list.

Create a constructor for Class Stack that implements a new stack with an empty list.
"""


class Stack:
    def __init__(self) -> None:
        self.stack_list = []
