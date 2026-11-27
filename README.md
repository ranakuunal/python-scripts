# Python Scripting Practice
## Overview
This repository documents my Python scripting learning journey, focusing on developing practical automation skills relevant to Cloud Engineering, DevOps, Infrastructure Engineering and System Administration.

The goal is to strengthen my Python fundamentals through hands-on exercises and gradually progress toward real-world infrastructure automation
### Exercises
### Exercise 01 - Server Health Analyzer 

**File**: server_health_analyzer.py

**Description**:
Analyzes server operational statuses, identifies stopped servers and calculate overall server availability.

**Features**:
- Counts total, running and stopped servers.
- Displays names of stopped servers.
- Calculates server availability perccentage

**Python concepts practised**:
Functions, lists, dictionaries, loops, conditionals, counters and f-strings.

**Sample Output**:
- Total number of servers are: 7
- Number of running servers are: 4
- Number of stopped servers are: 3

The stopped servers are:
- web-02
- db-02
- app-02

Percentage of running server: 57.14%

### Exercise 02 - Infrastructure Resource Usage Analyzer

**File** - resource_usage_analyzer.py

**Description**: Analyzes CPU and memory usage across multiple instances, calculates average utilization and identifies exceeding 80% usage thresholds.

**Features**:
- Calculates total instances and average CPU/Memory usage.
- Identifies instances with high CPU, memory, or both.
- Handles empty datasets gracefully.
- Generates a formatted resource utilization report.

**Concepts Practised**:
Functions, dictionaries, lists, loops, conditionals, f-strings, dictionary.items() and gaurd clauses.

**Sample Output**:

- Total Instances: 7
- Average CPU Usage: 60.71%
- Average Memory Usage: 69.43%

High CPU Usage (>80%):
- web-02
- app-01

High Memory Usage (>80%):
- app-01
- app-02
- db-01

High CPU and Memory Usage (>80%):
- app-01

### Exercise 03 — Linux Server Log Analyzer

**File:** `linux_server_log_analyzer.py`

**Description:** Reads and analyzes Linux server logs to identify errors, monitor log levels, and detect servers with the most failures.

**Features:**
- Reads and validates log entries from a `.log` file.
- Counts INFO, WARNING, and ERROR logs.
- Identifies servers with errors and ranks them by error count.
- Skips malformed log entries.

**Concepts Practised:** File handling, functions, string methods, lists, sets, tuples, sorting, loops, and input validation.

**Sample Output**:
========== SERVER LOG ANALYSIS ==========

Total Valid Logs: 11

- INFO Logs: 4
- WARNING Logs: 3
- ERROR Logs: 4

Servers with Errors:
- db-01: 3 errors
- app-01: 1 error

Server with Most Errors: db-01 (3 errors)

Invalid Log Entries Skipped: 1

=========================================