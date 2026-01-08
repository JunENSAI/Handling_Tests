## 1. What is Code Coverage?
Code coverage is a metric (percentage) that tells you how much of your codebase was actually run when you executed your tests. 

* **Green lines:** Code that ran.

* **Red lines:** Code that was never touched by any test.

---

## 2. Tools
We use `pytest-cov`, a plugin for pytest. 

* **Usage:** `pytest --cov=src tests/`

* This command tells pytest to run the tests in the `tests/` folder while monitoring the `src/` folder.

---

## 3. The Goal
While 100% coverage is not always necessary for every utility script, **core ETL transformations** (like your `flatten_json` or `standardize_date`) should aim for high coverage (90%+) because a bug there corrupts data downstream.

### Commands to run

- If you wanna see the coverage tests type :
```bash
pytest --cov=src tests/
```
- Generate a full report on HTML page :
```bash
pytest --cov=src --cov-report=html tests/
```