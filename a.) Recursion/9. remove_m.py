"""
Write a recursive function that removes all occurrences of the letter 'm' from a given string. 
The function should take a single string as input and return a new string with all 'm' 
characters removed.
"""

def removeM(string):
    # Base case: If the string is empty, return an empty string
    if len(string) == 0:
        return ""
    
    # If the first character is 'm', skip it and recurse on the rest of the string
    elif string[0] == "m":
        return removeM(string[1:])
    
    # If the first character is not 'm', include it in the result and recurse on the rest of the string
    else:
        return string[0] + removeM(string[1:])

# Example usage
string = "ambmcm"
result = removeM(string)
print(result)  # Output should be "abcm"
