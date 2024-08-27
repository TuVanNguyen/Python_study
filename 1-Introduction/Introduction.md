# 1. Introduction

## 1.3 What is Computer Science?
  * the study of problems, problem solving, and solutions from the problem solving process
  * a study of algorithms
    * def **algorithm**: n.finite processes that if followed will solve a problem
  * the study of problems that are and that are not computable 
    * def **computable**: adj. having an existing algorithm that can solve it [a problem]
  * the study of **abstraction** of problems and algorithms
    * e.g user interfaces, the use of libraries to reuse solutions without knowing all the details

## 1.4 What is Programming?
  * writing an algorithm into a programming language, to be executed by a computer
  * creating the representation on our solutions

## 1.5 Why Study Data Structures and Abstract Data Types
  * Help simplify problems and problem-solving process, to effectively understand and manipulate them
  *  **abstract data type**: logical description of data members and operations disregarding implementation
  * **data structure**: the implementation of an abstract data type

## 1.6 Why Study Algorithms
  * algorithms can act as a set of techniques for solving known problems, to help us solve new problems
  * develop better pattern recognition so better understand how to solve the next problem
  * to be able to compare algorithms and figure out the better or best solution
  * to distinguish solvable from unsolvable problems

## 1.8 Atomic Data Types

### 1.8.1 Numeric Data Types
* int
* float

| Operator | Description                                     |
|----------|-------------------------------------------------|
| x+y      |                                                 |
| x-y      |                                                 |
| x*y      | multiplication                                  |
| x//y     | integer division, returns truncated integer     |
| x/y      | floating point division, returns floating point | 
| x%y      | modulo, remainder                               |
| x*y      | exponentiation                                  |


### 1.8.1 Boolean Data Type
  * bool: value is either True or False

| Operator | Description                     |
|----------|---------------------------------|
| x<y      | less than                       |
| x>y      | greater than                    |
| x<=y     | less than or equal to           |
| x>=y     | greater than or equal to        |
| x==y     | equal to                        |
| x!=y     | not equal                       |
| x and y  | and (both True)                 |
| x or y   | inclusive or (one or both True) |
| not x    | negation (not True)             | 

## 1.8.2 Built-in Collection Data Types
  * list: mutable sequence of references to Python data objects
  * strings: immutable sequence of chars
  * tuples: immutable sequence of data objects 
  * dictionaries: unordered collection of key-value pairs
  * sets: unordered collection of unique data objects

### Ordered Collections (aka Sequences) 

```commandline
myList = [1.5,1,"cat",True]
myString = "I am a string"
myTuple = (1,False,"kitty")
```

| Operator | Description                                                 |
|----------|-------------------------------------------------------------|
| [ ]      | indexing; access i<sup>th</sup> element in sequence         |
| +        | concatenation; join two sequences together                  |
| *        | repetition; join copies of the same sequence i times        |
| in       | membership; return bool for whether item is in the sequence |
| len()    | length; returns number of items in the sequence             |
| [i:j]    | slicing; return the i<sup>th</sup> to j<sup>th</sup> item   |

### Sets

```commandline
mySet = {3,6,"cat",4.5,False}
```

| Operator   | Description                                                       |
|------------|-------------------------------------------------------------------|
| in         | membership; return True if item in set, else False                |
| len()      | length; number of items in set                                    |
| x &#124; y | union; returns new set with all elements from set x and y         |
| x & y      | intersection; returns new set with elements common to set x and y |
| x-y        | difference; returns new set with all items in set x not in set y  |
| x <= y     | subset; returns bool of whether x is subset of y                  |

### Dictionaries

```commandline
capitals = {'Iowa':'DesMoines','Wisconsin':'Madison'}
```

| Operator         | Description                            |
|------------------|----------------------------------------|
| myDict[key]      | get value for key in dict              |
| key in myDict    | return True if key in dict, else False |
| del myDict[key]  | delete key from dict                   |

### 1.9.1 String Formatting

#### Using print()

```commandline
aName = "Mary"
age=19
print("%s is %d years old." % (aName, age))
# Output:"Mary is 19 years old"
```

| Format Operator | Description                      |
|-----------------|----------------------------------|
| %d, %i          | integer                          |
| %u              | unsigned integer                 |
| %f              | floating point as m.ddddd        |
| %e              | floating point as m.ddddde+/-xx  |
| %E              | floating point as m.dddddE+/-xx  |
| %c              | single character                 | 