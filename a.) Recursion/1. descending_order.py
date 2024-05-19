"""
Recursion is a programming technique where a function calls itself directly or
indirectly to solve a problem. 

In recursion, a base condition is a stopping criterion that 
prevents the function from calling itself indefinitely, ensuring the recursion 
terminates. Tail recursion is a special form of recursion where the recursive 
call is the last operation performed in the function. This allows for optimization 
by reusing the same stack frame, reducing memory usage and preventing stack overflow.

Instruction Pointer: It is a register in a computer's CPU that points to the memory 
address of the next instruction to be executed.


Types of Recursion:
Tail Recursion: The recursive call is the last operation in the function.
Non-Tail Recursion: The recursive call is not the last operation in the function.

Tree Method and Stack Method:

Tree Method: In recursion, the tree method visualizes the recursive calls as a
    tree structure, showing the flow of function calls and their relationships.

Stack Method: Recursion uses the call stack to manage function calls, pushing information
    onto the stack when a function is called and popping it off when the function returns.
"""
def descending_order(n):
    if(n <= 0):
        return
    print(n)
    descending_order(n - 1)

descending_order(5)


def ascending_order(n):
    if(n <= 0):
        return
    ascending_order(n - 1)
    print(n)

ascending_order(5)