from abc import ABC, ABCMeta, abstractmethod


class Node(ABC):
    _name = "Error"
    _calculated = False
    _value = None

    @property
    def value(self):
        return self._value

    @property
    def name(self):
        return self._name

    def __repr__(self) -> str:
        return self.name

    @property
    def is_calculated(self):
        return self._calculated

    @abstractmethod
    def dependencies(self) -> tuple[ABCMeta]:
        ...

    @abstractmethod
    def calculate(self, *args):
        ...


class Graph:

    def __init__(self):
        self.nodes = []

    def __repr__(self) -> str:
        strings = []
        for node in self.nodes:
            if node.is_calculated:
                strings.append(str(node))
            else:
                strings.append("*" + str(node))
        return f"Graph({', '.join(strings)})"

    def contains_class(self, cls: ABCMeta) -> bool:
        return any(isinstance(node, cls) for node in self.nodes)

    def add_node(self, node: Node):
        if self.contains_class(type(node)):
            return
        for dep in node.dependencies():
            if self.contains_class(dep):
                continue
            new_node = dep()
            self.add_node(new_node)
        self.nodes.append(node)

    def __getitem__(self, cls: ABCMeta):
        for node in self.nodes:
            if isinstance(node, cls):
                return node
        raise ValueError

    def calculate_node(self, cls: ABCMeta, verbose=False):
        node = self[cls]
        if node.is_calculated:
            return
        for dep in node.dependencies():
            self.calculate_node(dep)
        args = tuple(self[dep].value for dep in node.dependencies())
        print(f"Calculating {node.name}")
        node.calculate(*args)

    def calculate_all(self, verbose=False):
        for node in self.nodes:
            self.calculate_node(type(node), verbose=verbose)

