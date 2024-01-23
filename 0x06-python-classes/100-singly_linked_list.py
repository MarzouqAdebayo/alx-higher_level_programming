#!/usr/bin/python3
"""Defines the Node and SinglyLinkedList classes"""


class Node:
    """
    Node class represents a node in a singly linked list.

    Attributes:
        _data (int): The data stored in the node.
        _next_node (Node): The reference to the next node in the list.

    Methods:
        __init__(self, data, next_node=None): Initializes a new node.
        data (property): Getter method for the data attribute.
        data (setter): Setter method for the data attribute.
        next_node (property): Getter method for the next_node attribute.
        next_node (setter): Setter method for the next_node attribute.
        __str__(self): Returns a string representation of the node.
    """

    def __init__(self, data, next_node=None):
        """
        Initializes a new node.

        Args:
            data (int): The data to be stored in the node.
            next_node (Node, optional): The reference to the next node.
                Defaults to None.
        """
        if not isinstance(data, int):
            raise TypeError("data must be an integer")
        self.__data = data
        self.__next_node = next_node

    @property
    def data(self):
        """
        Getter method for the data attribute.

        Returns:
            int: The data stored in the node.
        """
        return self.__data

    @data.setter
    def data(self, value):
        """
        Setter method for the data attribute.

        Args:
            value (int): The new value to set for the data attribute.

        Raises:
            TypeError: If the provided value is not an integer.
        """
        if not isinstance(value, int):
            raise TypeError("data must be an integer")
        self.__data = value

    @property
    def next_node(self):
        """
        Getter method for the next_node attribute.

        Returns:
            Node: The next node or None if there is no next node.
        """
        return self.__next_node

    @next_node.setter
    def next_node(self, value):
        """
        Setter method for the next_node attribute.

        Args:
            value (Node): The new reference to the next node.

        Raises:
            TypeError: If the provided value is not a Node object.
        """
        if value is not None and not isinstance(value, Node):
            raise TypeError("next_node must be a Node object")
        self.__next_node = value

    def __str__(self):
        """
        Returns a string representation of the node.

        Returns:
            str: The string representation of the node's data.
        """
        return str(self.__data)


class SinglyLinkedList:
    """
    SinglyLinkedList class represents a singly linked list.

    Attributes:
        __head (Node): The head of the linked list.

    Methods:
        __init__(self): Initializes an empty linked list.
        sorted_insert(self, value): Inserts a new node with the given value
            in sorted order.
        display(self): Displays the data of all nodes in the linked list.
    """

    def __init__(self):
        """
        Initializes an empty linked list.
        """
        self.__head = None

    def sorted_insert(self, value):
        """
        Inserts a new node with the given value in sorted order.

        Args:
            value: The value to be inserted into the linked list.
        """
        new_node = Node(value)
        if self.__head is None:
            self.__head = new_node
        else:
            if value <= self.__head.data:
                new_node.next_node = self.__head
                self.__head = new_node
            else:
                current = self.__head
                while current.next_node:
                    if current.next_node.data > value:
                        break
                    current = current.next_node
                new_node.next_node = current.next_node
                current.next_node = new_node

    def __str__(self):
        """
        Returns a string representation of the linked list.

        Returns:
            str: The string representation of the linked list.
        """
        result = ""
        current = self.__head
        while current:
            result += str(current.data)
            if current.next_node:
                result += "\n"
            current = current.next_node
        return result
