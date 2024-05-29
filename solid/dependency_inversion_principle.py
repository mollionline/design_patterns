# DIP
from abc import abstractmethod
from enum import Enum


# Dependency Inversion Principle
# - High-Level modules should not depend upon low-level ones; use abstractions


class Relationship(Enum):
    PARENT = 0
    CHILD = 1
    SIBLING = 2


class Person:
    def __init__(self, name):
        self.name = name


class RelationshipBrowser:
    @abstractmethod
    def find_all_children_of(self, name):
        pass


class Relationships(RelationshipBrowser):  # low-level
    def __init__(self):
        self.relations = []

    def add_parent_and_child(self, parent, child):
        self.relations.append(
            (parent, Relationship.PARENT, child)
        )
        self.relations.append(
            (child, Relationship.CHILD, parent)
        )

    def find_all_children_of(self, name):
        for r in self.relations:
            if r[0].name == name and r[1] == Relationship.PARENT:
                yield r[2].name


class Research:
    # def __init__(self, relationships):
    #     relations = relationships.relations
    #     for r in relations:
    #         if r[0].name == 'John' and r[1] == Relationship.PARENT:
    #             print(f'John has a child called {r[2].name}.')

    def __init__(self, browser):
        for p in browser.find_all_children_of('John'):
            print(f'John has a child called {p}')


parent = Person('John')
child1 = Person('Chris')
child2 = Person('Matt')

relationships = Relationships()
relationships.add_parent_and_child(parent, child1)
relationships.add_parent_and_child(parent, child2)

Research(relationships)

# Single Responsibility Principle
# - A class should only have one reason to change
# - Separation of concerns - different classes handling different, independent tasks/problems

# Open-Closed Principle
# - Classes should be open for extension but closed for modification

# Liskov Substitution Principle
# - You should be able to substitute a base type for a subtype

# Interface Segregation Principle
# - Don't put too much into an interface; split into separate interfaces
# - YAGNI - You Ain't Going to Need It

# Dependency Inversion Principle
# - High-Level modules should not depend upon low-level ones; use abstractions
