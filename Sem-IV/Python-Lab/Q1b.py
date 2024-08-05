# Write a python program to create a list of tuples having first element as the strings and the second element as the length of the string. Output the list of tuples sorted based on the length of the string.

def create_and_sort_tuples(strings_list):
    # Create a list of tuples (string, length_of_string)
    tuples_list = [(s, len(s)) for s in strings_list]
    
    # Sort the list of tuples based on the length of the strings (second element of the tuple)
    sorted_tuples_list = sorted(tuples_list, key=lambda x: x[1])
    
    return sorted_tuples_list

# Example usage
if __name__ == "__main__":
    # Input: list of strings
    strings_list = ["apple", "banana", "cherry", "date", "elderberry"]
    
    # Create and sort the list of tuples
    sorted_tuples_list = create_and_sort_tuples(strings_list)
    
    # Print the result
    print("Sorted list of tuples based on length of strings:")
    for item in sorted_tuples_list:
        print(item)
