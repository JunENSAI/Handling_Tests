# Module 2: Pytest Configuration and Discovery Mechanisms

## 1. Test Discovery

Unlike the older `unittest` library which required verbose classes, Pytest uses a powerful discovery system.

* **File Naming:** Pytest automatically scans your directories for files matching `test_*.py` or `*_test.py`.

* **Function Naming:** Within those files, it looks for functions starting with `test_`.

---

## 2. The Configuration File (`pytest.ini`)

The `pytest.ini` file is the control center for your testing framework. It sits at the root of your project. It allows you to:

* **Register Markers:** Define categories like `@pytest.mark.slow` or `@pytest.mark.integration`.

* **Enforce Strictness:** You can configure Pytest to fail if a developer creates a typo in a marker name (e.g., `@pytest.mark.smok` instead of `smoke`). [cite_start]This is crucial for CI/CD environments.

* **Set Defaults:** Define default command-line arguments (e.g., always showing verbose output).

---

## 3. Professional Directory Structure
To prevent testing code from being packaged with your production code, we separate them into distinct directories.

**Standard Structure:**
```text
project_root/
├── pytest.ini
├── src/
│   ├── __init__.py
│   └── transformations.py
└── tests/
    ├── __init__.py
    └── test_transformations.py
```

---