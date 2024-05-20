def string_reversal(inputStr):
    # Base case: if the input string is empty, return an empty string.
    if len(inputStr) == 0:
        return ""
    
    # Recursive case:
    # Call the function recursively with the substring excluding the first character (inputStr[1:])
    # and concatenate the first character (inputStr[0]) at the end of the result.
    return string_reversal(inputStr[1:]) + inputStr[0]

# Example usage:
print(string_reversal("hello"))  # Output: "olleh"



# Without Substring/Slicing method

def string_reversal_without_substring(inputStr, idx = 0):
        if idx == len(inputStr):
                return ""
        
        left = string_reversal_without_substring(inputStr, idx + 1)
        right = inputStr[idx]
        reversedStr = left + right
        return reversedStr

print(string_reversal_without_substring("hello"))  # Output: "olleh"
        
        
        
        
        