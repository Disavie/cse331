"""
Project 5
CSE 331 SS26
starter.py
"""

from collections import deque
import math
from queue import SimpleQueue
from typing import TypeVar, Generator, List, Tuple, Optional


# for more information on typehinting, check out https://docs.python.org/3/library/typing.html
T = TypeVar("T")  # represents generic type
# represents a Node object (forward-declare to use in Node __init__)
Node = TypeVar("Node")


class Node:
    """
    Implementation of an BST and AVL tree node.

    DO NOT MODIFY.
    """
    # preallocate storage: see https://stackoverflow.com/questions/472000/usage-of-slots
    __slots__ = ["value", "parent", "left", "right", "height", "data"]

    def __init__(self, value: T, parent: Node = None,
                 left: Node = None, right: Node = None, data: str = None) -> None:
        """
        Construct an AVL tree node.

        :param value: value held by the node object
        :param parent: ref to parent node of which this node is a child
        :param left: ref to left child node of this node
        :param right: ref to right child node of this node
        :param data: Optional parameter to store data in Node, used in the application problem.
        """
        self.value = value
        self.parent, self.left, self.right = parent, left, right
        self.height = 0
        self.data = data

    def __repr__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return f"<{str(self.value)}>"

    def __str__(self) -> str:
        """
        Represent the AVL tree node as a string.

        :return: string representation of the node.
        """
        return repr(self)


####################################################################################################

