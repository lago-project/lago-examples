Lago simple fixture example
----------------------------
This is a simple example showing how you can easily create a pytest fixture
that encapsulates the isolated environment Lago creates, which is defined in
``init-myapp.yaml``.

Requires: Lago and pytest installed.

To run execute:
```bash
> pytest -vvv test_myapp.py
```

The tests should obviously fail as the application was not installed.
When they fail notice how the directory ``test_results`` was created where you
ran the tests, with the logs taken before tearing down the environment.
