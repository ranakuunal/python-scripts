"""Write a Python program that:
1. Reads the contents of server.log.
2. Calculates the total number of valid log entries.
3. Counts the number of INFO, WARNING, and ERROR entries.
4. Identifies every server that generated an ERROR.
5. Counts how many errors each of those servers generated.
6. Identifies the server with the highest number of errors.
7. Skips malformed log entries without crashing the program."""

"""Rules
- Create at least one function.
- Read the logs from the actual .log file rather than hardcoding the entries in Python.
- Use only Python concepts you've already studied.
- No third-party libraries.
- Don't use AI-generated solutions.
- You can refer to your Python notes and official documentation."""

def log_analyzer(filename):
    valid_log_entries = 0
    invalid_log_entries = 0
    info_logs = 0
    warning_logs = 0
    error_logs = 0
    log_levels = []
    error_servers = []
    server_count = []
    
    with open (filename) as file:
        for line in file:
            parts = [part.strip() for part in line.split("|")]
            
            if (
                len(parts) != 4
                or not all(parts)
                or parts[1] not in ('INFO', 'WARNING', 'ERROR')
                ):
                invalid_log_entries += 1
                continue
            
            valid_log_entries += 1
            log_levels.append(parts[1])
            
            if parts[1] == "ERROR":
                error_servers.append(parts[2])

    for level in log_levels:
        if level == 'INFO':
            info_logs += 1
        elif level == 'WARNING':
            warning_logs += 1
        elif level == 'ERROR':
            error_logs += 1
    
    for server in set(error_servers):
        server_count.append((error_servers.count(server), server))
    server_count.sort(reverse=True)
    
    print('==========SERVER LOG ANALYSIS==========\n')
    print(f'Total Valid Logs: {valid_log_entries}\n')
    print(f'INFO Logs: {info_logs}\nWARNING Logs: {warning_logs}\nERROR Logs: {error_logs}\n')
    
    print('Servers with Errors:')
    for item in server_count:
        print(f'{item[1]}: {item[0]}')
    print()
    
    if server_count:
        count, server = server_count[0]
        print(f'Server with Most Errors: {server} ({count} errros)\n')
    else:
        print('Server with most errors: None\n')
    print(f'Invalid Log Entries Skipped: {invalid_log_entries}\n')
    print('=======================================')

if __name__ == '__main__':
    log_analyzer('server.log')