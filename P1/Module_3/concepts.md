# Module 3: Stateless Logic Verification

## 1. Pure Functions

A "Pure Function" has two properties:

1.  Its output depends *only* on its input arguments.

2.  It has no "side effects" (no writing to S3, no DB inserts, no global variables).

**Why this matters :**

If a pipeline fails, you need to know if it's because the *logic* is wrong (Unit Test) or because the *server* is down (Integration Test). By isolating transformation logic into pure functions, you can prove the math works before you ever try to load the data.

---

## 2. Python 3.12 Typing

We use strict typing (Type Hints) to catch errors early.

* `dict[str, Any]`: A dictionary with string keys and values of any type.

* `list[int]`: A list of integers.

---

## 3. Recursion in Data

We often deal with nested JSON (e.g., from NoSQL databases like MongoDB or APIs). flattening these structures is a classic algorithmic task.

---