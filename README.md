This repository contains a simple Python function that highlights two potential sources of confusion or bugs:

1. **Implicit Return of None:** The function doesn't explicitly return a value when `x` is negative, leading to an implicit return of `None`. This might be unexpected and cause issues in other parts of the code.
2. **Handled ZeroDivisionError:**  The function handles the potential `ZeroDivisionError` when `x` is 0. While this prevents a program crash, the behavior (and error handling) may need to be made explicit, depending on the application's requirements.

The `bugSolution.py` file shows how to improve the function by adding explicit returns and better error handling.