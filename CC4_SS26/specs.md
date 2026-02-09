

## 📦 Inventory Sorting System  

### **Problem Statement**  
You are managing an **inventory** in a warehouse, where items belong to exactly **three distinct categories**. The inventory is represented as an array of item IDs, and a **priority list** specifies the order in which items should be arranged for shipment.  

Your task is to **rearrange the inventory in-place** so that items appear in the same order as given in the priority list. You must accomplish this in **O(N) time** and **O(1) auxiliary space**.  

![alt text](CC4_img.png)
### **Function Signature**  
```python
def sort_inventory(inventory: List[int], priority: List[int]) -> List[int]:
```

### **Constraints**  
- The `inventory` **only contains** item IDs found in the `priority` list.  
- The order in `priority` **is fixed** and must be respected in the sorted `inventory`.  
- You **must not use extra memory** beyond a few variables (**O(1) space**).  
- Your solution **should run in O(N) time**.  

---

### **Example 1**  
#### **Input:**  
```python
inventory = [2, 0, 0, 3, 3, 0, 2, 2]
priority = [0, 2, 3]
```
#### **Output:**  
```python
[0, 0, 0, 2, 2, 2, 3, 3]
```
---

### **Example 2**  
#### **Input:**  
```python
inventory = [5, 4, 5, 6, 6, 4, 5, 6, 4]
priority = [4, 5, 6]
```
#### **Output:**  
```python
[4, 4, 4, 5, 5, 5, 6, 6, 6]
```
---

### **Example 3**  
#### **Input:**  
```python
inventory = [3, 1, 2, 3, 2, 1, 1, 3, 2]
priority = [1, 2, 3]
```
#### **Output:**  
```python
[1, 1, 1, 2, 2, 2, 3, 3, 3]
```


[🎵 Coding Music Playlist](https://youtu.be/xAR6N9N8e6U?si=lpoAhtiYOdgH7wpm)
# 📝 Required README.txt Format for CC4

Your `README.txt` must include the points you earned for each test in `tests.py`. This helps us understand your testing process and self-assess how well your implementation performs. Use the format shown below.

---

## ✅ Example Format
```
Total points for CC4: XX Points

Detailed points for each test:
1) test_case_1: 15
2) test_case_2: 15
3) test_case_3: 15
4) test_case_4: 15
5) test_case_5: 10
6) test_case_6: 15
7) test_case_7: 15
```

> ✅ Passed test = full points  
> ❌ Failed test = 0 points  
> 🔁 Partial logic passed = give yourself partial credit **only if instructed by staff**

---

## 🧪 Test Case Breakdown

| Test Name         | Description                                | Points |
|-------------------|---------------------------------------------|--------|
| `test_case_1`     | Basic inventory with mixed item ordering    | 15     |
| `test_case_2`     | Already sorted input                        | 15     |
| `test_case_3`     | Inventory with only one item type           | 15     |
| `test_case_4`     | Inventory with only two item types          | 15     |
| `test_case_5`     | Edge case: empty input                      | 10     |
| `test_case_6`     | Missing one of the priority items           | 15     |
| `test_case_7`     | Large input stress test                     | 15     |
| **Total**         |                                             | **100** |

---

## 🧠 Why This Matters

We are focusing on **reasoning-first coding** this semester. The `README.txt` encourages you to:
- Think beyond just "passing tests"
- Track how your code handles each case
- Build self-debugging and test interpretation skills

Just like in real-world engineering teams, **self-reporting** is part of developing engineering maturity.

— **Team 331**
