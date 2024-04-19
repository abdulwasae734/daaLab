def fractional_knapsack(item_weights, item_values, max_capacity):
    # Calculate the value per unit weight for each item and store it with the original weight and value
    items = [(item_values[i] / item_weights[i], item_weights[i], item_values[i]) for i in range(len(item_weights))]
    # Sort items based on the value per unit weight in descending order
    items.sort(reverse=True)
    
    total_value = 0
    remaining_capacity = max_capacity
    
    # Process each item in the sorted list
    for value_ratio, weight, value in items:
        if remaining_capacity >= weight:
            # If the remaining capacity can hold the entire item, add its full value
            total_value += value
            remaining_capacity -= weight
        else:
            # Otherwise, add as much value as the remaining capacity allows
            total_value += value_ratio * remaining_capacity
            break
            
    return total_value

# Get user input for the number of items
num_items = int(input("Enter the number of items: "))
weights = []
values = []

print("Enter weights and values for each item:")
for i in range(num_items):
    w = int(input(f"Enter weight for item {i + 1}: "))
    v = int(input(f"Enter value for item {i + 1}: "))
    weights.append(w)
    values.append(v)

# Get the knapsack's maximum capacity from the user
capacity = int(input("Enter the capacity of the knapsack: "))

# Calculate the maximum value the knapsack can carry
max_value = fractional_knapsack(weights, values, capacity)
print("Maximum value that can be obtained:", max_value)
