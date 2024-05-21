def remove_duplicates(s, idx=0, ans="", freq_distribution=None):
    # Initialize the frequency distribution array on the first call
    if freq_distribution is None:
        freq_distribution = [False] * 26  # Array to keep track of seen characters

    # Base case: when the index reaches the length of the string, print the answer
    if idx == len(s):
        print(ans)  # Output the resulting string without duplicates
        return

    # Calculate the index for the current character in the frequency array
    char_index = ord(s[idx]) - ord('a')
    
    # If the character hasn't been seen before, add it to the answer
    if not freq_distribution[char_index]:
        ans += s[idx]  # Append the current character to the answer string
        freq_distribution[char_index] = True  # Mark the character as seen

    # Recursive call to process the next character in the string
    remove_duplicates(s, idx + 1, ans, freq_distribution)

# Test the function with a sample input
remove_duplicates("abbaacffbdd")