class AVLTree:
    """
    Implementation of an AVL tree.

    Modify only below indicated line.
    """

    __slots__ = ["origin", "size"]

    def __init__(self) -> None:
        """
        Construct an empty AVL tree.
        """
        self.origin = None
        self.size = 0

    def __repr__(self) -> str:
        """
        Represent the AVL tree as a string.

        :return: string representation of the AVL tree
        """
        if self.origin is None:
            return "Empty AVL Tree"

        return super(AVLTree, self).__repr__()

    def __str__(self) -> str:
        """
        Represent the AVLTree as a string.

        :return: string representation of the BSTree
        """
        return repr(self)

    ########################################
    # Implement functions below this line. #
    ########################################

    def height(self, root: Node) -> int:
        """
        Return the height of the subtree rooted at `root`, or -1 if `root` is None.

        :param root: root node of subtree
        :return: height of subtree
        """
        if root is None:
            return -1
        return root.height

    def left_rotate(self, root: Node) -> Optional[Node]:
        """
        Perform a left rotation on the subtree rooted at `root`. Return new subtree root.

        :param root: root node of unbalanced subtree to be rotated.
        :return: new root node of subtree following rotation.
        """
        if root is None:
            return None
    
        if root.right is None:
            return root

        y = root.right
        T3 = y.left

        y.left = root
        root.right = T3

        if T3 is not None:
            T3.parent = root

        y.parent = root.parent
        if y.parent is None:
            self.origin = y
        else:
            if root.parent.left == root:
                root.parent.left = y
            else:
                y.parent.right = y

        root.parent = y


        root.height = 1 + max(self.height(root.right),self.height(root.left))
        y.height = 1 + max(self.height(y.right),self.height(y.left))
        return y

    def right_rotate(self, root: Node) -> Optional[Node]:

        """
        Perform a right rotation on the subtree rooted at `root`. Return new subtree root.

        :param root: root node of unbalanced subtree to be rotated.
        :return: new root node of subtree
        """
        if root is None:
            return None
    
        if root.left is None:
            return root

        y = root.left
        T3 = y.right

        y.right = root
        root.left = T3

        if T3 is not None:
            T3.parent = root

        y.parent = root.parent
        if y.parent is None:
            self.origin = y
        else:
            if root.parent.left == root:
                root.parent.left = y
            else:
                y.parent.right = y
        root.parent = y

        root.height = 1 + max(self.height(root.left),self.height(root.right))
        y.height = 1 + max(self.height(y.left),self.height(y.right))

        return y

        

    def balance_factor(self, root: Node) -> int:

        """
        Compute the balance factor of the subtree rooted at `root`.

        :param root: root node of subtree
        :return: balance factor of subtree
        """
        if root is None:
            return 0
        return self.height(root.left)-self.height(root.right)


    def rebalance(self, root: Node) -> Optional[Node]:
        """
        Rebalance the subtree rooted at `root`. Return the new subtree root.

        :param root: root node of subtree to be rebalanced
        :return: new root node of subtree
        """

        b = self.balance_factor(root)


        if b > 1: # left heavy
            if self.balance_factor(root.left) < 0:
                root.left = self.left_rotate(root.left)

            return self.right_rotate(root)

            #
        elif b < -1: # right heavy
            if self.balance_factor(root.right) > 0:
                root.right = self.right_rotate(root.right)

            return self.left_rotate(root)

        return root

    def insert(self, root: Node, val: T, data: str = None) -> Optional[Node]:
        """
        Insert `val` into the subtree rooted at `root`. Return the new subtree root.

        :param root: root node of subtree
        :param val: value to be inserted into subtree
        :param data: Optional parameter to store data in Node, used in the application problem.
        :return: new root node of subtree
        """

        if root is None:
            node = Node(val,data=data)
            self.size+=1
            if self.origin is None:
                self.origin = node
            return node

        if val < root.value:
            root.left = self.insert(root.left, val, data)
            root.left.parent = root
        elif val > root.value:
            root.right = self.insert(root.right,val,data)
            root.right.parent = root
        else:
            return root

        root.height = 1 + max(self.height(root.left), self.height((root.right)))
        new_root = self.rebalance(root)

        if new_root.parent is None:
            self.origin = new_root

        return new_root



    def remove(self, root: Node, val: T) -> Node:
        """
        Remove a value from the BSTree starting at root.

        :param root: root of subtree in BSTree
        :param val: the value to remove
        :return: the new root of the subtree
        """
        if root is None:
            return None

        if val < root.value:
            root.left = self.remove(root.left,val)
            if root.left:
                root.left.parent = root
        elif val > root.value:
            root.right = self.remove(root.right,val)
            if root.right:
                root.right.parent = root
        else:
            if root.left is None and root.right is None:
                self.size-=1
                if root == self.origin:
                    self.origin = None
                return None

            elif root.left is None:
                temp = root.right
                if temp:
                    temp.parent = root.parent
                self.size-=1
                return temp

            elif root.right is None:
                temp = root.left
                if temp:
                    temp.parent = root.parent
                self.size-=1
                return temp

            before = self.max(root.left)
            root.value = before.value
            root.data = before.data
            root.left = self.remove(root.left,before.value)
            if root.left:
                root.left.parent = root
        root.height = 1 + max(self.height(root.left), self.height(root.right))

        n = self.rebalance(root)

        if n.parent is None:
            self.origin = n

        return n

    def min(self, root: Node) -> Optional[Node]:
        """
        Return the node with the minimum value in the subtree rooted at `root`.

        :param root: root node of subtree
        :return: node with minimum value in subtree
        """
        if root is None:
            return None
        while root.left is not None:
            root = root.left
        return root

    def max(self, root: Node) -> Optional[Node]:
        """
        Return the node with the maximum value in the subtree rooted at `root`.

        :param root: root node of subtree
        :return: node with maximum value in subtree
        """
        if root is None:
            return None
        while root.right is not None:
            root = root.right
        return root

    def search(self, root: Node, val: T) -> Optional[Node]:
        """
        Search for `val` in the subtree rooted at `root`. Return the node containing `val` if found,
        or its potential parent otherwise.

        :param root: root node of subtree
        :param val: value to be searched for
        """
        if root is None:
            return None

        if val == root.value:
            return root

        elif val < root.value:
            if root.left is None:
                return root
            return self.search(root.left, val)

        else:
            if root.right is None:
                return root
            return self.search(root.right, val)


    def inorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Traverse the subtree rooted at `root` in-order, and yield each node.

        :param root: root node of subtree
        :return: generator of nodes in in-order traversal
        """
        if root is None:
            return
        yield from self.inorder(root.left)
        yield(root)
        yield from self.inorder(root.right)

    def __iter__(self) -> Generator[Node, None, None]:
        """
        Call `inorder` on the root node of the tree.

        :return: generator of nodes in in-order traversal
        """
        yield from self.inorder(self.origin)

    def preorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Traverse the subtree rooted at `root` in pre-order, and yield each node.

        :param root: root node of subtree
        :return: generator of nodes in pre-order traversal
        """
        if root is None:
            return


        yield(root)
        yield from self.preorder(root.left)
        yield from self.preorder(root.right)

    def postorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Traverse the subtree rooted at `root` in post-order, and yield each node.

        :param root: root node of subtree
        :return: generator of nodes in post-order traversal
        """
        if root is None:
            return
        yield from self.postorder(root.left)
        yield from self.postorder(root.right)
        yield(root)


    def levelorder(self, root: Node) -> Generator[Node, None, None]:
        """
        Traverse the subtree rooted at `root` in level-order, and yield each node.

        :param root: root node of subtree
        :return: generator of nodes in level-order traversal
        """
        if root is None:
            return
        q = deque([root])
        while q:
            node = q.popleft()
            yield node

            if node.left:
                q.append(node.left)
            if node.right:
                q.append(node.right)
    
# Classifier
class KNNClassifier:

    ########################################################
    # DO NOT MODIFY BELOW #
    ########################################################

    def __init__(self, k: int = 1):
        """
        KNN Classifier class that uses the k nearest neighbors algorithm to classify a data point

        :param k: Number of close neighbors to consider for classification
        :return: None
        """
        self.k = k
        self.tree = AVLTree()
       
    def floats_equal(self, f1:float, f2: float) -> bool:
        """
        Compares two floats using threshold to check if numbers are equal due to floating point error

        :param f1: First float
        :param f2: Second float
        :return: True if they are the same, false otherwise
        """
        return abs(f1 - f2) <= 1e-10

    def get_list_item(self, items: List[Tuple[float, str]], index: int) -> Tuple[float, str]:
        """
        Get item in list at index
        If index out of bounds return infinite so it can be ignored on closest comparison

        :param items: List to extract item from
        :param index: Index to extract
        :return: Tuple with values at index if inside list bounds or (infinity, None)

        This is an optional helper function used in get_k_neighbors( ) method. It is correct and feel free to use it.
        """
        if 0 <= index < len(items):
            return items[index]
        return (float('inf'), None)

    ########################################
    # MODIFY BELOW #
    ######################################## 
    def train(self, data: List[Tuple[float, str]]) -> None:
        """
        Adds training data to AVL tree

        :param data: List of tuples: (value, classification)
        :return: None
        """
        if len(data) > 0:
            for e1, e2 in data:
                self.tree.origin = self.tree.insert(self.tree.origin,e1,e2)


    def get_k_neighbors(self, target_value: float) -> List[Tuple[float, str]]:

        """
        Finds the k closest neighbors to the target_value using in-order traversal
        of the AVL tree and a sliding window approach.

        :param target_value: The value to find neighbors for
        :return: A list of (value, label) tuples representing the k closest neighbors
        """
        # root of our tree
        if self.tree.origin is None or self.tree.origin.value is None:
            return []

        root = self.tree.origin
        k = self.k

        generator = root.inorder(avl.origin)
        self.assertIsInstance(generator, types.GeneratorType)
        expected = list(range(10))
        for num in expected:
            node = next(generator)
            nodes.append(node)

        with self.assertRaises(StopIteration):
            next(generator)
        print(nodes)



    def calculate_best_fit(self, neighbors: List[Tuple[float, str]], target_value: float) -> str:
        """
        Calculates the predicted classification label using inverse distance weighting.
        Each neighbor contributes a weight of 1 / distance to its label.
        The label with the highest total weight is selected.

        :param neighbors: List of (value, label) tuples representing k nearest neighbors
        :param target_value: The value to be classified
        :return: The predicted label
        """
        pass

    def classify(self, value: float) -> str:
        """
        Classifies value with k-closest neighbor method

        :param value: value to be classified.
        """
        pass


########################################################
# DO NOT MODIFY BELOW #
########################################################

def is_avl_tree(node):
    def is_avl_tree_inner(cur, high, low):
        # if node is None at any time, it is balanced and therefore True
        if cur is None:
            return True, -1
        if cur.value > high or cur.value < low:
            return False, -1
        is_avl_left, left_height = is_avl_tree_inner(cur.left, cur.value, low)
        is_avl_right, right_height = is_avl_tree_inner(cur.right, high, cur.value)
        cur_height = max(left_height, right_height) + 1
        return is_avl_left and is_avl_right and abs(left_height - right_height) < 2, cur_height

    # absolute difference between right and left subtree should be no greater than 1
    return is_avl_tree_inner(node, float('inf'), -float('inf'))[0]



_SVG_XML_TEMPLATE = """
<svg width="{width}" height="{height}" xmlns="http://www.w3.org/2000/svg">
<style>
    .value {{
        font: 300 16px monospace;
        text-align: center;
        dominant-baseline: middle;
        text-anchor: middle;
    }}
    .dict {{
        font: 300 16px monospace;
        dominant-baseline: middle;
    }}
    .node {{
        fill: lightgray;
        stroke-width: 1;
    }}
