## 1. What is a Fixture?
A fixture is a function decorated with `@pytest.fixture`. It performs setup (creating data, connecting to DBs) and returns a value.

## 2. Dependency Injection
You don't call fixtures like normal functions. Instead, you put the fixture's name as an argument in your test function. Pytest automatically finds the fixture, runs it, and passes the return value to your test.

## 3. "DRY" Testing
"Don't Repeat Yourself." If 5 tests need a list of server logs, you define the list in one fixture. If the log format changes later, you update it in one place, not 5.

## 4. Scopes
* `scope="function"` (Default): The fixture runs fresh for every single test function. Safe, but slower.
* `scope="session"`: Runs once for the whole test suite. Great for connecting to a database (Module 8).