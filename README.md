# Basic data structures

### Task 1

You need to develop a program that simulates the intake and processing of requests: the program should automatically generate new requests (identified by a unique number or other data), add them to a queue, and then sequentially remove them from the queue for "processing," thus simulating the operation of a service center.

Here is the pseudocode for the task using a queue (Queue from the queue module in Python) for the request processing system:

```python

```

In this pseudocode, two main functions are used: generate_request(), which generates new requests and adds them to the queue, and process_request(), which processes requests by removing them from the queue. The main program loop executes these functions, simulating a constant flow of new requests and their processing.

Task 2
You need to develop a function that takes a string as an input parameter, adds all its characters to a deque (from the collections module in Python), and then compares the characters from both ends of the deque to determine if the string is a palindrome. The program should correctly handle both even and odd-length strings and be case-insensitive and space-insensitive.

Here is the pseudocode for the task:

```python

```

Task 3 (Optional)
In many programming languages, we deal with expressions marked by delimiter characters such as round ( ), square [ ], or curly braces { }.

Write a program that reads a string with a sequence of delimiter characters, such as (){}[]()(){} }, and provides an appropriate message when the delimiters are symmetrical, asymmetrical, or when delimiters of different types are paired, such as ()}.

💡 Use a stack to remember currently open delimiter characters.

Here is the pseudocode for the task:

```python

```
