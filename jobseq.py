def sort_projects_by_profit(project):
    return project[1]

def maximize_profit(projects):
    projects.sort(key=sort_projects_by_profit, reverse=True)
    timeline = [False] * max(p[0] for p in projects)
    total_profit = 0
    sequence_of_jobs = []
    
    for project in projects:
        deadline, profit = project
        while deadline > 0 and timeline[deadline - 1]:
            deadline -= 1
        if deadline > 0:
            timeline[deadline - 1] = True
            total_profit += profit
            sequence_of_jobs.append(project)
    
    return total_profit, sequence_of_jobs

projects = []
n = int(input("Enter the number of projects: "))
for i in range(n):
    deadline = int(input(f"Enter deadline for project {i+1}: "))
    profit = int(input(f"Enter profit for project {i+1}: "))
    projects.append((deadline, profit))

max_profit, sequence_of_jobs = maximize_profit(projects)
print("Maximum Profit:", max_profit)
print("Sequence of Jobs Executed:", sequence_of_jobs)
