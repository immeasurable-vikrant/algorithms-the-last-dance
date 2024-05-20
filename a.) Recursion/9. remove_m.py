"""
        This function recursively removes all occurrences of the letter 'm' from a string.
        
        Args:
        string: The string to remove 'm' from.
        
        Returns:
        The string with all 'm' characters removed.
"""

def removeM(string):

  if len(string) == 0:
    return ""
  elif string[0] == "m":
    return removeM(string[1:])
  else:
    return string[0] + removeM(string[1:])

# Example usage
string = "ambmcm"
result = removeM(string)
print(result)