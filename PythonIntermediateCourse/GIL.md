#### Global Interpreter Lock (GIL)
- A lock that allows only 1 thread at a time to execute in Python
- Needed in CPython because memory management is not thread-safe
- Avoid
    - Use multiprocessing
    - Use a different, `free-threaded` python implementation `(Jython, IronPython)`
    - Use Python as wrapper for third-party libraries (C++/Java): `numpy, scipy`