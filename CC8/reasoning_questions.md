# Reasoning Questions: Compute Formula Tree

Use these for discussion or short-answer reflection after implementing the challenge.

---

1. **Traversal choice**  
   Why is a post-order (or bottom-up) evaluation natural for this formula tree? What would go wrong if you tried to evaluate the root before its children?

2. **Leaf vs internal node**  
   How do you decide whether a node is a leaf or an internal operator node? Why is it safe to assume that every internal node has exactly two non-None children?

3. **Time complexity**  
   Argue that your solution runs in O(n) time, where n is the number of nodes. How many times is each node visited?

4. **Space complexity**  
   Explain why the auxiliary space is O(h) where h is the height of the tree. What dominates: recursion stack, or extra data structures?

5. **Division truncation**  
   In Python, how does integer division `//` behave for negative numbers? How would you implement “truncate toward zero” so that both 7/2 and (-7)/2 behave as specified?

6. **Extension**  
   If the tree could also contain a unary operator (e.g., negation) at an internal node with only one child, how would you change your recursion and your node-type checks?
