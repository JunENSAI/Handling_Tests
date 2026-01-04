## Exercises

Create a file `tests/test_module_3.py` and implement tests for the following scenarios:

### 1. The Happy Path

Input: A simple nested dictionary.

```Python
input_data = {"user": {"name": "Alice", "address": {"city": "Paris"}}}
```

```text
Expected Output: {"user_name": "Alice", "user_address_city": "Paris"}
```

### 2. The Empty Case

Input: `{}`

Expected: `{} (Ensure it doesn't crash).`

### 3. The Ambiguity (Edge Case)

Input: A dictionary containing a List.

```Python
input_data = {"groups": ["admin", "editor"]}
```

- **Task:** Run the code mentally or physically. How does the current implementation handle lists? Does it crash? Does it ignore them? Does it include them as-is?

- **Requirement:** Write a test that asserts whatever the current behavior is (even if that behavior is weird). This is called "Characterization Testing"—documenting exactly how the code acts right now.