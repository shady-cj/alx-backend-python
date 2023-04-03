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



### 1. Let's execute multiple coroutines at the same time with async

Import `wait_random`from the previous python file that you’ve written and write an async routine called `wait_n` that takes in 2 int arguments (in this order): `n` and `max_delay`. You will spawn `wait_random` `n` times with the specified `max_delay`.

`wait_n `should return the list of all the delays (float values). The list of the delays should be in ascending order without using `sort()` because of concurrency.



```
bob@dylan:~$ cat 1-main.py
#!/usr/bin/env python3
'''
Test file for printing the correct output of the wait_n coroutine
'''
import asyncio

wait_n = __import__('1-concurrent_coroutines').wait_n

print(asyncio.run(wait_n(5, 5)))
print(asyncio.run(wait_n(10, 7)))
print(asyncio.run(wait_n(10, 0)))

bob@dylan:~$ ./1-main.py
[0.9693881173832269, 1.0264573845731002, 1.7992690129519855, 3.641373003434587, 4.500011569340617]
[0.07256214141415429, 1.518551245602588, 3.355762808432721, 3.7032593997182923, 3.7796178143655546, 4.744537840582318, 5.50781365463315, 5.758942587637626, 6.109707751654879, 6.831351588271327]
[0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
```
The output for your answers might look a little different and that’s okay.

**File**: `1-concurrent_coroutines`





### 2. Measure the runtime
From the previous file, import wait_n into 2-measure_runtime.py.

Create a `measure_time` function with integers `n` and `max_delay` as arguments that measures the total execution time for `wait_n(n, max_delay)`, and returns `total_time / n`. Your function should return a `float`.

Use the time module to measure an approximate elapsed time.


```
bob@dylan:~$ cat 2-main.py
#!/usr/bin/env python3

measure_time = __import__('2-measure_runtime').measure_time

n = 5
max_delay = 9

print(measure_time(n, max_delay))

bob@dylan:~$ ./2-main.py
1.759705400466919
```

**File**: `2-measure_runtime.py`