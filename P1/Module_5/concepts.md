## 1. The Problem with Cardinality

Data engineering logic handles a high variety of inputs[cite: 129]. Writing separate tests for "MM/DD/YYYY" and "YYYY.MM.DD" is inefficient and violates the DRY (Don't Repeat Yourself) principle.

---

## 2. The Solution: `pytest.mark.parametrize`
This decorator allows you to define a list of inputs and expected outputs. Pytest will run the **same test function** multiple times—once for each set of arguments.

**Syntax:**
```python
@pytest.mark.parametrize("input_val, expected", [
    ("3", 3),
    ("5", 5),
])
def test_conversion(input_val, expected):
    assert int(input_val) == expected
```

---