</style>
<g stroke="#000000">
{body}
</g>
</svg>
"""

_NNC_DICT_BOX_TEXT_TEMPLATE = """<text class="dict" y="{y}" xml:space="preserve">
    <tspan x="{label_x}" dy="1.2em">{label}</tspan>
    <tspan x="{bracket_x}" dy="1.2em">{{</tspan>
    {values}
    <tspan x="{bracket_x}" dy="1.2em">}}</tspan>
</text>
"""


def pretty_print_binary_tree(root: Node, curr_index: int, include_index: bool = False,
                             delimiter: str = "-", ) -> \
        Tuple[List[str], int, int, int]:
    """
    Taken from: https://github.com/joowani/binarytree

    Recursively walk down the binary tree and build a pretty-print string.
    In each recursive call, a "box" of characters visually representing the
    current (sub)tree is constructed line by line. Each line is padded with
    whitespaces to ensure all lines in the box have the same length. Then the
    box, its width, and start-end positions of its root node value repr string
    (required for drawing branches) are sent up to the parent call. The parent
    call then combines its left and right sub-boxes to build a larger box etc.
    :param root: Root node of the binary tree.
    :type root: binarytree.Node | None
    :param curr_index: Level-order_ index of the current node (root node is 0).
    :type curr_index: int
    :param include_index: If set to True, include the level-order_ node indexes using
        the following format: ``{index}{delimiter}{value}`` (default: False).
    :type include_index: bool
    :param delimiter: Delimiter character between the node index and the node
        value (default: '-').
    :type delimiter:
    :return: Box of characters visually representing the current subtree, width
        of the box, and start-end positions of the repr string of the new root
        node value.
    :rtype: ([str], int, int, int)
    .. _Level-order:
        https://en.wikipedia.org/wiki/Tree_traversal#Breadth-first_search
    """
    if root is None:
        return [], 0, 0, 0

    line1 = []
    line2 = []
    if include_index:
        node_repr = "{}{}{}".format(curr_index, delimiter, root.value)
    else:
        node_repr = f'{root.value},h={root.height},' \
                    f'⬆{str(root.parent.value) if root.parent else "None"}'

    new_root_width = gap_size = len(node_repr)

    # Get the left and right sub-boxes, their widths, and root repr positions
    l_box, l_box_width, l_root_start, l_root_end = pretty_print_binary_tree(
        root.left, 2 * curr_index + 1, include_index, delimiter
    )
    r_box, r_box_width, r_root_start, r_root_end = pretty_print_binary_tree(
        root.right, 2 * curr_index + 2, include_index, delimiter
    )

    # Draw the branch connecting the current root node to the left sub-box
    # Pad the line with whitespaces where necessary
    if l_box_width > 0:
        l_root = (l_root_start + l_root_end) // 2 + 1
        line1.append(" " * (l_root + 1))
        line1.append("_" * (l_box_width - l_root))
        line2.append(" " * l_root + "/")
        line2.append(" " * (l_box_width - l_root))
        new_root_start = l_box_width + 1
        gap_size += 1
    else:
        new_root_start = 0

    # Draw the representation of the current root node
    line1.append(node_repr)
    line2.append(" " * new_root_width)

    # Draw the branch connecting the current root node to the right sub-box
    # Pad the line with whitespaces where necessary
    if r_box_width > 0:
        r_root = (r_root_start + r_root_end) // 2
        line1.append("_" * r_root)
        line1.append(" " * (r_box_width - r_root + 1))
        line2.append(" " * r_root + "\\")
        line2.append(" " * (r_box_width - r_root))
        gap_size += 1
    new_root_end = new_root_start + new_root_width - 1

    # Combine the left and right sub-boxes with the branches drawn above
    gap = " " * gap_size
    new_box = ["".join(line1), "".join(line2)]
    for i in range(max(len(l_box), len(r_box))):
        l_line = l_box[i] if i < len(l_box) else " " * l_box_width
        r_line = r_box[i] if i < len(r_box) else " " * r_box_width
        new_box.append(l_line + gap + r_line)

    # Return the new box, its width and its root repr positions
    return new_box, len(new_box[0]), new_root_start, new_root_end


def svg(root: Node, node_radius: int = 16, nnc_mode=False) -> str:
    """
    Taken from: https://github.com/joowani/binarytree

    Generate SVG XML.
    :param root: Generate SVG for tree rooted at root
    :param node_radius: Node radius in pixels (default: 16).
    :type node_radius: int
    :return: Raw SVG XML.
    :rtype: str
    """
    tree_height = root.height
    scale = node_radius * 3
    xml = deque()
    nodes_for_nnc_visualization = []

    def scale_x(x: int, y: int) -> float:
        diff = tree_height - y
        x = 2 ** (diff + 1) * x + 2 ** diff - 1
        return 1 + node_radius + scale * x / 2

    def scale_y(y: int) -> float:
        return scale * (1 + y)

    def add_edge(parent_x: int, parent_y: int, node_x: int, node_y: int) -> None:
        xml.appendleft(
            '<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}"/>'.format(
                x1=scale_x(parent_x, parent_y),
                y1=scale_y(parent_y),
                x2=scale_x(node_x, node_y),
                y2=scale_y(node_y),
            )
        )

    def add_node(node_x: int, node_y: int, node: Node) -> None:
        x, y = scale_x(node_x, node_y), scale_y(node_y)
        xml.append(f'<circle class="node" cx="{x}" cy="{y}" r="{node_radius}"/>')

        if nnc_mode:
            nodes_for_nnc_visualization.append(node.value)
            xml.append(f'<text class="value" x="{x}" y="{y + 5}">key={node.value.key}</text>')
        else:
            xml.append(f'<text class="value" x="{x}" y="{y + 5}">{node.value}</text>')

    current_nodes = [root.left, root.right]
    has_more_nodes = True
    y = 1

    add_node(0, 0, root)

    while has_more_nodes:

        has_more_nodes = False
        next_nodes: List[Node] = []

        for x, node in enumerate(current_nodes):
            if node is None:
                next_nodes.append(None)
                next_nodes.append(None)
            else:
                if node.left is not None or node.right is not None:
                    has_more_nodes = True

                add_edge(x // 2, y - 1, x, y)
                add_node(x, y, node)

                next_nodes.append(node.left)
                next_nodes.append(node.right)

        current_nodes = next_nodes
        y += 1

    svg_width = scale * (2 ** tree_height)
    svg_height = scale * (2 + tree_height)
    if nnc_mode:

        line_height = 20
        box_spacing = 10
        box_margin = 5
        character_width = 10

        max_key_count = max(map(lambda obj: len(obj.dictionary), nodes_for_nnc_visualization))
        box_height = (max_key_count + 3) * line_height + box_margin

        def max_length_item_of_node_dict(node):
            # Check if dict is empty so max doesn't throw exception
            if len(node.dictionary) > 0:
                item_lengths = map(lambda pair: len(str(pair)), node.dictionary.items())
                return max(item_lengths)
            return 0

        max_value_length = max(map(max_length_item_of_node_dict, nodes_for_nnc_visualization))
        box_width = max(max_value_length * character_width, 110)

        boxes_per_row = svg_width // box_width
        rows_needed = math.ceil(len(nodes_for_nnc_visualization) / boxes_per_row)

        nodes_for_nnc_visualization.sort(key=lambda node: node.key)
        for index, node in enumerate(nodes_for_nnc_visualization):
            curr_row = index // boxes_per_row
            curr_column = index % boxes_per_row

            box_x = curr_column * (box_width + box_spacing)
            box_y = curr_row * (box_height + box_spacing) + svg_height
            box = f'<rect x="{box_x}" y="{box_y}" width="{box_width}" ' \
                  f'height="{box_height}" fill="white" />'
            xml.append(box)

            value_template = '<tspan x="{value_x}" dy="1.2em">{key}: {value}</tspan>'
            text_x = box_x + 10

            def item_pair_to_svg(pair):
                return value_template.format(key=pair[0], value=pair[1], value_x=text_x + 10)

            values = map(item_pair_to_svg, node.dictionary.items())
            text = _NNC_DICT_BOX_TEXT_TEMPLATE.format(
                y=box_y,
                label=f"key = {node.key}",
                label_x=text_x,
                bracket_x=text_x,
                values='\n'.join(values)
            )
            xml.append(text)

        svg_width = boxes_per_row * (box_width + box_spacing * 2)
        svg_height += rows_needed * (box_height + box_spacing * 2)

    return _SVG_XML_TEMPLATE.format(
        width=svg_width,
        height=svg_height,
        body="\n".join(xml),
    )
