def function_with_uncommon_error(x):
    if x == 0:
        return 1/x  # ZeroDivisionError, but it's handled
    elif x < 0:
        return  # Implicit return of None; unexpected behavior
    else:
        return x * 2

result = function_with_uncommon_error(-1)
print(result) # Output: None, might be unexpected
result2 = function_with_uncommon_error(0)
print(result2) # Output: raises ZeroDivisionError
result3 = function_with_uncommon_error(5)
print(result3) # Output: 10