# 🧠 CC4 Reflection: Inventory Sorting – Reasoning Questions

Once the official solution is released, carefully read through the implementation provided. Then, thoughtfully answer the following reasoning questions.

Each question is designed to help you internalize not just **what** the code is doing, but **why** it was designed that way. Imagine you're in an engineering interview at a top company (e.g. Google, Meta, etc.). Your interviewer is not looking for a regurgitated solution — they want to know whether you **understand the trade-offs**, **maintain invariants**, and **meet constraints**.

This reflection is part of our SS26 focus on **reasoning-first learning** — moving beyond "code that works" to "code you can defend."

---

## ✅ Function Spec Recap

You were tasked with implementing:

```python
def sort_inventory(inventory: List[int], priority: List[int]) -> List[int]
```

- Sorts a list of inventory items so they appear in the order specified by `priority` (which contains exactly three distinct item types).
- Must run in **O(N) time** and use **O(1) auxiliary space**.
- Sorting must happen **in-place** by rearranging the input list.

---

## 📋 Reasoning Questions

### **R1. Invariants Under Pressure**
> "As you progress through the loop, what guarantees are you maintaining about the regions marked by `first_idx`, `second_idx`, and `third_idx`?  
> How do you know at any point that previously-processed elements will not violate the sorting order?"

---

### **R2. Defensive Swapping**
> "Why do we swap the current item with the `third_idx` position immediately when it's the third-priority item?  
> What could go wrong if we just incremented `second_idx` in that case, like we do for second-priority items?"

---

### **R3. Optimal Traversal Direction**
> "Some students implemented a simpler approach using three passes through the list to count and overwrite the values. Why doesn’t that meet the space or time constraints?  
> Why is the collapsing two-pointer approach (first_idx / third_idx) better for this case?"

---

### **R4. Priority Lookup Design**
> "Would it be acceptable to use `priority.index(current_item)` inside the loop to decide where an item belongs?  
> Analyze the time complexity of that approach, and explain why this solution avoids it."

---

### **R5. Space Constraint Discipline**
> "This problem explicitly requires O(1) auxiliary space. How does the final solution adhere to that constraint?  
> What are some common Python strategies (e.g., using `sorted()` or new lists) that would violate this constraint, even if they look clean?"

---

## 🧠 Final Thoughts

Understanding the **why behind the structure** of a solution is essential to becoming a strong problem solver and technical communicator. Use these reflections to level up from a code writer to an engineer who can defend and adapt algorithms under constraints.
