def remove_duplicates_preserve_order(lst):
    seen = set()
    result = []
    for item in lst:
        if item not in seen:
            seen.add(item)
            result.append(item)
    return result

# Given list
lst = [12, 24, 35, 24, 88, 120, 155, 88, 120, 155]

# Remove duplicates preserving order
result = remove_duplicates_preserve_order(lst)

# Print the result
print(result)  
