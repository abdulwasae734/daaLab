def fractional_knapsack(weights, values, capacity):
    value_per_weight = [(values[i] / weights[i], weights[i], values[i]) for i in range(len(weights))]
    value_per_weight.sort(reverse=True)
    total_value = 0
    remaining_capacity = capacity
    
    for ratio, weight, value in value_per_weight:
        if remaining_capacity >= weight:
            total_value += value
            remaining_capacity -= weight
        else:
            total_value += ratio * remaining_capacity
            break
            
    return total_value

n = int(input("Enter the number of items: "))
weights = []
values = []

print("Enter weights and values for each item:")
for i in range(n):
    w = int(input("Enter weight for item {}: ".format(i + 1)))
    v = int(input("Enter value for item {}: ".format(i + 1)))
    weights.append(w)
    values.append(v)

capacity = int(input("Enter the capacity of knapsack: "))

max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value that can be obtained:", max_value)
