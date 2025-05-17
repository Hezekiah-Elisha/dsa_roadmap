#!/usr/bin/python3
def maximum_and_minimum(arr: list) -> tuple:
    """
    This function takes a list of integers and returns a tuple containing the maximum and minimum values in the list.
    
    :param arr: List of integers
    :return: Tuple (max_value, min_value)
    """
    if not arr:
        return None, None
    
    max_value = arr[0]
    min_value = arr[0]
    
    for num in arr:
        if num > max_value:
            max_value = num
        if num < min_value:
            min_value = num
            
    return max_value, min_value

# Example usage
if __name__ == "__main__":
    numbers = [13, 51, 1, 18, 12]
    max_val, min_val = maximum_and_minimum(numbers)
    print(f"Maximum: {max_val}, Minimum: {min_val}")