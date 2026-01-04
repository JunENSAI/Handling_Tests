## Task 1: Create the Configuration

- Create a file named `pytest.ini` in your project_root.

- Requirement A: Register a custom marker named unit (for fast unit tests) and integration (for slow DB tests).

- Requirement B: Add a configuration setting that enforces strict markers. This means if someone tries to use a marker that isn't listed in the ini file, Pytest should raise an error.

---

## Task 2: The "Failing" Test

- Create a new test file tests/test_module_2.py.

- Write a simple test function (it can just assert True).

- Decorate this function with a marker that you did not register in Task 1 (e.g., @pytest.mark.smoke).

---

## Task 3: Verification

- Run pytest in your terminal.

- **Success Condition**: The test run should FAIL (or error out) specifically complaining that 'smoke' not found in markers configuration option.

If the test passes, you haven't successfully enforced strict markers!