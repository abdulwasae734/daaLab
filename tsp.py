import sys

def tsp_max_profit(cities, profits, dist):
    n = len(cities)
    num_sets = 2 ** n
    
    dp = [[sys.maxsize] * n for _ in range(num_sets)]
    dp[1][0] = 0  
    
    for mask in range(1, num_sets):
        for u in range(n):
            if mask & (1 << u):  
                for v in range(n):
                    if u != v and mask & (1 << v): 
                        dp[mask][u] = min(dp[mask][u], dp[mask ^ (1 << u)][v] + dist[v][u])
    
    min_dist = sys.maxsize
    for u in range(1, n):
        min_dist = min(min_dist, dp[num_sets - 1][u] + dist[u][0])  
    
    return min_dist

cities = ["A", "B", "C", "D"]
profits = [10, 20, 15, 25]


distances = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

max_profit = tsp_max_profit(cities, profits, distances)
print("Maximum profit:", max_profit)
