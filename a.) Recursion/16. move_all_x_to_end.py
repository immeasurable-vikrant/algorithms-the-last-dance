def move_x_to_end(s):
    if not s:
        return ""
    
    first_char = s[0]
    rest_of_string = s[1:]
    
    if first_char == 'x':
        return move_x_to_end(rest_of_string) + first_char
    else:
        return first_char + move_x_to_end(rest_of_string)

# Example usage:
input_string = "abxcxd"
result = move_x_to_end(input_string)
print(result)  # Output: "abcdxx"
