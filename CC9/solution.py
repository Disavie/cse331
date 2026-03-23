class DisjointSet:
    """
    A class that implements the Disjoint Set (Union-Find) data structure.

    The data structure maintains a collection of disjoint sets, allowing efficient
    union and find operations.

    Attributes:
    parents (dict): A dictionary to store the parent of each element.
    ranks (dict): A dictionary to store the rank (or depth) of each element's tree.
    """

    def __init__(self):
        """
        Initializes an empty Disjoint Set with no elements.
        """
        self.parents = {}
        self.ranks = {}

    def add_set(self, value):
        """
        Adds a new set containing the given value. The value becomes its own parent initially.

        Args:
        value (int): The value to add to the disjoint set.
        """
        pass

    def find_representative(self, value):
        """
        Finds and returns the representative (root) of the set containing the given value.
        Applies path compression to flatten the structure and improve future operations.

        Args:
        value (int): The value for which the representative is to be found.

        Returns:
        int or None: The representative of the set, or None if the value is not found.
        """
        pass

    def merge_sets(self, value_one, value_two):
        """
        Merges the sets containing the two given values. Uses union by rank to
        attach the smaller tree to the root of the larger tree.

        Args:
        value_one (int): The first value.
        value_two (int): The second value.
        """
        pass
