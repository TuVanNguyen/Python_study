# Karat Interview Guide

### Companies known to use Karat
* Atlassian
* Indeed
* Intuit
* Palantir
* Pinterest
* Schlumberger (SLB): Houston based
* Roblox
* Walmart
* Ecomm: Wayfair. Instacart
* Finance: Citi
* FinTech: SoFi, Coinbase, Paypal, Robinhood

## Interview Structure 
* ~60 minutes overall
* can schedule 1 redo

### Domain Knowledge
* focuses on core concepts directly related to the role
* More open ended questions that tests ability to reason about real world systems and architectural decisions

#### Strategies
* be short, accurate, to the point 
* acknowledge knowledge gaps early, quickly, and politely
* relate to experience if applicable: still be very brief, mention specifics if possible
* leave time for coding section, probably spend less that 10 minutes here

#### Study Strategy
* very low priority: others have reported successfully passing the Karat screen despite doing poorly in domain knowledge, by passing the coding screen

### Live Coding
* Ideally solve at least 2 parts or problems in the given time

#### Problem Solving Evaluation
* Correctness: handle requirements and edge cases
* clarity and reasoning: communicate logic, assumptions, design choices
* working: code is function; DO NOT need to provide optimal solution

#### Final Evaluation
* Run code against test cases provided by interviewer to verify correctness and edge cases
* Discuss time and space complexity  

#### Performance Strategies
* communicate constantly: treat interviewer as collaborator
    * Before starting
        * ask clarifying questions if needed to understand the problem as quickly as possible
        * state your assumptions
        * walk through thought process
        * set up test cases (provided or you thought of) first: explain you're starting with a test driven development approach
            * buys you time to think of a solution
            * gives you a chance to think and talk about any edge cases you want to make sure to capture
            * clarifies what your expected inputs and outputs are before you begin
    * while coding:
        * walkthrough the approach you're taking
        * bring up tradeoffs e.g using additional space or increasing time complexity for code that's quicker to implement and easier to read
        * can bring up other approaches you'd try if you had more time
        * if you are stuck, be sure to ask the interviewer clarifying questions or suggestions
* Focus on correctness, rather than most optimal algorithm

## Study Strategies (Coding)

### Coding
* Slow is smooth, smooth is fast
* practice coding on the Karat Studio IDE
* practice identifying and settting up all your test cases fairly quickly

### Topics To Cover (Ordered by Priority for each section)
* Algorithms:
    * merge sort (low priority, maybe just memorize the python command for it)
    * breadth-first search
    * depth first search
    * binary search
* Data Structures 
    * Arrays/List
    * hash tables/dictionary
    * trees 
    * graphs
    * stacks/queues
    * heaps
* Concepts 
    * Big O complexity analysis (high priority)
    * recursion