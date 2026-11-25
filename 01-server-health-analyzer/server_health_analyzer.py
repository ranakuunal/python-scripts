"""Task: Write a Python program that:
1. Calculates the total number of servers.
2. Counts how many servers are running.
3. Counts how many servers are stopped.
4. Prints the names of all stopped servers.
5. Calculates the percentage of servers that are running."""

def server_health(servers_list):
    total_servers = 0
    running_servers = 0
    stopped = 0
    stopped_servers = []
    
    if not servers_list:
        print('No instances found.')
        return
    
    for server in servers_list:
        total_servers += 1
        if server["status"] == "running":
            running_servers += 1
        elif server["status"] == "stopped":
            stopped += 1
            stopped_servers.append(server['name'])
        else:
            print('Unknown status')
    print(f'Total number of servers are: {total_servers}')
    print(f'Number of running servers are: {running_servers}')
    print(f'Number of stopped servers are: {stopped}')
    print('The stopped servers are: ')
    for s in range(len(stopped_servers)):
        print(stopped_servers[s])
    print(f'Percentage of running servers: {running_servers / total_servers * 100:.2f}%')

if __name__ == "__main__":
    servers = [
    {"name": "web-01", "status": "running"},
    {"name": "web-02", "status": "stopped"},
    {"name": "db-01", "status": "running"},
    {"name": "db-02", "status": "stopped"},
    {"name": "app-01", "status": "running"},
    {"name": "app-02", "status": "stopped"},
    {"name": "cache-01", "status": "running"}
]
    server_health(servers)