# Python Scripting Practice
## Overview
This repository documents my Python scripting learning journey, focusing on developing practical automation skills relevant to Cloud Engineering, DevOps, Infrastructure Engineering and System Administration.

The goal is to strengthen my Python fundamentals through hands-on exercises and gradually progress toward real-world infrastructure automation
### Exercises
#### Exercise 01 - Server Health Analyzer 

File: server_health_analyzer.py

##### Description:
A Python script that processes a predefined list of servers and generates a summary of their operational statuses.

###### Features:
1. Calcualtes the total number of servers.
2. Identifies and counts running servers.
3. Identifies and counts stopped servers.
4. Displays the names of stopped servers.
5. Calculates the percentage of running servers.

###### Python concepts practised:
1. Functions and parameters
2. Lists and dictionaries
3. For Loops
4. Conditional statements
5. Counters
6. List maipulation
7. F-string formatting

###### Sample Output:
Total number of servers are: 7
Number of running servers are: 4
Number of stopped servers are: 3

The stopped servers are:
web-02
db-02
app-02
Percentage of running server: 57.14%

###### Limitations:
The current implementation works with a predefined list of servers whost status are either 'running' or 'stopped'. It does not perform live infrastructure monitoring or handle empty server lists.