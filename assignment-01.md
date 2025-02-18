

# CMPS 2200 Assignment 1

**Name:**_________________________


In this assignment, you will learn more about asymptotic notation, parallelism, functional languages, and algorithmic cost models. As in the recitation, some of your answer will go here and some will go in `main.py`. You are welcome to edit this `assignment-01.md` file directly, or print and fill in by hand. If you do the latter, please scan to a file `assignment-01.pdf` and push to your github repository. 
  
  

1. (2 pts ea) **Asymptotic notation** (12 pts)

  - 1a. Is $2^{n+1} \in O(2^n)$? Why or why not? 
.  Yes it is, because big-O notation a function f(n) is said to be O(g(n)) is there are positive constants c and k such that f(n) =< c x g(n) for all n >= k. To determine if there exists constants c and k such that 2^n + 1 <= c x 2^n for all n>=k you can rearrange it such that 1/2^n <= c-1. and if we choose c=2 we get a simplified expression 2^n + 1 <= 2^n+1, and since 2^n + 1 is always less than or equal to 2^n+1 for n >=1 the condition holds. 
.  
.  
.  
. 
  - 1b. Is $2^{2^n} \in O(2^n)$? Why or why not?     
.  This is not true because by using the definition of big-O we get
. 2^2n <= c x 2^n, which we can then reduce to
.ln 2 x 2n <= ln c + ln2 x n
.  2n<= ln c + n
.  n <= ln c , this is wrong because there is no constant that can satisfy this inequality
.  
  - 1c. Is $n^{1.01} \in O(\mathrm{log}^2 n)$?    
.  no because in order for this to be true there exists consts c and k such that: f(n) <= c x g(n) for all n >= k. We can check if this is true by evaluating the limit, if we do n^1.01/ log^2 n we can see that the fraction grows to infinity with a very large n value. Because the limit is equal to infinity it means that f(n) grows faster than g(n) which contradicts the Big-O requirement that f(n) should be boune dabove some constant multiple of g(n), so f(n) is not equal to O(g(n)). so this is not true. 
.  
.  
.  

  - 1d. Is $n^{1.01} \in \Omega(\mathrm{log}^2 n)$?  
.  Yes this is true because in order for this to be true there needs to exist positive constants c and k such that f(n) >= c x g(n) for all n>= k. This means for sufficiently large n, f(n) grows at least as far as g(n) up to a constant multiple. Since for succiefienctly large n, n^1.01 will be larger than some constant multiple of log2n so this statement is true.
.  
.  
.  
  - 1e. Is $\sqrt{n} \in O((\mathrm{log} n)^3)$?
  - The function square root of n grows polynomially and the function (log n) ^3 grows polylogarithmaically. if we exam the limits, the square root of n grows much aster than log^3 , since the ratio is not bounded we can conclude that it is impossible to find a constant c such that square root of n <= c (long n)^3 for all large n and that the statement is not true. 
.  
.  
.  
.  
  - 1f. Is $\sqrt{n} \in \Omega((\mathrm{log} n)^3)$?  
.  If we analyze the behavior using limits, the swuare root of n is larger than log n^3 in growth rate so the ratio will diverge into infinity. Because the ratio diverges, we can conclude that we can always find a constant c>0 such that the swuare root of n >= c(log n)^3 for a large n so we can conclude that this statement is true


2. **SPARC to Python** (12 pts)

Consider the following SPARC code of the Fibonacci sequence, which is the series of numbers where each number is the sum of the two preceding numbers. For example, 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610 ... 
$$
\begin{array}{l}
\mathit{foo}~x =   \\
~~~~\texttt{if}{}~~x \le 1~~\texttt{then}{}\\
~~~~~~~~x\\   
~~~~\texttt{else}\\
~~~~~~~~\texttt{let}{}~~(ra, rb) = (\mathit{foo}~(x-1))~~,~~(\mathit{foo}~(x-2))~~\texttt{in}{}\\  
~~~~~~~~~~~~ra + rb\\  
~~~~~~~~\texttt{end}{}.\\
\end{array}
$$ 

  - 2a. (6 pts) Translate this to Python code -- fill in the `def foo` method in `main.py`  

  - 2b. (6 pts) What does this function do, in your own words?  

.  
.  
.  
.  
.  
.  
.  
.  
  

3. **Parallelism and recursion** (26 pts)

Consider the following function:  

```python
def longest_run(myarray, key)
   """
    Input:
      `myarray`: a list of ints
      `key`: an int
    Return:
      the longest continuous sequence of `key` in `myarray`
   """
```
E.g., `longest_run([2,12,12,8,12,12,12,0,12,1], 12) == 3`  
 
  - 3a. (7 pts) First, implement an iterative, sequential version of `longest_run` in `main.py`.  

  - 3b. (4 pts) What is the Work and Span of this implementation?  

.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3c. (7 pts) Next, implement a `longest_run_recursive`, a recursive, divide and conquer implementation. This is analogous to our implementation of `sum_list_recursive`. To do so, you will need to think about how to combine partial solutions from each recursive call. Make use of the provided class `Result`.   

  - 3d. (4 pts) What is the Work and Span of this sequential algorithm?  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  
.  


  - 3e. (4 pts) Assume that we parallelize in a similar way we did with `sum_list_recursive`. That is, each recursive call spawns a new thread. What is the Work and Span of this algorithm?  

.  
.  
.  
.  
.  
.  
.  
.  

