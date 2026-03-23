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
        self.parents[value] = value
        self.ranks[value] = 0

    def find_representative(self, value):
        """
        Finds and returns the representative (root) of the set containing the given value.
        Applies path compression to flatten the structure and improve future operations.

        Args:
        value (int): The value for which the representative is to be found.

        Returns:
        int or None: The representative of the set, or None if the value is not found.
        """
        if value not in self.parents:
            return None
        if self.parents[value] != value:
            self.parents[value] = self.find_representative(self.parents[value])
        return self.parents[value]

    def merge_sets(self, value_one, value_two):
        """
        Merges the sets containing the two given values. Uses union by rank to
        attach the smaller tree to the root of the larger tree.

        Args:
        value_one (int): The first value.
        value_two (int): The second value.
        """
        r1 = self.find_representative(value_one)
        r2 = self.find_representative(value_two)

        if r1 is None or r2 is None or r1 == r2:
            return

        if self.ranks[r1] < self.ranks[r2]:
            self.parents[r1] = r2
        elif self.ranks[r1] > self.ranks[r2]:
            self.parents[r2] = r2
        else:
            self.parents[r2] = r1
            self.ranks[r1] +=1
