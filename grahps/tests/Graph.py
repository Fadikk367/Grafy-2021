import unittest


class Node:
    id: int
    is_visited: bool

    def __init__(self, node_id: int = 0, visited: bool = False):
        self.id = node_id
        self.is_visited = visited

    def __eq__(self, other):
        # isinstance(other, self.__class__)
        return self.id == other.id

    def __hash__(self) -> int:
        return id(self)

    def __str__(self):
        return f"({self.id})"


class Edge:
    def __init__(self, first_node: Node, second_node: Node, is_visited: bool = False, weight: int = 0, is_weighted: bool = False):
        self.nodes = (first_node, second_node)
        self.weight = weight
        self.is_visited = is_visited
        self.is_weighted = is_weighted

    def __str__(self):
        return f"{self.nodes[0]}--{self.nodes[1]}"

    def __eq__(self, other):
        # TODO
        return (
            (self.nodes[0] == other.nodes[0] and self.nodes[1] == other.nodes[1]) or
            (self.nodes[1] == other.nodes[0] and self.nodes[0] == other.nodes[1])
        )
        # return self.nodes[0] == other.nodes[0] and self.nodes[1] == other.nodes[1]

    def has_common_node_with(self, other) -> bool:
        return (
            self.nodes[0] == other.nodes[0] or
            self.nodes[0] == other.nodes[1] or
            self.nodes[1] == other.nodes[0] or
            self.nodes[1] == other.nodes[1]
        )


class TestStringMethods(unittest.TestCase):
    def setUp(self) -> None:
        self.A = Node(0)
        self.B = Node(1)
        self.C = Node(2)
        self.D = Node(3)
        self.E = Node(4)

    def test_has_common_node_when_it_exists_on_start(self):
        a = Edge(self.A, self.B)
        b = Edge(self.B, self.C)

        self.assertEqual(a.has_common_node_with(b), True)

    def test_has_common_node_when_it_exists_on_end(self):
        a = Edge(self.A, self.B)
        b = Edge(self.C, self.A)

        self.assertEqual(a.has_common_node_with(b), True)

    def test_has_common_node_when_it_does_not_exist(self):
        a = Edge(self.A, self.B)
        b = Edge(self.C, self.D)

        self.assertEqual(a.has_common_node_with(b), False)

    def test_has_common_node_when_compared_to_the_same_edge(self):
        a = Edge(self.A, self.B)
        b = Edge(self.A, self.B)

        self.assertEqual(a.has_common_node_with(b), True)

    def test_edges_should_be_equal_for_identical_edges(self):
        a = Edge(self.A, self.B)
        b = Edge(self.A, self.B)

        self.assertEqual(a == b, True)

    def test_edges_should_be_equal_for_reversed_edges(self):
        a = Edge(self.A, self.B)
        b = Edge(self.B, self.A)

        self.assertEqual(a == b, True)

    def test_edges_should_not_be_equal_for_one_common_node_on_start(self):
        a = Edge(self.A, self.B)
        b = Edge(self.A, self.C)

        self.assertEqual(a != b, True)

    def test_edges_should_not_be_equal_for_one_common_node_on_end(self):
        a = Edge(self.A, self.B)
        b = Edge(self.C, self.B)

        self.assertEqual(a != b, True)

    def test_isupper(self):
        self.assertTrue('FOO'.isupper())
        self.assertFalse('Foo'.isupper())

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)


if __name__ == '__main__':
    unittest.main()
