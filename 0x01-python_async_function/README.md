# 0x01-python_async_function

Learning the concept of asynchronous programming in python using the newly introduced async/await syntax (python3.4-till date) and the asyncio library.

At the end of this project the following concepts should be fully understood.


* async and await syntax
* How to execute an async program with asyncio
* How to run concurrent coroutines
* How to create asyncio tasks
* How to use the random module


## TASKS


### 0. The basics of async
Write an asynchronous coroutine that takes in an integer argument (`max_delay`, with a default value of 10) named `wait_random` that waits for a random delay between 0 and `max_delay` (included and float value) seconds and eventually returns it.

Use the `random` module.


```
bob@dylan:~$ cat 0-main.py
#!/usr/bin/env python3

import asyncio

wait_random = __import__('0-basic_async_syntax').wait_random

print(asyncio.run(wait_random()))
print(asyncio.run(wait_random(5)))
print(asyncio.run(wait_random(15)))

bob@dylan:~$ ./0-main.py
9.034261504534394
1.6216525464615306
10.634589756751769
```

**File**: `0-basic_async_syntax.py`