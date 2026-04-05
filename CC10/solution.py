class Trie:
    """
    A simple Trie (Prefix Tree) data structure used to store strings
    for efficient prefix-based search.
    """

    def __init__(self):
        # Root node of the trie is an empty dictionary
        self.root = {}

        # Special symbol to mark the end of a word
        self.end_symbol = "*"

    def insert(self, word):
        """
        Inserts a word into the trie.

        Args:
            word (str): The word to insert.
        """
        # TODO: Implement this method
        pass


def multi_string_search(big_string, small_strings):
    """
    Determines which strings from small_strings are present in big_string.

    Args:
        big_string (str): The larger string to search within.
        small_strings (List[str]): A list of smaller strings to search for.

    Returns:
        List[bool]: A list of boolean values indicating whether each small string
                    is found in the big string.
    """
    # TODO: Build the trie and search for the small strings
    pass


def search_from_index(string, start_index, trie, found_strings):
    """
    Traverses the big string from the given start index, using the trie
    to find matching substrings that correspond to the small strings.

    Args:
        string (str): The big string.
        start_index (int): The index to start searching from.
        trie (Trie): The trie built from the small strings.
        found_strings (dict): A dictionary to record found strings.
    """
    # TODO: Traverse the trie from the start index and record matches
    pass
