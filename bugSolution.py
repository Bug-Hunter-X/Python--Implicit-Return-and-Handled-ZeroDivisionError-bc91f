def improved_function(x):
    if x == 0:
        return float('inf') # Or raise a more specific exception
    elif x < 0:
        return None # Explicitly indicate no result for negative x 
    else:
        return x * 2

result = improved_function(-1)
print(result) # Output: None
result2 = improved_function(0)
print(result2) # Output: inf
result3 = improved_function(5)
print(result3) # Output: 10