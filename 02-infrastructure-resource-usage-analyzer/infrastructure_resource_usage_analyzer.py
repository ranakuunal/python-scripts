"""
Write a Python function that:
1. Calculates the total number of instances.
2. Calculates the average CPU utilization across all instances.
3. Calculates the average memory utilization across all instances.
4. Identifies instances with CPU usage strictly greater than 80%.
5. Identifies instances with memory usage strictly greater than 80%.
6. Identifies instances where both CPU and memory usage are strictly greater than 80%.
"""
"""
Rules
- Create at least one function that accepts the instance dataset as a parameter.
- Use only the Python fundamentals you've already learned.
- No external libraries are required.
- Format the average percentages to two decimal places.
- Write the solution independently, without AI-generated code.
"""

def resource_usage_analyzer(server_usage):
    total_instances = 0
    total_cpu_usage = 0
    total_mem_usage = 0
    high_cpu_usage = []
    high_mem_usage = []
    high_cpu_mem_usage = []
    
    categories = {
        "High CPU Usage (>80%):" : high_cpu_usage,
        "High Memory Usage (>80%):" : high_mem_usage,
        "High CPU and Memory Usage (>80%):" : high_cpu_mem_usage
    }
    
    if not server_usage:
        print('No instances found.')
        return
    
    for server in server_usage:
        total_instances += 1
        total_cpu_usage += server['cpu']
        total_mem_usage += server['memory']
        
        if server['cpu'] > 80 and server['memory'] > 80:
            high_cpu_mem_usage.append(server['name'])
            high_mem_usage.append(server['name'])
            high_cpu_usage.append(server['name'])
        elif server['cpu'] > 80:
            high_cpu_usage.append(server['name'])
        elif server['memory'] > 80:
            high_mem_usage.append(server['name'])
    
    print(f'Total Instances: {total_instances}\n')
    print(f'Average CPU usage: {total_cpu_usage / total_instances:.2f}%\n')
    print(f'Average Memory usage: {total_mem_usage / total_instances:.2f}%\n')
    
    for headings, names in categories.items():
        print(headings)
        print(*names, sep="\n")
        print()

if __name__ == '__main__':
    
    instances = [
    {"name": "web-01", "cpu": 45, "memory": 60},
    {"name": "web-02", "cpu": 85, "memory": 70},
    {"name": "app-01", "cpu": 92, "memory": 88},
    {"name": "app-02", "cpu": 35, "memory": 91},
    {"name": "db-01", "cpu": 78, "memory": 82},
    {"name": "db-02", "cpu": 25, "memory": 40},
    {"name": "cache-01", "cpu": 65, "memory": 55}
]  

    resource_usage_analyzer(instances)