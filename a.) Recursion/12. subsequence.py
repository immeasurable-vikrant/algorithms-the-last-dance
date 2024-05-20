def subsequence_of_a_string(str, idx=0, ans=""):
    # Base case: if idx has reached the end of the string, return the current subsequence
    if idx == len(str):
        return [ans]
    
    # Current character to consider
    currStr = str[idx]
    
    # Recursively find subsequences that include the current character
    include = subsequence_of_a_string(str, idx + 1, ans + currStr)
    
    # Recursively find subsequences that do not include the current character
    exclude = subsequence_of_a_string(str, idx + 1, ans)
    
    # Combine the results of both choices
    return include + exclude

# Test the function
print(subsequence_of_a_string("abc"))
