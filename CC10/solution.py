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
        curr = self.root
        for ch in word:
            if ch not in curr:
                curr [ch] = {}
            curr = curr[ch]

        curr[self.end_symbol] = word
        return

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
    t = Trie()
    for word in small_strings:
        t.insert(word)

    # edge
    found = {word: False for word in small_strings}
    if "" in found:
        found[""] = True

    for i in range(len(big_string)):
        curr = t.root
        j = i

        while j < len(big_string):
            ch = big_string[j]
            if ch not in curr:
                break
            curr = curr[ch]

            if t.end_symbol in curr:
                found_word = curr[t.end_symbol]
                found[found_word] = True
            j+=1

    return [found[word] for word in small_strings]
    return isin


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
