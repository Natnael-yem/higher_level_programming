#!/usr/bin/python3
"""defines a class student."""

class Student:
    "Represent a student."""

    def __init__(self, first_name, last_name, age):
        """initialize a new student.

        args:
            first_name (str): the first name of the student.
            last_name (str): the last name of the student.
            age (int): the age of the student.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """get a dictionary representation of the student.

        if attrs is list of strings, represents only those attributes included in the list.

        Args:
           attrs (list): the attibutes to represent.
        """
        if (type(attrs) == list and all(type(ele) == str for ele in attrs)):
            return {k: getattr(self, k) for k in attrs if hasattr(self, k)}
        return self.__dict__

    def reload_from_json(self, json):
        """Replace all attributes of the student.

        Args:
            json (dict): key pairs to replace attributes with.
        """
        for k, v in json.items():
            setattr(Self, k, v)
