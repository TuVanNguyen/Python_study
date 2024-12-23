# Algorithm Analysis
    * compare the efficiency of algorithms based on how much computing resources each algorithm uses to solve the same problem
        * typical computing resources:
            * memory used
            * execution time
### Benchmark Analysis of Execution Time in Python
```
import time
def sumOfN2(n):
      theSum = 0
   for i in range(1,n+1):
      theSum = theSum + i
   return theSum,end-start
if __name__ == "__main__":
    # Performing Benchmark analysis below with time module
    start = time.time()
    sumOfN2(10)
    end = time.time()
```
## Big-O Notation
    * Mathematically analyze of algorithm execution time by quantifying the number of operations required to solve the problem
    * Notation for function quantifying number of operations: `T(n) = ...`
        * n = size of problem
        * T(n) = time to solve problem of size n
    * Notation for dominant part of T(n): `f(n)`
        * f(n) is the fastest growing component of T(n) 
