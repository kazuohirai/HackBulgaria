import unittest
from graph import Graph


class TestGraph(unittest.TestCase):
    def setUp(self):
        self.testgraph = Graph("My Graph")

    def test_init(self):
        self.assertEqual(self.testgraph.name, "My Graph")

    def test_add_edge_when_possible(self):
        result = self.testgraph.add_edge("Node1", "Node2")
        self.assertEqual(result, {"Node1": ["Node2"], "Node2": []})

    def test_add_edge_when_impossible(self):
        self.testgraph.add_edge("Node1", "Node2")
        result = self.testgraph.add_edge("Node1", "Node2")
        self.assertEqual(result, "Edge already exists.")

    def test_neighbours_of_correct_node(self):
        self.testgraph.add_edge("Node1", "Node2")
        self.testgraph.add_edge("Node1", "Node3")
        result = self.testgraph.get_neighbours_for("Node1")
        self.assertEqual(result, ["Node2", "Node3"])

    def test_neighbours_of_incorrect_node(self):
        self.testgraph.add_edge("Node1", "Node2")
        result = self.testgraph.get_neighbours_for("Node3")
        self.assertEqual(result, "Node not in neighbours list.")

    def test_path_between_unexisting_nodes(self):
        self.testgraph.add_edge("Node1", "Node2")
        self.assertFalse(self.testgraph.path_between("Node1", "Node3"))

    def test_path_between_existing_nodes(self):
        self.testgraph.add_edge("2", "1")
        self.testgraph.add_edge("2", "4")
        self.testgraph.add_edge("2", "5")
        self.testgraph.add_edge("1", "3")
        self.testgraph.add_edge("5", "6")
        self.assertTrue(self.testgraph.path_between("2", "6"))


if __name__ == "__main__":
    unittest.main()
