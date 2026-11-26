# Python Scripting Practice
## Overview
This repository documents my Python scripting learning journey, focusing on developing practical automation skills relevant to Cloud Engineering, DevOps, Infrastructure Engineering and System Administration.

The goal is to strengthen my Python fundamentals through hands-on exercises and gradually progress toward real-world infrastructure automation
### Exercises
#### Exercise 01 - Server Health Analyzer 

File: server_health_analyzer.py

##### Description:
Analyzes server operational statuses, identifies stopped servers and calculate overall server availability.

###### Features:
1. Counts total, running and stopped servers.
2. Displays names of stopped servers.
3. Calculates server availability perccentage

###### Python concepts practised:
Functions, lists, dictionaries, loops, conditionals, counters and f-strings.

###### Sample Output:
Total number of servers are: 7

Number of running servers are: 4

Number of stopped servers are: 3

The stopped servers are:

web-02

db-02

app-02

Percentage of running server: 57.14%

#### Exercise 02 - Infrastructure Resource Usage Analyzer

File - resource_usage_analyzer.py

##### Description: Analyzes CPU and memory usage across multiple instances, calculates average utilization and identifies exceeding 80% usage thresholds.

###### Features:
1. Calculates total instances and average CPU/Memory usage.
2. Identifies instances with high CPU, memory, or both.
3. Handles empty datasets gracefully.
4. Generates a formatted resource utilization report.

##### Concepts Practised:
Functions, dictionaries, lists, loops, conditionals, f-strings, dictionary.items() and gaurd clauses.