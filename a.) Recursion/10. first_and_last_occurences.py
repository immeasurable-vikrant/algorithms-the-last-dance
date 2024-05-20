def first_and_last_occurrence(s, elem, idx=0, firstIdx=-1, lastIdx=-1):
    # Base case: if index reaches the length of the string, return the results
    if idx == len(s):
        # If lastIdx was not set, it means there was only one occurrence
        if lastIdx == -1:
            lastIdx = firstIdx
        return [firstIdx, lastIdx]

    # Check if the current character matches the element we are looking for
    if s[idx] == elem:
        if firstIdx == -1:
            # Set firstIdx if this is the first occurrence
            firstIdx = idx
        # Always update lastIdx on finding the element
        lastIdx = idx

    # Recur with the next index
    return first_and_last_occurrence(s, elem, idx + 1, firstIdx, lastIdx)

# Test the function
result = first_and_last_occurrence("abaacdaefaah", "a")
print('first:', result[0], ', last:', result[1])
